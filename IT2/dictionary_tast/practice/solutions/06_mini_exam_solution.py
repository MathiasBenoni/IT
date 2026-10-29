"""Solution to exercise 06 - try it yourself first!"""

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



print("----- movies_list -----")

# a) critics sorted by average rating given
critic_avg = {}
for n in range(3, 7):
  ratings = []
  for movie in movies_list:
    if movie[n] != "-":
      ratings.append(movie[n])
  critic_avg[headers[n]] = round(sum(ratings) / len(ratings), 2)

print("a)", critic_avg)
print("a)", sorted(critic_avg, key=critic_avg.get, reverse=True))

# b) genres sorted by average of all ratings
genre_ratings = {}
for movie in movies_list:
  genre = movie[1]
  if genre not in genre_ratings:
    genre_ratings[genre] = []
  for rating in movie[3:]:
    if rating != "-":
      genre_ratings[genre].append(rating)

genre_avg = {}
for genre, ratings in genre_ratings.items():
  genre_avg[genre] = round(sum(ratings) / len(ratings), 2)

print("b)", genre_avg)
print("b)", sorted(genre_avg, key=genre_avg.get, reverse=True))

# c) ratings as one list
movies_list2 = []
for movie in movies_list:
  movies_list2.append([movie[0], movie[1], movie[2], movie[3:]])

print("c)", movies_list2[0])

# d) top 10 movies
movie_avg = {}
for movie in movies_list:
  ratings = []
  for rating in movie[3:]:
    if rating != "-":
      ratings.append(rating)
  movie_avg[movie[0]] = round(sum(ratings) / len(ratings), 2)

top10 = sorted(movie_avg, key=movie_avg.get, reverse=True)[:10]
print("d)")
for place, title in enumerate(top10, 1):
  print(f"  {place}. {title} - {movie_avg[title]}")

# e) movies per decade
decades = {}
for movie in movies_list:
  decade = movie[2] // 10 * 10
  if decade not in decades:
    decades[decade] = 0
  decades[decade] += 1

print("e)")
for decade in sorted(decades):
  print(f"  {decade}s: {decades[decade]}")


print("----- movies_dict -----")

critics = headers[3:]

# a)
critic_avg = {}
for critic in critics:
  ratings = []
  for movie in movies_dict:
    if movie[critic] != "-":
      ratings.append(movie[critic])
  critic_avg[critic] = round(sum(ratings) / len(ratings), 2)

print("a)", sorted(critic_avg, key=critic_avg.get, reverse=True))

# b)
genre_ratings = {}
for movie in movies_dict:
  genre = movie["Genre"]
  if genre not in genre_ratings:
    genre_ratings[genre] = []
  for critic in critics:
    if movie[critic] != "-":
      genre_ratings[genre].append(movie[critic])

genre_avg = {}
for genre, ratings in genre_ratings.items():
  genre_avg[genre] = round(sum(ratings) / len(ratings), 2)

print("b)", sorted(genre_avg, key=genre_avg.get, reverse=True))

# c)
movies_dict2 = []
for movie in movies_dict:
  ratings = []
  for critic in critics:
    ratings.append(movie[critic])
  movies_dict2.append({"Title": movie["Title"], "Genre": movie["Genre"], "Year": movie["Year"], "Ratings": ratings})

print("c)", movies_dict2[0])

# d)
movie_avg = {}
for movie in movies_dict2:
  ratings = []
  for rating in movie["Ratings"]:
    if rating != "-":
      ratings.append(rating)
  movie_avg[movie["Title"]] = round(sum(ratings) / len(ratings), 2)

top10 = sorted(movie_avg, key=movie_avg.get, reverse=True)[:10]
print("d)")
for place, title in enumerate(top10, 1):
  print(f"  {place}. {title} - {movie_avg[title]}")

# e)
decades = {}
for movie in movies_dict:
  decade = movie["Year"] // 10 * 10
  if decade not in decades:
    decades[decade] = 0
  decades[decade] += 1

print("e)")
for decade in sorted(decades):
  print(f"  {decade}s: {decades[decade]}")
