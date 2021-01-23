import plotly.figure_factory as ff
import random
import statistics
import pandas as pd

df = pd.read_csv('data.csv')
data = df['temp'].tolist()
population_mean = statistics.mean(data)

fig = ff.create_distplot([data], ['temp'], show_hist=False)
fig.show()