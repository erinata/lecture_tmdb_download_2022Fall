import pandas
import numpy

import matplotlib.pyplot as plt

dataset = pandas.read_csv("parsed_files/tmdb_dataset.csv")

print(dataset)
print(dataset.describe())
print("--------------")


###  Check how many movies has vote average 0
# dataset['zero_score'] = (dataset['vote_average'] == 0)*1
# print(dataset['zero_score'].sum())

### Generate new column by a condition
# dataset['popular'] = (dataset['popularity'] > 30)*1


# ### count missing values and drop them
# print(dataset.isna().sum())
# dataset = dataset.dropna(subset=['release_date'])
# print(dataset.isna().sum())



### Replace NaN with empty string
dataset['genres'] = dataset['genres'].fillna("")
dataset['production_countries'] = dataset['production_countries'].fillna("")




# dataset['Adventure'] = (dataset["genres"].str.contains("Adventure"))*1
# dataset['History'] = (dataset["genres"].str.contains("History"))*1


def flatten(input_list):
	return [item for sublist in input_list for item in sublist]

def get_unique_list(series, sep):
	input_list = [i.split(sep) for i in series]
	return list(set(flatten(input_list)))
	

for genre in get_unique_list(dataset['genres'], ";"):
	dataset["genre_" + genre] = (dataset["genres"].str.contains(genre))*1
	
	
for country in get_unique_list(dataset['production_countries'], ";"):
	dataset["country_" + country] = (dataset["production_countries"].str.contains(country))*1
	
	
dataset['the'] = (dataset["movie_title"].str.contains("the ", case=False))*1




print(dataset)
print(dataset.describe())





# sub_dataset = dataset[ (dataset['budget']>0) & (dataset['revenue']>0) ]

# print(sub_dataset)
# print(sub_dataset.describe())

# revenue = sub_dataset['revenue']
# budget = sub_dataset['budget']
# vote_average = sub_dataset['vote_average']
# horror = sub_dataset['genre_Horror']

# logrevenue = numpy.log(revenue)
# logbudget = numpy.log(budget)


# plt.scatter(logbudget, logrevenue, c=horror)
# plt.title("Budget and Revenue")
# plt.ylabel("Revenue")
# plt.xlabel("Budget")
# plt.colorbar()
# plt.savefig('figure.png')



