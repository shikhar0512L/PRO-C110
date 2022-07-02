import csv
import random
import pandas as pd 
import statistics
import plotly.graph_objects as go 
import plotly.figure_factory as ff 

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist() 


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean 

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.show()

def set_up():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print('mean of sampling distribution',mean)

set_up()

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print('stadard deviation of sampling distrabution',std_deviation)
standard_deviation()