"""Solution to exercise 03 - try it yourself first!"""

players = [
  ["Heggebø", "Brann", "Striker", 12],
  ["Myhre", "Brann", "Midfielder", 3],
  ["Dyngeland", "Brann", "Goalkeeper", 0],
  ["Finne", "Brann", "Winger", 7],
  ["Tagseth", "Rosenborg", "Midfielder", 4],
  ["Sæter", "Rosenborg", "Striker", 9],
  ["Tengstedt", "Rosenborg", "Winger", 6],
  ["Tangen", "Rosenborg", "Defender", 1],
  ["Berg", "Bodø/Glimt", "Midfielder", 5],
  ["Hauge", "Bodø/Glimt", "Winger", 8],
  ["Høgh", "Bodø/Glimt", "Striker", 14],
  ["Bjørtuft", "Bodø/Glimt", "Defender", 2],
  ["Haikin", "Bodø/Glimt", "Goalkeeper", 0],
  ["Ruud", "Molde", "Striker", 10],
  ["Eriksen", "Molde", "Midfielder", 6],
  ["Haugen", "Molde", "Defender", 1],
]

# a) unique teams
teams = []
for player in players:
  if player[1] not in teams:
    teams.append(player[1])

print("a)", teams)

# b) total goals per team
totals = {}
for player in players:
  team = player[1]
  if team not in totals:
    totals[team] = 0
  totals[team] += player[3]

print("b)", totals)
print("b)", sorted(totals, key=totals.get, reverse=True))

# c) dict of lists, team -> goals of each player
team_goals = {}
for player in players:
  team = player[1]
  if team not in team_goals:
    team_goals[team] = []
  team_goals[team].append(player[3])

print("c)", team_goals)

# d) average goals per player for each team
team_avg = {}
for team, goals in team_goals.items():
  team_avg[team] = round(sum(goals) / len(goals), 2)

print("d)", team_avg)
print("d)", sorted(team_avg, key=team_avg.get, reverse=True))

# e) same thing, grouped by position
position_goals = {}
for player in players:
  position = player[2]
  if position not in position_goals:
    position_goals[position] = []
  position_goals[position].append(player[3])

position_avg = {}
for position, goals in position_goals.items():
  position_avg[position] = round(sum(goals) / len(goals), 2)

position_sorted = sorted(position_avg, key=position_avg.get, reverse=True)
print("e)", position_avg)
print("e) best position:", position_sorted[0])

# f) top scorer on each team
best = {}
for player in players:
  team = player[1]
  if team not in best or player[3] > best[team][3]:
    best[team] = player

top_scorers = {}
for team, player in best.items():
  top_scorers[team] = player[0]

print("f)", top_scorers)
