import pandas as pd
from matplot.histogram import Histogram
bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
lazr = pd.read_csv('LAZR.csv')

chart = Histogram(lazr['Adj Close'], bins=bins, xlabel='Adj Close', ylabel='Number of days', title='Distribution of '
                                                                                                   'Adj Close LAZR')
chart.draw()


