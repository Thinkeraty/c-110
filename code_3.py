import plotly.figure_factory as ff
import random
import statistics
import pandas as pd

df = pd.read_csv('newdata.csv')
data = df['average'].tolist()

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
    fig = ff.create_distplot([df], ['average'],show_hist=False)
    fig.show()

def setup():
    mean_list = []

    for i in range(0, 10):
        set_of_means = random_set_of_mean(50)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print(mean)


setup()

# mean of raw data
population_mean = statistics.mean(data)
print(population_mean)

def std_dev():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_dev = statistics.stdev(mean_list)
    print(std_dev)

std_dev()
