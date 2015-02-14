import csv

import json
from urllib.request import urlopen


class Movie:

	def find_highest_rated(filename):
		with open(filename, "r", encoding="utf-8") as f:
			data = csv.DictReader(f, fieldnames= ("id", "title", "director", "imdb_rating", "year_released"))
			
			highest_rated = "2"
			highest_row = None

			for row in data:
				if row["imdb_rating"] > highest_rated:
					highest_row = row
					highest_rated = row["imdb_rating"]
			
			x = Movie()
			x.id = highest_row["id"]
			x.title = highest_row["title"]
			x.imdb_rating = float(highest_row["imdb_rating"])
			x.year = highest_row["year_released"]
			x.director = highest_row["director"]
		return x

	def plot(self):
		
		webservice_url = "http://www.omdbapi.com/?i=" + self.id + "&plot=short&r=json"
		data = urlopen(webservice_url).read().decode("utf8")
		result = json.loads(data)
		movieplot = result["Plot"]
		return movieplot


