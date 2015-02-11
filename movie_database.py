import csv

class Movie:
	pass

	def find_highest_rated(self):
		with open("imdb_top250.csv", "r", encoding="utf-8") as csvFile:
			movieReader = csv.reader(csvFile, delimiter=",")

			movieList = []

			for row in movieReader:
				movie = Movie()
				movie.title = row[1]
				movie.imdb_rating = row[3]
				movie.director = row[2]
				#movie.plot = have to access the API using the url
				movieList.append(movie)


##had trouble doing a few things opening the csv file and creating objects
##also had trouble just getting the best_movie to pass assertion even though i created a Movie class
##I know i create a for loop that loopst through the movie file
# I can use a similar method to the divvy problem to keep track of the highest rating
# I also need to loop through the csv file
# and build a new object with attributes for title, imdb_rating, director, plot etc... 
#for the plot 



# best_movie = Movie.find_highest_rated('imdb_top250.csv') 



