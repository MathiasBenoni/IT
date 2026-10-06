WIDTH = 7
HEIGHT = 6

board = []

def create_board():
  for i in range(HEIGHT):
    
    row = []
    #print(i)
    for n in range(WIDTH):
      cell = "| " + str(n)
      #board.append("|")
      row.append(cell)
      #board.append("|")
      #print(n)
    print(row)
    board.append(row)

def print_board():
  print("±---------------------------±")
  for row in board:
    print(*row, "|")
    
  print("|---------------------------|")
  print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
  print("±---------------------------±")

def ask_move():
  try:
    move = int(input(f"Player {player_piece[player]} (1 - 7): "))
  except:
    print("Try again")
  else:
    if move > 0 and move < 8:
      print("OK")
      return move

  if move == 0:
    return False

create_board()
print_board()

"""
Gameloop
---------------------------------------------------------
1. Ask the player for a number (1 - 7)
2. Get the piece belonig to the player to the correct row
3. Get the piece to the correct collumn
4. Check for 4 in a row
5. Swap player
6. Loop
---------------------------------------------------------
"""

player_piece = {
  0: "X",
  1: "O"
}
swap_player = {0: 1, 1:0}

player = 0

while True:

  #  Asking the player for a number
  move = ask_move()

  if move == False:
    break
  # Done asking the player

  

  