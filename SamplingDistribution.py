import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

data = pd.read_csv('data.csv')
data = data["claps"].tolist()
print(data)

PopulationMean = statistics.mean(data)
print(PopulationMean)

PopulationSD = statistics.stdev(data)
print(PopulationSD)

def Sample():
    samples = []
    for i in range (0,30):
        randomClaps = random.randint(0,len(data)-1)
        value = data[randomClaps]
        samples.append(float(value))

    SampleMean = statistics.mean(samples)
    #print(SampleMean)

    SampleStandardDeviation = statistics.stdev(samples)
    #print(SampleStandardDeviation)
    return(SampleMean)


SampleMeans = []

for i in range (0,100):
    Means = Sample()
    SampleMeans.append(float(Means) )

graph = ff.create_distplot([SampleMeans], ["Means"], show_hist = False)
graph.show()