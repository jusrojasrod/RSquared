# import utils
# import paths
import sectors as s
import data


class Strategy:

    tickers = s.ETF_sectors

    def __init__(self, y_back=5, start=None, end=None):

        self.start = start
        self.end = end
        self.y_back = y_back

        self._ff_data = None

    def etf_dates(self):
        pass

    def factors_dates(self):
        pass

    def set_fama_french_data(self):
        self._ff_data = data.famaFrenchdownload(self.start, self.end)[0]/100

    def set_momento_data():
        pass

    def set_etf_data(self, tickers):
        self._ETFdata = data.downloadData(tickers,
                                          start=self.start, end=self.end)

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
