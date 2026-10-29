"""
Exercise 04 - Same data, two shapes

Solve every task TWICE: once with scores_list and once with scores_dict.
They contain exactly the same data. "N/A" means the player did not play that game.

scores_list:  a list of lists. You need headers to know what index 3 means.
                scores_list[0][3]        -> Game 1 score for the first player
scores_dict:  a list of dicts. You use the column name instead of an index.
                scores_dict[0]["Game 1"] -> the same value

Useful tools:
  range(2, 6)  /  headers[n]          -> the game columns in scores_list
  games = headers[2:]                 -> the game names, for looping over scores_dict
  if value != "N/A":                  -> skip missing games
  sum() / len()                       -> average
  if key not in d: d[key] = []        -> group by
  sorted(d, key=d.get, reverse=True)  -> sort keys by value

a) Make a list of the four games, sorted by the average score in each game (highest first).
   (This is the same as task a in elev_test.py.)
   Hint: loop over the columns, collect the valid scores going down, store the average
         per game in a dict, then sorted(...).

b) Make a list of the teams, sorted by the team's average score in Game 4 (highest first).
   (This is the same as task b in elev_test.py.)
   Hint: group by team (dict of lists) using only the Game 4 value.

c) Make a dict with how many games each player played:  {"Alex": 4, "Mia": 3, ...}
   Then make a list of the players who played all four games.
   Hint: count the values that are != "N/A".

d) Make a dict with each player's average score over the games they played,
   and print the name of the player with the highest average.
   Hint: divide by the number of games played, not by 4. Then sorted(...)[0].
"""

headers = ["Player", "Team", "Game 1", "Game 2", "Game 3", "Game 4"]

scores_list = [
  ["Alex", "Red", 120, 95, 110, 130],
  ["Mia", "Blue", 105, "N/A", 98, 115],
  ["Jonas", "Green", 88, 92, 101, 97],
  ["Sofie", "Red", 140, 128, "N/A", 135],
  ["Emil", "Blue", 76, 81, 90, "N/A"],
  ["Ella", "Green", 115, 119, 108, 122],
  ["Noah", "Red", "N/A", 102, 99, 104],
  ["Leah", "Blue", 132, 125, 138, 129],
  ["Oskar", "Green", 94, "N/A", "N/A", 89],
  ["Thea", "Red", 101, 108, 112, 117],
  ["William", "Blue", 89, 93, 87, 91],
  ["Ida", "Green", 125, 131, 119, "N/A"],
]

scores_dict = [
  {"Player": "Alex", "Team": "Red", "Game 1": 120, "Game 2": 95, "Game 3": 110, "Game 4": 130},
  {"Player": "Mia", "Team": "Blue", "Game 1": 105, "Game 2": "N/A", "Game 3": 98, "Game 4": 115},
  {"Player": "Jonas", "Team": "Green", "Game 1": 88, "Game 2": 92, "Game 3": 101, "Game 4": 97},
  {"Player": "Sofie", "Team": "Red", "Game 1": 140, "Game 2": 128, "Game 3": "N/A", "Game 4": 135},
  {"Player": "Emil", "Team": "Blue", "Game 1": 76, "Game 2": 81, "Game 3": 90, "Game 4": "N/A"},
  {"Player": "Ella", "Team": "Green", "Game 1": 115, "Game 2": 119, "Game 3": 108, "Game 4": 122},
  {"Player": "Noah", "Team": "Red", "Game 1": "N/A", "Game 2": 102, "Game 3": 99, "Game 4": 104},
  {"Player": "Leah", "Team": "Blue", "Game 1": 132, "Game 2": 125, "Game 3": 138, "Game 4": 129},
  {"Player": "Oskar", "Team": "Green", "Game 1": 94, "Game 2": "N/A", "Game 3": "N/A", "Game 4": 89},
  {"Player": "Thea", "Team": "Red", "Game 1": 101, "Game 2": 108, "Game 3": 112, "Game 4": 117},
  {"Player": "William", "Team": "Blue", "Game 1": 89, "Game 2": 93, "Game 3": 87, "Game 4": 91},
  {"Player": "Ida", "Team": "Green", "Game 1": 125, "Game 2": 131, "Game 3": 119, "Game 4": "N/A"},
]


# Write your code below (scores_list version)



# Write your code below (scores_dict version)
