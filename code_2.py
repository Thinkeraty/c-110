import plotly.figure_factory as ff
import random
import statistics
import pandas as pd

df = pd.read_csv('data.csv')
data = df['temp'].tolist()

#funtion to get the mean of the given data samples
def random_set_of_mean(counter):
    data_set = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        data_set.append(value)
    
    mean = statistics.mean(data_set)
    
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ['temp'],show_hist=False)
    fig.show()

def setup():
    mean_list = []

    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)


setup()