import urllib.request

import os

if not os.path.exists("json_files"):
	os.mkdir("json_files")

f = open("api_key", "r")
api_key = f.read()
f.close()



response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/550?api_key="+api_key)
print(response.read())







