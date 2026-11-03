"""
Exercise 02 - Columns vs. rows, and skipping invalid values

The data is a list of lists. Each row is one runner:
  [name, club, lap1, lap2, lap3]     (lap times in seconds)
"DNF" means "Did Not Finish" that lap. It is NOT a number, so it must be skipped.

ROW    = one runner, going across:   results[0]       -> ["Emma", "Bergen IL", 72, 75, 71]
COLUMN = one lap, going down:        results[i][2]    -> lap 1 for every runner i

Useful tools:
  for runner in results:         -> loop over rows
  for n in range(2, 5):          -> loop over the lap columns (index 2, 3, 4)
  if value != "DNF":             -> skip invalid values (simpler than try/except)
  my_list.append(x)              -> collect valid values in a list
  sum(my_list) / len(my_list)    -> average of only the values you collected
  round(x, 1)                    -> round to 1 decimal
  sorted(d, key=d.get)           -> dict keys sorted by their values

a) Find the average time for lap 1 (a COLUMN), skipping "DNF".
   Hint: loop over every runner, look at runner[2], and append it to a list if it is
         not "DNF". Then use sum(list) / len(list). Do NOT divide by len(results),
         because some runners have no time for that lap.

b) Make a dict with the average time for each lap:  {"Lap 1": 73.4, "Lap 2": ...}
   Then print the lap names sorted from fastest average to slowest.
   Hint: put the code from a) inside  for n in range(2, 5):  and use
         headers[n] as the dict key. Then use sorted(lap_avg, key=lap_avg.get).

c) Find each runner's average lap time (a ROW), over the laps they actually completed.
   Store it in a dict:  {"Emma": 72.7, ...}
   Hint: for each runner, loop over range(2, 5) and collect the valid times in a list.
         Divide by len() of THAT list, not by 3.

d) Make a list of the runners that finished all three laps.
   Hint: "DNF" not in runner[2:]  is True when there are no "DNF"s in the lap times.

e) For the runners from d), find the total time (sum of the three laps).
   Print the names of the top 3 fastest runners (lowest total).
   Hint: build a dict {name: total}, sort it with key=totals.get, then use [:3].
"""

headers = ["Name", "Club", "Lap 1", "Lap 2", "Lap 3"]

results = [
  ["Emma", "Bergen IL", 72, 75, 71],
  ["Lars", "Tjalve", 70, "DNF", "DNF"],
  ["Nora", "Tjalve", 78, 76, 74],
  ["Isak", "Bergen IL", 69, 71, 73],
  ["Maja", "Gular", 81, 79, 80],
  ["Henrik", "Gular", 74, 74, "DNF"],
  ["Ingrid", "Bergen IL", 71, 70, 70],
  ["Elias", "Tjalve", "DNF", 77, 75],
  ["Sara", "Gular", 76, 78, 77],
  ["Filip", "Tjalve", 73, 72, 72],
]


# Write your code below
