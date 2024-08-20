import pandas as pd

df = pd.read_csv("../data/fifa_data.csv")
print(df.columns)

# print(df['GKDiving'].max())
# print(df['Age'].max())

max_age = df['Age'].max()
min_age = df['Age'].min()

older = df.loc[df['Age'] == max_age]
younger = df.loc[df['Age'] == min_age]

"""
    How to use loc, iloc in pandas.
"""


