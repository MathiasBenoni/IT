WIDTH = 7
HEIGHT = 6

board = []

def create_board():
  for i in range(HEIGHT):
    row = []

    for n in range(WIDTH):
      row.append(" ")

    board.append(row)

def print_board():
  print(" --------------------------- ")

  for row in board:
    print("|", end="")
    for n in row:
      print(" " + str(n) + " |", end="")
    print()

  print("|---------------------------|")
  print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
  print(" --------------------------- ")

def ask_player():
  while True:
    try:
      move = int(input(f"Player {player_piece[player]} (1 - 7): "))
      if move == 0:
        print("Bye!")
        return move
      if move in legal_moves:
        print("OK")
        return move
      else:
        print("Try again")
    except ValueError:
      print("Try again")

def place_piece():
  accual_move = move - 1
  print(accual_move)

  for row in reversed(board):
    if row[accual_move] == " ":
      row[accual_move] = player_piece[player]
      break

create_board()
print_board()

"""
Gameloop
---------------------------------------------------------
1. Ask the player for a number (1 - 7) V
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
move = None
legal_moves = [1, 2, 3, 4, 5, 6, 7]


while True:

  #  Asking the player for a number
  move = ask_player()
  if move == 0:
    break
  # Done asking the player

  place_piece()    



  print_board()

  break

  