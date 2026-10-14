import copy
import my_functions
import check_win

import random

swap = {0: 1, 1: 0}

def find_x(move):
  # column number from the player (1 - 7) -> index in board (0 - 6)
  return move - 1

def find_y(board, x):
  # lowest empty row in column x (bottom is the highest y), or None if full
  for y in range(len(board[x]) - 1, -1, -1):
    if board[x][y] == " ":
      return y
  return None

def wins_with(local_board, move, player, player_piece):
  # place the piece, check for a win, then take it back
  x = find_x(move)
  y = find_y(local_board, x)
  if y is None:
    return False  # column full

  local_board[x][y] = player_piece[player]
  wins = check_win.check_win(x, y, player_piece, player, local_board)
  local_board[x][y] = " "
  return wins

def bot_1(board, player, player_piece):
  local_board = copy.deepcopy(board)
  # 1. Can I win?
  for move in range(1, 8):
    if wins_with(local_board, move, player, player_piece):
      return move

  # 2. Can the opponent win? Block it.
  for move in range(1, 8):
    if wins_with(local_board, move, swap[player], player_piece):
      return move

  return None
  
def bot_2(board, player, player_piece):
  possible_moves = []

  for move in range(1, 8):
    local_board = copy.deepcopy(board)
    x = find_x(move)

    if find_y(local_board, x) is None:
      continue # Column is full

    my_functions.place_piece(move, local_board, player_piece, player)

    if find_y(local_board, x) is None:
      possible_moves.append(move) # my piece fills the column, enemy can't go on top
      continue

    enemy_y = my_functions.place_piece(move, local_board, player_piece, swap[player])

    enemy_wins = check_win.check_win(x, enemy_y, player_piece, swap[player], local_board)

    local_board[x][enemy_y] = player_piece[player] # swap the enemy piece for mine
    # no vertical check here
    i_would_win = (check_win.check_horizontal(x, enemy_y, player_piece, player, local_board)
                or check_win.check_diagonal_left(x, enemy_y, player_piece, player, local_board)
                or check_win.check_diagonal_right(x, enemy_y, player_piece, player, local_board))

    if enemy_wins or i_would_win:
      print(f"You win, if I were to place on column {move} or I destroy a chance for me to win")
      continue
    else:
      possible_moves.append(move)

  # print(possible_moves)
  if not possible_moves:
    return None
  
  return random.choice(possible_moves)

def make_move(board, player, player_piece):
  local_board = copy.deepcopy(board)

  possible_move = bot_1(local_board, player, player_piece)

  if possible_move != None:
    print(f"Bot 1 found a win or block in column {possible_move}")
    return possible_move

  else:
    # print("Bot 1 did not find any good move")
    possible_move = bot_2(local_board, player, player_piece)

    if possible_move != None:
      return possible_move

    else:
      # print("Bot 2 did not find any good move")
      possible_move = random.randint(1, 7)

      return possible_move