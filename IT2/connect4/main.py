WIDTH = 7
HEIGHT = 6

board = []

def create_board():
  for x in range(WIDTH):
    column = []

    for y in range(HEIGHT):
      column.append(" ")

    board.append(column)

def print_board():
  print()

  for y in range(HEIGHT):
    print("|", end="")
    for x in range(WIDTH):
      print(board[x][y] + "|", end="")
    print()

  print("---------------")
  print("|1|2|3|4|5|6|7|")



def ask_player():
  while True:
    try:
      move = int(input(f"Player {player_piece[player]} (1 - 7): "))
      if move == 0:
        print("Bye!")
        return move
      if move in legal_moves:
        #print("OK")
        return move
      else:
        print("Try again")
    except ValueError:
      print("Try again")

def place_piece():
  x = move - 1
  column = board[x]

  for y in range(HEIGHT - 1, -1, -1):
    if column[y] == " ":
      column[y] = player_piece[player]
      print(f"Placing a piece on X: {x}, Y: {y}")
      return y

  print("Column full")
  return None

def check_vertical(x, y, player):
  print(x, y, player)
  print(board)

  if board[x][y] != player_piece[player]:
    print(f"Did not find: {x}, {y}")

  if board[x][y] == str(player_piece[player]):
    print(f"Board coordinates: {x}, {y}")

def swap_player(current_player):
  new_player = swap[current_player]
  return new_player

create_board()
print_board()

"""
Gameloop
----------------------------------------------------------
1. Ask the player for a number (1 - 7) V
2. Get the piece belonig to the player to the correct row V
3. Get the piece to the correct collumn V
4. Check for 4 in a row:
  Vertical
  Horizontal
  Diagonal right
  Diagonal left
5. Swap player V
6. Loop V
----------------------------------------------------------
"""

player_piece = {
  0: "X",
  1: "O"
}
swap = {0: 1, 1:0}
player = 0
move = None
legal_moves = [1, 2, 3, 4, 5, 6, 7]


while True:

  #  Asking the player for a number
  move = ask_player()
  if move == 0:
    break
  # Done asking the player
  placed_row = place_piece() 
  if placed_row == None:
    continue
  else:


    check_vertical(move - 1, placed_row, player)

    print_board()

    player = swap_player(player)