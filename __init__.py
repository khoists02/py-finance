# This is a sample Python script.
from data.info import FinancialData
from matplot.plot import Plot
from matplot.histogram import Histogram
from helpers import format_date_from_timestamp, reverse
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
plots = ['Financing Cash Flow', 'Free Cash Flow', 'Sale Of Investment']


# default_data = np.array([[1,2], [3,4], [5,6]])

def draw_histogram():
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    lazr = pd.read_csv('./luminar/LAZR.csv')
    title = 'Distribution of Adj Close LAZR'
    # TODO print data
    chart = Histogram(lazr['Adj Close'], bins=bins, xlabel='Adj Close', ylabel='Number of days', title=title)
    chart.draw()


if __name__ == '__main1__':
    draw_histogram()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: new instance
    # TODO: load data
    new_data = FinancialData("LAZR")
    keys = new_data.get_quarterly_cashflow_keys()
    # defined init x, y values
    k_labels = []
    k_values = []

    for i, plt in enumerate(plots):
        # TODO: Convert keys to datetime format.
        values = []
        labels = []
        for idx, key in enumerate(keys):
            # TODO: get values of label. 1M
            result = new_data.get_quarterly_cashflow__values_by_index_and_label(idx, plt)
            values.append(result / 1000 if result else 0)
            labels.append(format_date_from_timestamp(timestamp=key, date_format='%m-%Y'))

        result_arr = reverse(values)
        k_values.append(result_arr)

        k_labels = labels
    # TODO: Matplot work.
    plot = Plot(reverse(k_labels), k_values, plots)
    plot.draw()
