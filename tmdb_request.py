import urllib.request
import json
import os
import time

if not os.path.exists("json_files"):
	os.mkdir("json_files")

f = open("api_key", "r")
api_key = f.read()
f.close()


response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/latest?api_key="+api_key)
json_response = json.load(response)

movie_max = int(json_response['id'])
movie_min = movie_max - 20
# movie_min = 0

# print(movie_max)


for movie_id in range(movie_min, movie_max):
	file_name = "json_files/tmdb_" + str(movie_id ) 

	if os.path.exists(file_name + ".json"):
		print("File exists", movie_id)
	else:
		print("Downloading: ", movie_id)
		response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movie_id) +  "?api_key="+api_key)
		json_response = json.load(response)

		f = open(file_name + ".tmp", "w")
		f.write(json.dumps(json_response))
		f.close()

		time.sleep(1)
		os.rename(file_name + ".tmp", file_name + ".json")
		print("Waiting 15 seconds")
		time.sleep(15)
















