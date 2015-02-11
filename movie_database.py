import csv

class Movie:
	pass

	def find_highest_rated(self, file):
		pass

def read_movie_data():
	with open("imdb_top250.csv", "r", encoding="utf-8") as csvFile:
		movieReader = csv.reader(csvFile, delimiter=",")

		movieList = []

		for row in movieReader:
			movie = Movie()
			movie.imdbID = row[0]
			movieList.append(movie)

	return movieList

read_movie_data()
movieList


# best_movie = Movie.find_highest_rated('imdb_top250.csv') 



