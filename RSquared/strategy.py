# import pandas as pd
from datetime import date

# import utils
# import paths
from . import sectors as s
from . import data


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

        # Fama-French history
        self.ff_data = None
        self.fama_french_data()

        # ETF df dates
        self.endETF_date = None
        self.startETF_date = None
        self.etf_dates()

    @property
    def factors_end_date(self):
        return self.endFF_date

    @factors_end_date.setter
    def factors_end_date(self, end):
        self.endFF_date = end

    @property
    def factors_start_date(self):
        return self.startFF_date

    @factors_start_date.setter
    def factors_start_date(self, start):
        self.startFF_date = start

    def fama_french_data(self):
        data_ = data.famaFrenchdownload(start=self.startFF_date,
                                        end=self.endFF_date)[0]/100
        self.ff_data = data_.copy()
        return data_

    def etf_dates(self):
        # Necesito la última fecha del df de FF
        # end: el mismo "endFF_date" con dia 29 (día random)
        # start: restar "lookback_period" al año de "endFF_date"

        self.startETF_date = date(self.endFF_date.year - self.lookback_period,
                                  self.endFF_date.month - 1,
                                  1)
        lastFF_date = self.ff_data.index[-1]
        self.endETF_date = date(lastFF_date.year,
                                lastFF_date.month,
                                29)

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
