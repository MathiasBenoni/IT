from pandas import col


swap = {0: 1, 1:0}

def create_board(width, height):
  board = []
  for x in range(width):
    column = []

    for y in range(height):
      column.append(" ")

    board.append(column)
  return board

def print_board(width, height, board):
  print()

  for y in range(height):
    print("|", end="")
    for x in range(width):
      print(board[x][y] + "|", end="")
    print()

  print("---------------")
  print("|1|2|3|4|5|6|7|")
  print()

def ask_player(player, player_piece, legal_moves):
  while True:
    try:
      move = int(input(f"Player {player_piece[player]} (1 - 7): "))
      if move == 0:
        print("Bye!")
        return move
      if move in legal_moves:
        return move
      else:
        print("Try again")
    except ValueError:
      print("Try again")

def place_piece(move, board, player_piece, player, colors, backgrounds):
  x = move - 1
  column = board[x]

  for y in range(len(column) - 1, -1, -1):
    if column[y] == " ":
      column[y] = colors[player] + backgrounds[player] + str(player_piece[player]) + colors["White"] + backgrounds["No"]
      return y

  print("Column full")
  return None

def swap_player(current_player):
  new_player = swap[current_player]
  return new_player