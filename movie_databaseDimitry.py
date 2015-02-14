# MPCS 50101 Winter 2015 Midterm
  
import csv
import math
import json
from urllib.request import urlopen


#accessing internet to get the plot
def get_plot_info(imdb_code):
  url = "http://www.omdbapi.com/?i=" +imdb_code + "&plot=short&r=json"
  data = urlopen(url).read().decode()
  result = json.loads(data)
  return result


#defining a key function which will help find the "largest" element in the list of lists
def getKey(item):
    return item[1]


class Movie:
  
    def find_highest_rated(database):

     best_movie = Movie()
     
     #opening the file
     file = open(database)
     reader = csv.reader(file)

     #defining the list 
     master_list = []

     #inputing  .csv file in into a list 
     for row in reader:
       if row:
         inner_list = []   
         id = row[0]
         title = row[1]
         director = row[2]
         rank = row[3]
         year =  row[4]

         inner_list.insert(0, row[1]) #title
         inner_list.insert(1, row[3]) #rank
         inner_list.insert(2, row[2]) #director
         inner_list.insert(3, row[0]) #id
        
         master_list.append(inner_list)
        
     file.close()

    #applying max function from the standard library to find the highest rated movie
     highest_rated = []
     highest_rated.append(max(master_list, key = getKey))
     best_movie.title = highest_rated[0][0] #title
     best_movie.imdb_rating = float(highest_rated[0][1]) #rating
     best_movie.director = highest_rated[0][2] #director 

     return best_movie 

  # def plot(self):
  #      data = get_plot_info(self.id)
  #      return data["Plot"]


      
