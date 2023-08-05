import re
import numpy as np
import pandas as pd
import mplfinance as mpf
from functools import wraps
from datetime import datetime, timedelta


def assert_dataframe(method):
    @wraps(method)
    def inner(*args, **kwargs):
        # print("data" in kwargs.keys())
        data = args[1]
        if "data" in kwargs.keys():
            data = kwargs["data"]
        assert (
            type(data) == pd.DataFrame
        ), "data should be a pandas DataFrame but it is a" + str(type(data))
        assert (
            type(data.index) == pd.DatetimeIndex
        ), "data should have pandas Datetime as index but it is a" + str(
            type(data.index)
        )
        return method(*args, **kwargs)

    return inner


class TimeframeConverter:
    # timeframes

    M1 = "1m"
    M3 = "3m"
    M5 = "5m"
    M10 = "10m"
    M15 = "15m"
    M30 = "30m"

    H1 = "1h"
    H2 = "2h"
    H3 = "3h"
    H4 = "4h"

    D = "d"
    W = "w"

    def __init__(
        self,
        ohlc_columns=["Open", "High", "Low", "Close"],
        other_column_drop=True,
        intraday_start_time="9:16",
        intraday_end_time="15:30",
    ):
        self.ohlc = ohlc_columns
        self.other_column_drop = other_column_drop
        self.intraday_start_time = intraday_start_time
        self.intraday_end_time = intraday_end_time

        start_time = datetime.strptime(intraday_start_time, "%H:%M")
        end_time = datetime.strptime(intraday_end_time, "%H:%M")

        time_diff = end_time - start_time
        self.trading_time_minutes = time_diff.seconds / 60 + 1

    def _build_row(self, subset):
        col_list = []

        col_list.append(subset.index[0])
        subset = subset.to_numpy()
        col_list.append(subset[0][0])
        col_list.append(np.max(subset))
        col_list.append(np.min(subset))
        col_list.append(subset[-1][-1])

        return col_list

    def _list_to_df(self, df_list, ref_data):
        coverted_df = pd.DataFrame(np.array(df_list))
        columns = list(ref_data.columns)
        columns.insert(0, ref_data.index.name)
        coverted_df.columns = columns
        coverted_df.set_index(ref_data.index.name, drop=True, inplace=True)

        return coverted_df.apply(pd.to_numeric)

    def _convert(self, data):
        i = 0
        df_list = []
        while i < len(data.index):
            j = i + self.timeframe_multiplier
            subset = data.iloc[i:j, :]
            col_list = self._build_row(subset)
            i += self.timeframe_multiplier

            df_list.append(col_list)

        return df_list

    def _intraday_convert(self):
        self.data["TimeF"] = self.data.index.to_series().apply(
            lambda x: (x.hour * 100) + x.minute
        )
        self.data = self.data[
            self.data.TimeF >= int(self.intraday_start_time.replace(":", ""))
        ]
        self.data = self.data[
            self.data.TimeF <= int(self.intraday_end_time.replace(":", ""))
        ]
        self.data.drop("TimeF", axis=1, inplace=True)

        self.data["Date"] = self.data.index.date

        df_list = []

        for date in self.data["Date"].unique():
            day_df = self.data[self.data["Date"] == date]
            day_df.drop("Date", axis=1, inplace=True)

            df_list.extend(self._convert(day_df))

        self.data.drop("Date", axis=1, inplace=True)

        return self._list_to_df(df_list, self.data)

    @assert_dataframe
    def intraday_min_to_min(
        self, data: pd.DataFrame, source_timeframe, target_timeframe
    ):
        source_timeframe = int(re.findall("[0-9]+", source_timeframe)[0])
        target_timeframe = int(re.findall("[0-9]+", target_timeframe)[0])

        assert (
            source_timeframe < target_timeframe
        ), "Can not convert from higher timeframe to lower timeframe"
        assert (
            target_timeframe % source_timeframe == 0
        ), "Can not convert to a target timeframe that is not a multiple of source timeframe"

        self.data = data
        self.timeframe_multiplier = int(target_timeframe / source_timeframe)

        return self._intraday_convert()

    @assert_dataframe
    def intraday_min_to_hour(self):
        pass

    @assert_dataframe
    def intraday_hour_to_hour(self):
        pass

    @assert_dataframe
    def intraday_to_day(self, data: pd.DataFrame, source_timeframe):
        assert (
            "m" in source_timeframe or "h" in source_timeframe
        ), "Timeframe other than minutes and hours not supported for Daily CPR"

        self.data["Date"] = self.data.index.date

        df_list = []
        for date in self.data["Date"].unique():
            day_df = self.data[self.data["Date"] == date]
            day_df.drop("Date", axis=1, inplace=True)

            df_list.append(self._build_row(day_df))

        self.data.drop("Date", axis=1, inplace=True)

        converted_df = self._list_to_df(df_list, self.data)
        converted_df["Date"] = converted_df.index.date
        converted_df.set_index("Date", inplace=True, drop=True)

        return converted_df

    @assert_dataframe
    def intraday_to_week(self):
        pass

    @assert_dataframe
    def day_to_week(self):
        pass


class CPR(TimeframeConverter):
    def __init__(self, s_r_depth=4):
        assert s_r_depth <= 4, "depth can not be more than 4"
        assert s_r_depth >= 0, "depth can not be negative"

        self.s_r_depth = s_r_depth
        super().__init__()

    def _compute_pivots(self, data):
        dh = data["High"].shift(1)
        dl = data["Low"].shift(1)
        dc = data["Close"].shift(1)

        data["pivot"] = (dh + dl + dc) / 3
        data["bc"] = (dh + dl) / 2
        data["tc"] = (data["pivot"] - data["bc"]) + data["pivot"]
        data["pdh"] = dh
        data["pdl"] = dl

        if self.s_r_depth > 0:
            data["r1"] = (2 * data["pivot"]) - dl
            data["s1"] = (2 * data["pivot"]) - dh
        else:
            return data

        if self.s_r_depth > 1:
            data["r2"] = data["pivot"] + (data["r1"] - data["s1"])
            data["s2"] = data["pivot"] - (data["r1"] - data["s1"])
        else:
            return data

        if self.s_r_depth > 2:
            data["r3"] = dh + 2 * (data["pivot"] - dl)
            data["s3"] = dl - 2 * (dh - data["pivot"])
        else:
            return data

        if self.s_r_depth > 3:
            data["r4"] = dh + 3 * (data["pivot"] - dl)
            data["s4"] = dl - 3 * (dh - data["pivot"])
        else:
            return data

        return data

    @assert_dataframe
    def daily_cpr(self, data: pd.DataFrame, source_timeframe):
        self.data = data

        if "d" in source_timeframe.lower():
            data_D = self.data
        else:
            data_D = self.intraday_to_day(self.data, source_timeframe)

        return self._compute_pivots(data_D)

    @assert_dataframe
    def plot_cpr(
        self,
        data,
        target_date_str,
        source_timeframe,
        s_r_depth=4,
        cpr="daily",
        ta_columns=[],
    ):
        assert s_r_depth <= self.s_r_depth, (
            "s_r_depth can not be greater than " + self.s_r_depth
        )
        assert type(ta_columns) == list, "ta_columns has to be a list"

        ta_data = data[ta_columns]
        data = data[self.ohlc]

        target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
        dates = list(np.unique(data.index.date))
        target_date_index = dates.index(target_date)

        assert (
            target_date_index != 0
        ), "Insufficient data to compute CPR for the given target date"

        cpr_date = dates[target_date_index - 1]
        base_data = data.loc[cpr_date: target_date + timedelta(days=1)]
        cpr_data = self.daily_cpr(base_data, source_timeframe).tail(1)

        target_data = data[data.index.date == target_date]
        target_data_array = target_data.to_numpy()

        pivot_lines = []
        pivot_colors = ["m", "b", "b", "k", "k"]
        s_list = ["s1", "s2", "s3", "s4"]
        r_list = ["r1", "r2", "r3", "r4"]

        pivot_lines.append(cpr_data["pivot"].values[0])
        pivot_lines.append(cpr_data["bc"].values[0])
        pivot_lines.append(cpr_data["tc"].values[0])
        pivot_lines.append(cpr_data["pdh"].values[0])
        pivot_lines.append(cpr_data["pdl"].values[0])

        flag = 0
        for i in s_list[:s_r_depth]:
            s = cpr_data[i].values[0]
            if s < target_data_array.min():
                flag += 1
                if flag > 1:
                    break
            pivot_lines.append(s)
            pivot_colors.append("g")

        flag = 0
        for i in r_list[:s_r_depth]:
            r = cpr_data[i].values[0]
            if r > target_data_array.max():
                flag += 1
                if flag > 1:
                    break
            pivot_lines.append(r)
            pivot_colors.append("r")

        additional_plots = []
        ta_data = ta_data[ta_data.index.date == target_date]

        for indicator in ta_columns:
            additional_plots.append(mpf.make_addplot(ta_data[indicator]))

        mpf.plot(
            target_data,
            addplot=additional_plots,
            style="charles",
            type="candle",
            figsize=(20, 10),
            hlines=dict(hlines=pivot_lines, colors=pivot_colors,
                        linestyle="dotted"),
            title=target_date_str,
        )
