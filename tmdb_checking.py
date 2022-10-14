import pandas
import numpy

import matplotlib.pyplot as plt

dataset = pandas.read_csv("parsed_files/tmdb_dataset.csv")

print(dataset)
print(dataset.describe())


sub_dataset = dataset[ (dataset['budget']>0) & (dataset['revenue']>0) ]

print(sub_dataset)
print(sub_dataset.describe())

revenue = sub_dataset['revenue']
budget = sub_dataset['budget']
vote_average = sub_dataset['vote_average']

logrevenue = numpy.log(revenue)
logbudget = numpy.log(budget)


plt.scatter(logbudget, logrevenue, c=vote_average)
plt.title("Budget and Revenue")
plt.ylabel("Revenue")
plt.xlabel("Budget")
plt.colorbar()
plt.savefig('figure.png')



