import random
import check_win

swap = {0: 1, 1: 0}

def drop_row(board, x):
  # lowest empty row in column x, or None if full
  for y in range(len(board[x]) - 1, -1, -1):
    if board[x][y] == " ":
      return y
  return None

def find_winning_column(board, player, player_piece):
  for x in range(len(board)):
    y = drop_row(board, x)
    if y is None:
      continue

    board[x][y] = player_piece[player]  # try the move
    wins = check_win.check_win(x, y, player_piece, player, board)
    board[x][y] = " "  # undo the move

    if wins:
      return x + 1  # columns are 1 - 7 in main.py
  return None

def make_move(board, player, player_piece):
  # 1. Can I win right now?
  move = find_winning_column(board, player, player_piece)
  if move is not None:
    return move

  # 2. Can the opponent win next turn? Block it.
  move = find_winning_column(board, swap[player], player_piece)
  if move is not None:
    return move

  # 3. Otherwise pick a random column that isn't full
  legal = [x + 1 for x in range(len(board)) if drop_row(board, x) is not None]
  return random.choice(legal)
