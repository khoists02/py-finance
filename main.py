# This is a sample Python script.
from data.info import FinancialData
from matplot.index import Matplot
from helpers.format import format_date_from_timestamp
from helpers.helper import reverse
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
FONTDICS = {'fontname': 'Comic Sans MS', 'fontsize': 16, 'color': '#d1d1d1'}

# Multiple data plot

plots = ['Operating Gains Losses', 'Financing Cash Flow', 'Free Cash Flow', 'Sale Of Investment']

# default_data = np.array([[1,2], [3,4], [5,6]])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: new instance
    new_data = FinancialData("LAZR")
    keys = new_data.get_quarterly_cashflow_keys()
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
            labels.append(format_date_from_timestamp(timestamp=key, date_format='%d-%m-%Y'))

        result_arr = reverse(values)
        k_values.append(result_arr)

        k_labels = labels
    # TODO: show chart.
    plot = Matplot(reverse(k_labels), k_values, plots)
    plot.draw()
