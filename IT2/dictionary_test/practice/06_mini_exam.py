"""
Exercise 06 - Mini exam (suggested time: 30 minutes)

Solve the tasks TWICE, both with movies_list and with movies_dict.
Each movie has been rated 1-6 by four critics. "-" means the critic did not rate the movie.

Useful tools:
  sorted(d, key=d.get, reverse=True)      if value != "-":
  sum() / len()                           if key not in d: d[key] = []
  row[3:]                                 enumerate(my_list, 1)
  round(x, 2)                             [:10]

a) Make a list of the four critics, sorted by the average rating each critic gives (highest first).
   Hint: column averages, then sorted() with key=.

b) Make a list of the genres, sorted by the average of ALL ratings given to movies in that genre.
   Hint: group by genre (dict of lists), and add every valid rating from the row to the list.

c) Make a new variable with the same content, where the four ratings are in one list.
   Print the information for the first movie to show the new data structure.
   Hint: row[3:] / a "Ratings" key.

d) Make a list of the ten best movies based on their average rating.
   Print them with their place, title and average.
   Hint: divide by the number of real ratings. Then [:10] and enumerate().

e) Count how many movies there are from each decade (1980s, 1990s, ...),
   and print the decades in order.
   Hint: year // 10 * 10 gives the decade. Count with a dict, then sorted() on the keys.
"""

headers = ["Title", "Genre", "Year", "Critic 1", "Critic 2", "Critic 3", "Critic 4"]

movies_list = [
  ["The Last Fjord", "Action", 1994, 6, 1, 2, 5],
  ["Midnight Code", "Drama", 2008, 6, 1, 4, 6],
  ["Red Harbour", "Drama", 1990, 1, 1, 2, 1],
  ["Silent Algorithm", "Drama", 2020, 1, 1, 6, 3],
  ["Paper Planets", "Comedy", 2022, 1, 6, 6, 6],
  ["The Long Winter", "Drama", 1999, 1, 5, 4, 3],
  ["Neon Rain", "Sci-Fi", 1994, 5, 3, 6, 3],
  ["Echoes of Bergen", "Horror", 1996, 3, 6, 6, 6],
  ["Cold Signal", "Action", 1991, 5, 2, 6, 1],
  ["The Glass Garden", "Horror", 1998, 3, 5, 1, 4],
  ["Storm Line", "Sci-Fi", 2022, 2, 5, 3, 1],
  ["Quiet Engines", "Comedy", 2000, 2, 6, 3, 4],
  ["Northern Static", "Sci-Fi", 2006, 2, 3, 2, 3],
  ["The Ninth Door", "Horror", 2011, 5, 4, 4, 3],
  ["Salt and Smoke", "Sci-Fi", 1987, 2, 5, 6, 4],
  ["Iron Valley", "Action", 2007, 3, 6, 2, 2],
  ["Lost Frequencies", "Drama", 2002, 3, 2, 1, 3],
  ["The Copper Key", "Horror", 2013, 3, 6, 5, "-"],
  ["Hollow Sun", "Sci-Fi", 2007, 5, 3, 3, 1],
  ["Blue Hour", "Comedy", 2003, 4, 1, 6, 6],
  ["Fast Lane Kids", "Sci-Fi", 1990, 5, 2, 6, 5],
  ["The Orchard", "Action", 1993, 1, 5, 2, 1],
  ["Deep Archive", "Action", 2009, 1, 4, 2, 5],
  ["Wild Current", "Comedy", 1999, 1, "-", 3, 6],
  ["Night Ferry", "Comedy", 2001, 3, "-", 4, 1],
  ["Small Giants", "Horror", 2008, 6, 4, 4, 4],
  ["The Lighthouse Club", "Horror", 1988, 2, 5, 6, 6],
  ["Velvet Circuit", "Sci-Fi", 2010, 3, 3, 6, 1],
  ["Frozen Lake Diaries", "Comedy", 1989, 6, 2, 5, 3],
  ["Borrowed Time", "Action", 2023, 1, 3, "-", 6],
  ["The Map Maker", "Comedy", 2019, 3, 5, "-", 2],
  ["Golden Static", "Comedy", 2024, 6, 4, 2, 5],
  ["Steel Birds", "Horror", 2008, 3, 3, 3, 3],
  ["Second Summer", "Sci-Fi", 2015, 3, 3, 2, 4],
  ["The Hidden Floor", "Drama", 2006, 2, 3, 5, 4],
  ["Pixel Hearts", "Drama", 1998, 4, 5, 4, 5],
  ["Last Train North", "Drama", 2018, 3, 2, 2, 4],
  ["The Quiet Coast", "Action", 1995, 5, 1, 5, 5],
  ["Double Shift", "Horror", 2006, 1, 6, 1, 6],
  ["Starfall Avenue", "Comedy", 1997, 4, 3, 5, "-"],
]

movies_dict = [
  {"Title": "The Last Fjord", "Genre": "Action", "Year": 1994, "Critic 1": 6, "Critic 2": 1, "Critic 3": 2, "Critic 4": 5},
  {"Title": "Midnight Code", "Genre": "Drama", "Year": 2008, "Critic 1": 6, "Critic 2": 1, "Critic 3": 4, "Critic 4": 6},
  {"Title": "Red Harbour", "Genre": "Drama", "Year": 1990, "Critic 1": 1, "Critic 2": 1, "Critic 3": 2, "Critic 4": 1},
  {"Title": "Silent Algorithm", "Genre": "Drama", "Year": 2020, "Critic 1": 1, "Critic 2": 1, "Critic 3": 6, "Critic 4": 3},
  {"Title": "Paper Planets", "Genre": "Comedy", "Year": 2022, "Critic 1": 1, "Critic 2": 6, "Critic 3": 6, "Critic 4": 6},
  {"Title": "The Long Winter", "Genre": "Drama", "Year": 1999, "Critic 1": 1, "Critic 2": 5, "Critic 3": 4, "Critic 4": 3},
  {"Title": "Neon Rain", "Genre": "Sci-Fi", "Year": 1994, "Critic 1": 5, "Critic 2": 3, "Critic 3": 6, "Critic 4": 3},
  {"Title": "Echoes of Bergen", "Genre": "Horror", "Year": 1996, "Critic 1": 3, "Critic 2": 6, "Critic 3": 6, "Critic 4": 6},
  {"Title": "Cold Signal", "Genre": "Action", "Year": 1991, "Critic 1": 5, "Critic 2": 2, "Critic 3": 6, "Critic 4": 1},
  {"Title": "The Glass Garden", "Genre": "Horror", "Year": 1998, "Critic 1": 3, "Critic 2": 5, "Critic 3": 1, "Critic 4": 4},
  {"Title": "Storm Line", "Genre": "Sci-Fi", "Year": 2022, "Critic 1": 2, "Critic 2": 5, "Critic 3": 3, "Critic 4": 1},
  {"Title": "Quiet Engines", "Genre": "Comedy", "Year": 2000, "Critic 1": 2, "Critic 2": 6, "Critic 3": 3, "Critic 4": 4},
  {"Title": "Northern Static", "Genre": "Sci-Fi", "Year": 2006, "Critic 1": 2, "Critic 2": 3, "Critic 3": 2, "Critic 4": 3},
  {"Title": "The Ninth Door", "Genre": "Horror", "Year": 2011, "Critic 1": 5, "Critic 2": 4, "Critic 3": 4, "Critic 4": 3},
  {"Title": "Salt and Smoke", "Genre": "Sci-Fi", "Year": 1987, "Critic 1": 2, "Critic 2": 5, "Critic 3": 6, "Critic 4": 4},
  {"Title": "Iron Valley", "Genre": "Action", "Year": 2007, "Critic 1": 3, "Critic 2": 6, "Critic 3": 2, "Critic 4": 2},
  {"Title": "Lost Frequencies", "Genre": "Drama", "Year": 2002, "Critic 1": 3, "Critic 2": 2, "Critic 3": 1, "Critic 4": 3},
  {"Title": "The Copper Key", "Genre": "Horror", "Year": 2013, "Critic 1": 3, "Critic 2": 6, "Critic 3": 5, "Critic 4": "-"},
  {"Title": "Hollow Sun", "Genre": "Sci-Fi", "Year": 2007, "Critic 1": 5, "Critic 2": 3, "Critic 3": 3, "Critic 4": 1},
  {"Title": "Blue Hour", "Genre": "Comedy", "Year": 2003, "Critic 1": 4, "Critic 2": 1, "Critic 3": 6, "Critic 4": 6},
  {"Title": "Fast Lane Kids", "Genre": "Sci-Fi", "Year": 1990, "Critic 1": 5, "Critic 2": 2, "Critic 3": 6, "Critic 4": 5},
  {"Title": "The Orchard", "Genre": "Action", "Year": 1993, "Critic 1": 1, "Critic 2": 5, "Critic 3": 2, "Critic 4": 1},
  {"Title": "Deep Archive", "Genre": "Action", "Year": 2009, "Critic 1": 1, "Critic 2": 4, "Critic 3": 2, "Critic 4": 5},
  {"Title": "Wild Current", "Genre": "Comedy", "Year": 1999, "Critic 1": 1, "Critic 2": "-", "Critic 3": 3, "Critic 4": 6},
  {"Title": "Night Ferry", "Genre": "Comedy", "Year": 2001, "Critic 1": 3, "Critic 2": "-", "Critic 3": 4, "Critic 4": 1},
  {"Title": "Small Giants", "Genre": "Horror", "Year": 2008, "Critic 1": 6, "Critic 2": 4, "Critic 3": 4, "Critic 4": 4},
  {"Title": "The Lighthouse Club", "Genre": "Horror", "Year": 1988, "Critic 1": 2, "Critic 2": 5, "Critic 3": 6, "Critic 4": 6},
  {"Title": "Velvet Circuit", "Genre": "Sci-Fi", "Year": 2010, "Critic 1": 3, "Critic 2": 3, "Critic 3": 6, "Critic 4": 1},
  {"Title": "Frozen Lake Diaries", "Genre": "Comedy", "Year": 1989, "Critic 1": 6, "Critic 2": 2, "Critic 3": 5, "Critic 4": 3},
  {"Title": "Borrowed Time", "Genre": "Action", "Year": 2023, "Critic 1": 1, "Critic 2": 3, "Critic 3": "-", "Critic 4": 6},
  {"Title": "The Map Maker", "Genre": "Comedy", "Year": 2019, "Critic 1": 3, "Critic 2": 5, "Critic 3": "-", "Critic 4": 2},
  {"Title": "Golden Static", "Genre": "Comedy", "Year": 2024, "Critic 1": 6, "Critic 2": 4, "Critic 3": 2, "Critic 4": 5},
  {"Title": "Steel Birds", "Genre": "Horror", "Year": 2008, "Critic 1": 3, "Critic 2": 3, "Critic 3": 3, "Critic 4": 3},
  {"Title": "Second Summer", "Genre": "Sci-Fi", "Year": 2015, "Critic 1": 3, "Critic 2": 3, "Critic 3": 2, "Critic 4": 4},
  {"Title": "The Hidden Floor", "Genre": "Drama", "Year": 2006, "Critic 1": 2, "Critic 2": 3, "Critic 3": 5, "Critic 4": 4},
  {"Title": "Pixel Hearts", "Genre": "Drama", "Year": 1998, "Critic 1": 4, "Critic 2": 5, "Critic 3": 4, "Critic 4": 5},
  {"Title": "Last Train North", "Genre": "Drama", "Year": 2018, "Critic 1": 3, "Critic 2": 2, "Critic 3": 2, "Critic 4": 4},
  {"Title": "The Quiet Coast", "Genre": "Action", "Year": 1995, "Critic 1": 5, "Critic 2": 1, "Critic 3": 5, "Critic 4": 5},
  {"Title": "Double Shift", "Genre": "Horror", "Year": 2006, "Critic 1": 1, "Critic 2": 6, "Critic 3": 1, "Critic 4": 6},
  {"Title": "Starfall Avenue", "Genre": "Comedy", "Year": 1997, "Critic 1": 4, "Critic 2": 3, "Critic 3": 5, "Critic 4": "-"},
]


# Write your code below (movies_list version)



# Write your code below (movies_dict version)
