"""
Exercise 01 - sorted() basics

Goal: never write your own sorting loop again. Python's sorted() does it for you.

Useful tools:
  sorted(something)                  -> returns a NEW sorted list
  sorted(something, reverse=True)    -> highest first
  sorted(something, key=...)         -> sort by something other than the value itself
  d.get                              -> a function that gives the value for a key
  lambda x: x[1]                     -> a tiny function, "give me item 1 of x"
  d.items()                          -> pairs of (key, value)
  my_list[:3]                        -> the first three elements

a) Sort the list `numbers` from lowest to highest, and print it.
   Hint: sorted(numbers). Note that sorted() does not change `numbers`, it returns a new list.

b) Sort `numbers` from highest to lowest.
   Hint: add reverse=True as an extra argument to sorted().

c) Sort the list `words` by length, shortest first.
   Hint: key=len tells sorted() to compare len(word) instead of the word itself.

d) Make a list of the fruit NAMES in `prices`, sorted from cheapest to most expensive.
   Hint: sorted(prices) on a dict sorts the KEYS. Add key=prices.get so the keys
         are compared by their values (the prices).

e) Make a list of the three most expensive fruits.
   Hint: sort with reverse=True, then slice with [:3].

f) Make a list of (fruit, price) pairs sorted by price, most expensive first.
   Example of one element: ("mango", 25)
   Hint: prices.items() gives (fruit, price) pairs. Use key=lambda pair: pair[1]
         to sort by the price (index 1 in each pair).

g) Sort `people` (a list of lists) by age, youngest first. Then sort it by name A-Z.
   Hint: each person is [name, age]. key=lambda p: p[1] sorts by age,
         key=lambda p: p[0] sorts by name.
"""

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


# Write your code below
