import csv

from urllib.request import urlopen
# look this up and become familiar with these modules
import json

class Movie:
	def find_highest_rated(filename):
		with open(filename, "r", encoding="utf-8") as csvfile:
			# Where is the documentation for with open
			reader = csv.DictReader(csvfile,fieldnames = ("imdb_id", "title", "director", "rating", "year"))
			# what's the difference between csv.DictReader and csv.DictWriter
			# what's the difference between csv.Reader and csv.DictReader
			highest_value = "2"
			highest_rated_movieDict = None

			for row in reader:
				if row["rating"] > highest_value:
					highest_rated_movieDict = row
					highest_value = row["rating"]

			highest_rated_movie_object = Movie()
			highest_rated_movie_object.id = highest_rated_movieDict["imdb_id"]
			highest_rated_movie_object.title = highest_rated_movieDict["title"]
			highest_rated_movie_object.imdb_rating = float(highest_rated_movieDict["rating"])
			highest_rated_movie_object.director = highest_rated_movieDict["director"]
		return highest_rated_movie_object

	def plot(self):
			#take any movie object and return the plot in string format
			webservice_url = "http://www.omdbapi.com/?i=" + self.id + "&plot=short&r=json"
			data = urlopen(webservice_url).read().decode("utf8")
			result = json.loads(data)

			return result["Plot"]
