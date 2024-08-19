import yfinance as yf


class FinancialModule:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_ticker_info(self) -> dict:
        return yf.Ticker(self.ticker).info

