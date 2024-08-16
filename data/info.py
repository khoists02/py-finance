import yfinance as yf
import json

class FinancialData:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_ticker_info(self) -> str:
        return  yf.Ticker(self.ticker).info

    def get_quarterly_cashflow(self):
        data = yf.Ticker(self.ticker).quarterly_cashflow
        return  json.loads(data.to_json())

    ### TODO: Date keys
    def get_quarterly_cashflow_keys(self) -> list[str]:
        return  list(self.get_quarterly_cashflow().keys())

    def get_quarterly_cashflow_keys_of_values(self) -> list[str]:
        allvalues = list(self.get_quarterly_cashflow().values())
        one_vl = allvalues[0]
        return  list(one_vl.keys())

    def get_quarterly_cashflow__values_by_index_and_label(self, index, label):
        return  list(self.get_quarterly_cashflow().values())[index][label]

