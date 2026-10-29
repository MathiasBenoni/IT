"""Solution to exercise 05 - try it yourself first!"""

headers = ["Name", "School", "Round 1", "Round 2", "Round 3", "Round 4"]

contestants = [
  ["Hanna", "Nordahl Grieg", 8, 7, 9, 6],
  ["Leon", "Amalie Skram", 9, 10, 8, 9],
  ["Vilde", "Nordahl Grieg", 5, "ABS", 6, 7],
  ["Mathias", "Bergen Katedral", 7, 8, 7, 8],
  ["Selma", "Amalie Skram", 10, 9, "ABS", 9],
  ["Tobias", "Bergen Katedral", 4, 5, 3, 6],
  ["Live", "Nordahl Grieg", 6, 6, 7, 5],
  ["Kasper", "Amalie Skram", "ABS", "ABS", 8, 7],
  ["Julie", "Bergen Katedral", 9, 8, 9, 10],
  ["Adrian", "Nordahl Grieg", 3, 4, 5, 4],
  ["Frida", "Amalie Skram", 7, 7, 8, "ABS"],
  ["Sander", "Bergen Katedral", 8, 9, 6, 7],
]

# a) scores as one list inside each row
contestants_list2 = []
for row in contestants:
  contestants_list2.append([row[0], row[1], row[2:]])

print("a)", contestants_list2[0])

# b) list of dicts
contestants_dicts = []
for row in contestants:
  contestants_dicts.append({"Name": row[0], "School": row[1], "Rounds": row[2:]})

print("b)", contestants_dicts[0])

# c) average per contestant, skipping ABS
averages = {}
for contestant in contestants_dicts:
  scores = []
  for score in contestant["Rounds"]:
    if score != "ABS":
      scores.append(score)
  averages[contestant["Name"]] = round(sum(scores) / len(scores), 2)

print("c)", averages)

# d) top 5
top5 = sorted(averages, key=averages.get, reverse=True)[:5]
print("d)")
for place, name in enumerate(top5, 1):
  print(f"  {place}. {name} - {averages[name]}")

# e) lowest 3 as (name, average) pairs
lowest = sorted(averages.items(), key=lambda p: p[1])[:3]
print("e)", lowest)

# f) present every round, sorted by total
totals = {}
for contestant in contestants_dicts:
  if "ABS" not in contestant["Rounds"]:
    totals[contestant["Name"]] = sum(contestant["Rounds"])

print("f)", sorted(totals, key=totals.get, reverse=True))
