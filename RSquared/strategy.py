# import pandas as pd
from datetime import date

# import utils
# import paths
from . import sectors as s
# from . import data


class Strategy:

    TICKERS = s.ETF_sectors

    def __init__(self, lookback_period=5, start=None, end=date.today(),
                 column_name="Close"):
        self.column_name = column_name
        self.lookback_period = lookback_period

        # Fama-French dates
        self.endFF_date = end
        self.startFF_date = start
        if start is None:
            self.startFF_date = date(self.endFF_date.year
                                     - self.lookback_period,
                                     self.endFF_date.month,
                                     self.endFF_date.day)

    @property
    def factors_end_date(self):
        return self.endFF_date

    @factors_end_date.setter
    def factors_end_date(self, end):
        self.endFF_date = end

    @property
    def factors_start_date(self):
        return self.start_ff

    @factors_start_date.setter
    def factors_start_date(self, start):
        self.startFF_date = start

    # def etf_dates(self):
    #     # self.start_etf = date(self.end_ff.year - self.y_back,
    #     #                       self.end_ff.month - 1,
    #     #                       1)
    #     # last_ff_date = self._ff_data.index[-1]
    #     # self.end_etf = date(last_ff_date.year,
    #     #                     last_ff_date.month,
    #     #                     29)
    #     pass

    # def set_fama_french(self):
    #     # self._ff_data = data.famaFrenchdownload(start=self.start_ff,
    #     #                                         end=self.end_ff)[0]/100
    #     pass

    # def get_fama_french(self):
    #     # if self._ff_data:
    #     #     self._ff_data = self._set_fama_french()
    #     # return self._ff_data
    #     pass

    # def set_momento_data():
    #     pass

    # def set_etf_data(self):
    #     # df = data.downloadData(tickers=self.symbols,
    #     #                        start=self.start_etf,
    #     #                        end=self.end_etf)[self.column_name]
    #     # return df
    #     # self._etf_data = pd.datetime(df.index,
    #     #                              format="%Y%m").to_period("M")
    #     # # print(df)
    #     pass

    # def concat_factors():
    #     pass

    # def returns():
    #     pass

    # def excess_return():
    #     pass

    # def plot_returns():
    #     pass

    # def _regression():
    #     pass

    # def join_reg_factors():
    #     pass

    # def r_squared():
    #     pass

    # def strategy():
    #     pass
