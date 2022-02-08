import statistics
import pandas as pd
import plotly.figure_factory as ff
import random 
import plotly.graph_objects as gb

df = pd.read_csv("det.csv")
data = df['reading_time'].tolist()

def random_setMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    print(mean)

    fig = ff.create_distplot([df],["Reding"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_setMean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)
    std_dev=statistics.stdev(mean_list)
    print(std_dev)

setup()