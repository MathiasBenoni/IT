"""
Exercise 03 - Grouping ("group by")

This is the pattern for questions like "average PER class" or "total PER team".
You build a dict where each key is a group, and each value is a LIST of numbers:

  {"Brann": [12, 3, 0, 7], "Rosenborg": [9, 1, 4], ...}

Then you average or sum each list, and sort the groups.

Each row is one player:  [name, team, position, goals]

Useful tools:
  if key not in d:  d[key] = []      -> create an empty list for a new group
  d[key].append(value)               -> add a value to that group's list
  for key in d:                      -> loop over the groups
  for key, values in d.items():      -> loop over groups AND their lists
  sum(values) / len(values)          -> average of one group
  sorted(d, key=d.get, reverse=True) -> group names sorted by their value

a) Make a list of all the teams. Each team should appear only once.
   Hint: loop over the players and append player[1] if it is  not in  the list already.

b) Make a dict with the total number of goals per team:  {"Brann": 22, ...}
   Print the team names sorted from most goals to fewest.
   Hint: if team not in totals: totals[team] = 0  ... then  totals[team] += goals

c) Make a dict of lists with the goals of every player on each team:
     {"Brann": [12, 3, 0, 7], ...}
   Hint: if team not in team_goals: team_goals[team] = []
         then  team_goals[team].append(player[3])

d) Use the dict from c) to make a new dict with the AVERAGE goals per player for each team.
   Print the teams sorted from highest average to lowest.
   Hint: for team, goals in team_goals.items():  ->  avg[team] = sum(goals) / len(goals)
         Then sorted(avg, key=avg.get, reverse=True).

e) Do the same as c) and d), but group by POSITION instead of team.
   Which position scores the most goals on average?
   Hint: it's the same code, just use player[2] as the key instead of player[1].

f) Find the top scorer on each team:  {"Brann": "Heggebø", ...}
   Hint: keep a dict team -> best player row so far. For each player:
         if the team is not in the dict yet, OR the player has more goals than
         the stored one, replace it.
"""

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


# Write your code below
