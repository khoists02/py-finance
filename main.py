# This is a sample Python script.
import matplotlib.pyplot as plt
from data.info import FinancialData
from datetime import datetime
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
FONTDICS = {'fontname': 'Comic Sans MS', 'fontsize': 16, 'color': '#d1d1d1'}

# default_data = np.array([[1,2], [3,4], [5,6]])

def plot_example(x, y, label):
    plt.plot(x, y, color='red') # o = marker.
    plt.ylabel(label)
    plt.show()

def reverse(lst):
    new_lst = lst[::-1]
    return new_lst

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: new instance
    new_data = FinancialData("LAZR")
    keys = new_data.get_quarterly_cashflow_keys()

    # print(new_data.get_quarterly_cashflow_keys_of_values())
    values = []
    # TODO: Convert keys to datetime format.
    labels = []
    for idx, key in enumerate(keys):
        result = new_data.get_quarterly_cashflow__values_by_index_and_label(idx, 'Purchase Of PPE')
        values.append(result if result else 0)
        # format datetime
        date = datetime.fromtimestamp(int(key) / 1e3)
        labels.append(date.strftime('%Y-%m-%d'))
    # plot_example(reverse(labels), reverse(values), 'Purchase Of PPE')

