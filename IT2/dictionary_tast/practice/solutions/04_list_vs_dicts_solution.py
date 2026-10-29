"""Solution to exercise 04 - try it yourself first!"""

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


print("----- scores_list -----")

# a) games sorted by average score
game_avg = {}
for n in range(2, 6):
  scores = []
  for player in scores_list:
    if player[n] != "N/A":
      scores.append(player[n])
  game_avg[headers[n]] = round(sum(scores) / len(scores), 1)

print("a)", game_avg)
print("a)", sorted(game_avg, key=game_avg.get, reverse=True))

# b) teams sorted by average in Game 4
team_scores = {}
for player in scores_list:
  team = player[1]
  if team not in team_scores:
    team_scores[team] = []
  if player[5] != "N/A":
    team_scores[team].append(player[5])

team_avg = {}
for team, scores in team_scores.items():
  team_avg[team] = round(sum(scores) / len(scores), 1)

print("b)", team_avg)
print("b)", sorted(team_avg, key=team_avg.get, reverse=True))

# c) games played per player
games_played = {}
for player in scores_list:
  count = 0
  for n in range(2, 6):
    if player[n] != "N/A":
      count += 1
  games_played[player[0]] = count

played_all = []
for name, count in games_played.items():
  if count == 4:
    played_all.append(name)

print("c)", games_played)
print("c)", played_all)

# d) best average per player
player_avg = {}
for player in scores_list:
  scores = []
  for n in range(2, 6):
    if player[n] != "N/A":
      scores.append(player[n])
  player_avg[player[0]] = round(sum(scores) / len(scores), 1)

print("d)", sorted(player_avg, key=player_avg.get, reverse=True)[0])


print("----- scores_dict -----")

games = headers[2:]

# a)
game_avg = {}
for game in games:
  scores = []
  for player in scores_dict:
    if player[game] != "N/A":
      scores.append(player[game])
  game_avg[game] = round(sum(scores) / len(scores), 1)

print("a)", sorted(game_avg, key=game_avg.get, reverse=True))

# b)
team_scores = {}
for player in scores_dict:
  team = player["Team"]
  if team not in team_scores:
    team_scores[team] = []
  if player["Game 4"] != "N/A":
    team_scores[team].append(player["Game 4"])

team_avg = {}
for team, scores in team_scores.items():
  team_avg[team] = round(sum(scores) / len(scores), 1)

print("b)", sorted(team_avg, key=team_avg.get, reverse=True))

# c)
games_played = {}
for player in scores_dict:
  count = 0
  for game in games:
    if player[game] != "N/A":
      count += 1
  games_played[player["Player"]] = count

played_all = []
for name, count in games_played.items():
  if count == 4:
    played_all.append(name)

print("c)", played_all)

# d)
player_avg = {}
for player in scores_dict:
  scores = []
  for game in games:
    if player[game] != "N/A":
      scores.append(player[game])
  player_avg[player["Player"]] = round(sum(scores) / len(scores), 1)

print("d)", sorted(player_avg, key=player_avg.get, reverse=True)[0])
