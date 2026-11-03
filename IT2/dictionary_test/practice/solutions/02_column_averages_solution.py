"""Solution to exercise 02 - try it yourself first!"""

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

# a) average of lap 1 (a column)
lap1_times = []
for runner in results:
  if runner[2] != "DNF":
    lap1_times.append(runner[2])

print("a)", round(sum(lap1_times) / len(lap1_times), 1))

# b) average of every lap, fastest lap first
lap_avg = {}
for n in range(2, 5):
  times = []
  for runner in results:
    if runner[n] != "DNF":
      times.append(runner[n])
  lap_avg[headers[n]] = round(sum(times) / len(times), 1)

print("b)", lap_avg)
print("b)", sorted(lap_avg, key=lap_avg.get))

# c) each runner's average over completed laps (a row)
runner_avg = {}
for runner in results:
  times = []
  for n in range(2, 5):
    if runner[n] != "DNF":
      times.append(runner[n])
  runner_avg[runner[0]] = round(sum(times) / len(times), 1)

print("c)", runner_avg)

# d) runners that finished every lap
finished = []
finished_names = []
for runner in results:
  if "DNF" not in runner[2:]:
    finished.append(runner)
    finished_names.append(runner[0])

print("d)", finished_names)

# e) top 3 fastest total time
totals = {}
for runner in finished:
  totals[runner[0]] = sum(runner[2:])

print("e)", sorted(totals, key=totals.get)[:3])
