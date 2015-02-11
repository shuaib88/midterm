import csv

class Movie:
	pass

	def find_highest_rated(self):
		pass

	def title(self):
		pass

	def imdb_rating(self):
		pass

	def director(self):
		pass

	def plot(self):
		pass

def read_movie_data():
	with open("imdb_top250.csv", "r", encoding="utf-8") as csvFile:
		movieReader = csv.reader(csvFile, delimiter=",")

		movieList = []

		for row in movieReader:
			movie = Movie()
			movie.title = 


##had trouble doing a few things opening the csv file and creating objects
##also had trouble just getting the best_movie to pass assertion even though i created a Movie class
##I know i create a for loop that loopst through the movie file
I can use a similar method to the divvy problem to keep track of the highest rating
then I can 


# best_movie = Movie.find_highest_rated('imdb_top250.csv') 



