"""
Exercise 05 - Changing the data structure, and top-N lists

Each row is one quiz contestant:  [name, school, round1, round2, round3, round4]
Scores are 0-10. "ABS" means the contestant was absent that round.

Useful tools:
  row[2:]                          -> everything from index 2 to the end (a new list)
  new_list.append([a, b, c])       -> build a new row
  {"Name": ..., "Rounds": [...]}   -> build a new dict
  if value != "ABS":               -> skip absent rounds
  sorted(d, key=d.get, reverse=True)[:5]       -> top 5 keys
  sorted(d.items(), key=lambda p: p[1])        -> (key, value) pairs sorted by value
  for place, name in enumerate(my_list, 1):    -> gives 1, 2, 3... together with each element

a) Make a new variable `contestants_list2` with the same content as `contestants`, but where
   the four scores are in ONE list:
     ["Hanna", "Nordahl Grieg", [8, 7, 9, 6]]
   Print the first contestant to show the new structure.
   (This is the same as task c in elev_test.py.)
   Hint: row[2:] slices out the scores. Append [row[0], row[1], row[2:]].

b) Make `contestants_dicts`, a list of dicts with this structure, and print the first one:
     {"Name": "Hanna", "School": "Nordahl Grieg", "Rounds": [8, 7, 9, 6]}
   Hint: same loop as a), but append a dict instead of a list.

c) Use `contestants_dicts` to make a dict with each contestant's average score:
     {"Hanna": 7.5, ...}
   Only count the rounds they were present for.
   Hint: loop over contestant["Rounds"] and skip "ABS". Then sum() / len().

d) Print the top 5 contestants like this:
     1. <name> - <average>
     2. ...
   (This is the same as task d in elev_test.py.)
   Hint: sorted(..., key=..., reverse=True)[:5], then enumerate(top5, 1) for the place.

e) Print the 3 contestants with the LOWEST average, as (name, average) pairs.
   Hint: sorted(averages.items(), key=lambda p: p[1]) and slice [:3].

f) Make a list of only the contestants who were present in every round, sorted by
   their TOTAL score (highest first).
   Hint: "ABS" not in contestant["Rounds"]. Then sum() for the total.
"""

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


# Write your code below
