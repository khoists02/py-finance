# This is a sample Python script.
# from io import StringIO
from pandas_module import PandasModule
from yahoo_lib.quaterly.cashflow import QuaterlyCashflow
from yahoo_lib.quaterly.balance_sheet import QuaterlyBalanceSheet
# from yahoo_lib import FinancialModule
from matplot.plot import Plot
# from matplot.histogram import Histogram
# from matplot.pie import Pie
from helpers import format_date_from_timestamp, reverse
import pandas as pd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
plots = ['Financing Cash Flow', 'Free Cash Flow', 'Sale Of Investment']


# default_data = np.array([[1,2], [3,4], [5,6]])

def draw_histogram():
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    lazr = pd.read_csv('data/LAZR-max.csv')
    print(lazr.head(5))
    title = 'Distribution of Adj Close LAZR'
    # TODO Histogram
    # chart = Histogram(lazr['Adj Close'], bins=bins, xlabel='Adj Close', ylabel='Number of days', title=title)
    # chart.draw()

    # Pie chart
    # TODO: count close more than 3 or less than or equal testing. and how to use loc function in dataframe
    # prefer doc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
    # Access a group of rows and columns by label(s) or a boolean array.

    more_than_three = lazr.loc[lazr['Adj Close'] > 3].count()[0]  # couting close value more than 3.0
    mt_five_and_lesst_seven = lazr.loc[(lazr['Adj Close'] > 5) & (lazr['Adj Close'] < 7)].count()[
        0]  # Multiple condition in loc function.
    less_than_or_equal_three = lazr.loc[lazr['Adj Close'] < 3].count()[0]
    print(more_than_three, less_than_or_equal_three)
    print(mt_five_and_lesst_seven)
    # pie = Pie([more_than_three, less_than_or_equal_three], labels=['More Than Three', 'Less Than Or Equal'], colors=['red', 'yellow'])
    # pie.draw()


"""
    Histogram chart
"""
if __name__ == '__main4__':
    draw_histogram()

# Press the green button in the gutter to run the script.

"""
    Cashflow  with plot chart
"""
if __name__ == '__main1__':
    # TODO: new instance
    # TODO: load data
    quaterly_cashflow = QuaterlyCashflow("LAZR")

    date_keys = quaterly_cashflow.get_quarterly_cashflow_keys()
    # defined init x, y values
    k_labels = []
    k_values = []

    for i, plt in enumerate(plots):
        # TODO: Convert keys to datetime format.
        values = []
        labels = []
        for idx, key in enumerate(date_keys):
            # TODO: get values of label. 1M
            result = quaterly_cashflow.get_quarterly_cashflow__values_by_index_and_label(idx, plt)
            values.append(result / 1000 if result else 0)
            labels.append(format_date_from_timestamp(timestamp=key, date_format='%m-%Y'))

        result_arr = reverse(values)
        k_values.append(result_arr)

        k_labels = labels
    # TODO: Matplot working here.
    plot = Plot(reverse(k_labels), k_values, plots)
    plot.draw()

"""
    Balance sheet with plot chart
"""
if __name__ == '__main4__':
    # TODO: new instance
    quaterly_balanace_sheet = QuaterlyBalanceSheet("LAZR")
    date_keys = quaterly_balanace_sheet.get_quarterly_balance_keys()

    # defined init x, y values
    b_labels = []
    b_values = []

    # print(quaterly_balanace_sheet.get_labels_of_balance_obj())
    b_plots = quaterly_balanace_sheet.get_labels_of_balance_obj()[1:3]
    # print(b_plots)
    for i, plt in enumerate(b_plots):
        # TODO: Convert keys to datetime format.
        values = []
        labels = []
        for idx, key in enumerate(date_keys):
            # TODO: get values of label. 1M
            result = quaterly_balanace_sheet.get_quarterly_balance_values_by_index_and_label(idx, plt)
            values.append(result / 1000 if result else 0)
            labels.append(format_date_from_timestamp(timestamp=key, date_format='%m-%Y'))

        result_arr = reverse(values)
        b_values.append(result_arr)

        b_labels = labels

    # TODO: Matplot working here.
    plot = Plot(reverse(b_labels), y=b_values, plots=b_plots)
    plot.draw()

if __name__ == '__main__':
    # TODO: Pandas module with yFinance module
    df = PandasModule.load_data_frame_from_yahoofincance('LAZR')

    # TODO: find min,max rows
    max_close = df['Close'].max()
    min_close = df['Close'].min()

    max_rows = df.loc[df['Close'] == max_close]
    min_rows = df.loc[df['Close'] == min_close]

    # print(max_rows['Date'], max_rows['Close'])
    print(min_rows)
