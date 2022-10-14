import json
import pandas
import glob
import os

if not os.path.exists('parsed_files'):
	os.mkdir('parsed_files')

df = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):

	# json_file_name = "json_files/tmdb_1032398.json"
	f = open(json_file_name, "r")
	json_data = json.load(f)
	f.close()


	movie_id = json_data['id']
	movie_title = json_data['title']
	vote_average = json_data['vote_average']
	vote_count =  json_data['vote_count']
	adult = json_data['adult']*1
	popularity = json_data['popularity']
	budget = json_data['budget']
	release_date = json_data['release_date']
	revenue = json_data['revenue']
	runtime = json_data['runtime']
	status = json_data['status']
	imdb_id = json_data['imdb_id']

	genres = ";".join([item['name'] for item in json_data['genres']])
	production_countries = ";".join([item['iso_3166_1'] for item in json_data['production_countries']])


	df = pandas.concat([df, 
			pandas.DataFrame.from_records([{
			'movie_id': movie_id,
			'movie_title': movie_title,
			'vote_average': vote_average,
			'vote_count': vote_count,
			'adult': adult,
			'popularity': popularity,
			'budget' : budget,
			'release_date' : release_date,
			'revenue' : revenue,
			'runtime' : runtime,
			'status' : status,
			'genres' : genres,
			'production_countries' : production_countries,
			'imdb_id': imdb_id
			}])
		 ])


# print(df)


df.to_csv("parsed_files/tmdb_dataset.csv", index=False)

print("done")














