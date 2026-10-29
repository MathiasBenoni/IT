"""Solution to exercise 01 - try it yourself first!"""

numbers = [42, 7, 19, 3, 88, 51, 7, 26]

words = ["banana", "kiwi", "apple", "fig", "watermelon", "plum"]

prices = {
  "apple": 8,
  "banana": 5,
  "mango": 25,
  "kiwi": 6,
  "pineapple": 30,
  "grape": 18,
  "lemon": 7,
}

people = [
  ["Ola", 17],
  ["Kari", 19],
  ["Ahmed", 16],
  ["Sofie", 18],
  ["Jonas", 20],
]

# a) lowest to highest
print("a)", sorted(numbers))

# b) highest to lowest
print("b)", sorted(numbers, reverse=True))

# c) shortest word first
print("c)", sorted(words, key=len))

# d) fruit names, cheapest first
# sorting a dict gives the keys, key=prices.get compares them by price
cheapest_first = sorted(prices, key=prices.get)
print("d)", cheapest_first)

# e) three most expensive
most_expensive = sorted(prices, key=prices.get, reverse=True)
print("e)", most_expensive[:3])

# f) (fruit, price) pairs, most expensive first
pairs = sorted(prices.items(), key=lambda pair: pair[1], reverse=True)
print("f)", pairs)

# g) people by age, then by name
print("g) by age: ", sorted(people, key=lambda p: p[1]))
print("g) by name:", sorted(people, key=lambda p: p[0]))
