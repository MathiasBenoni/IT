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

def make_move(board, player, player_piece):
  local_board = [column.copy() for column in board]

  # 1. Can I win?
  for move in range(1, 8):
    if wins_with(local_board, move, player, player_piece):
      return move

  # 2. Can the opponent win? Block it.
  for move in range(1, 8):
    if wins_with(local_board, move, swap[player], player_piece):
      return move

  # 3. Otherwise pick a random column that isn't full
  legal = [move for move in range(1, 8) if find_y(local_board, find_x(move)) is not None]
  return random.choice(legal)
