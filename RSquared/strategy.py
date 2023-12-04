import pandas as pd
from datetime import date

# import utils
# import paths
from . import sectors as s
from . import data


class Strategy:

    symbols = s.ETF_sectors

    def __init__(self, y_back=5, start=None, end=date.today(),
                 column_name="Close"):
        self.column_name = column_name

        # Fama-French dates
        self.start_ff = start
        self.end_ff = end

        # ETFs dates
        self.start_etf = None
        self.end_etf = None
        self.y_back = y_back

        self._ff_data = None

        self.set_fama_french()
        # initialize dates
        self.set_factors_dates()
        self.set_etf_dates()

        # Initialize fama-franch and ETF data

        self.set_etf_data()

    def set_etf_dates(self):
        self.start_etf = date(self.end_ff.year - self.y_back,
                              self.end_ff.month - 1,
                              1)
        last_ff_date = self._ff_data.index[-1]
        self.end_etf = date(last_ff_date.year,
                            last_ff_date.month,
                            29)

    def set_factors_dates(self):
        if self.start_ff is None:
            self.start_ff = date(self.end_ff.year - self.y_back,
                                 self.end_ff.month,
                                 self.end_ff.day)

    def set_fama_french(self):
        self._ff_data = data.famaFrenchdownload(start=self.start_ff,
                                                end=self.end_ff)[0]/100

    def get_fama_french(self):
        if self._ff_data:
            self._ff_data = self._set_fama_french()
        return self._ff_data

    def set_momento_data():
        pass

    def set_etf_data(self):
        df = data.downloadData(tickers=self.symbols,
                               start=self.start_etf,
                               end=self.end_etf)[self.column_name]
        return df
        self._etf_data = pd.datetime(df.index,
                                     format="%Y%m").to_period("M")
        # print(df)

    def concat_factors():
        pass

    def returns():
        pass

    def excess_return():
        pass

    def plot_returns():
        pass

    def _regression():
        pass

    def join_reg_factors():
        pass

    def r_squared():
        pass

    def strategy():
        pass
