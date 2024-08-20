from io import StringIO
from yahoo_lib import FinancialModule
import pandas as pd

class PandasModule:
    def __init__(self):
        pass

    @staticmethod
    def load_data_frame_from_yahoofincance(ticker):
        ticker = FinancialModule(ticker)
        csv_str = ticker.export_histories_to_csv()
        return pd.read_csv(StringIO(csv_str), dtype=str)


