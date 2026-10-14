import copy
import random

import check_win
from bot_2 import find_x, find_y, wins_with, bot_1

swap = {0: 1, 1: 0} # player 0 <-> player 1

DEPTH = 4 # default: how many moves ahead the brute force looks (bot, enemy, bot, enemy)

def legal_moves(board):
  # columns (1 - 7) that are not full
  return [move for move in range(1, 8) if find_y(board, find_x(move)) is not None]

def count_wins(board, player, player_piece):
  # how many columns the player can win in right now
  count = 0
  for move in range(1, 8):
    if wins_with(board, move, player, player_piece):
      count += 1
  return count

def block_double_threat(board, player, player_piece):
  # can the enemy make a move that gives them two ways to win? Take that spot first.
  # Example: enemy has _ X X _ _ and plays the 4th spot -> _ X X X _
  # Now the enemy can win on both sides, and I can only block one of them.
  enemy = swap[player]

  for move in range(1, 8):
    x = find_x(move)
    y = find_y(board, x)
    if y is None:
      continue # Column is full

    local_board = copy.deepcopy(board) # practice board, the real one is not touched
    local_board[x][y] = player_piece[enemy] # what if the enemy plays here?
    if count_wins(local_board, enemy, player_piece) < 2:
      continue # only one (or zero) ways to win, bot_1 can handle that later

    local_board[x][y] = player_piece[player] # then I play here instead
    if wins_with(local_board, move, enemy, player_piece):
      continue # enemy would win on top of my piece

    return move

  return None

def score_move(board, move, player, current, player_piece, depth):
  # Plays move for current, and gives it a score seen from player's (the bot's) side.
  # Bigger score = better for the bot.
  #   100 + depth  -> the bot wins (a faster win has more depth left, so a bigger score)
  # -(100 + depth) -> the enemy wins
  #   0            -> nobody wins within the moves we look at
  # depth counts down by 1 for every move, the search stops at 1.
  x = find_x(move)
  y = find_y(board, x)
  board[x][y] = player_piece[current] # place the piece

  if check_win.check_win(x, y, player_piece, current, board):
    score = 100 + depth # faster wins count more
    if current != player:
      score = -score # it was the enemy who won
  elif depth == 1:
    score = 0 # nobody won within the moves we look at
  else:
    # Recursion: try every reply from the other player, one move deeper
    scores = [score_move(board, m, player, swap[current], player_piece, depth - 1) for m in legal_moves(board)]
    if not scores:
      score = 0 # board full, tie
    elif swap[current] == player:
      score = max(scores) # my turn next: I pick my best move
    else:
      score = min(scores) # enemy's turn next: they pick the move that is worst for me

  board[x][y] = " " # undo the move, so the board is the same as before
  return score

def brute_force(board, player, player_piece, depth):
  # Score every column and pick the best one
  local_board = copy.deepcopy(board) # practice board, the real one is not touched

  scores = {} # column -> score, e.g. {1: 0, 2: -103, 3: 102, ...}
  for move in legal_moves(local_board):
    scores[move] = score_move(local_board, move, player, player, player_piece, depth)

  print(scores)
  best = max(scores.values())
  # several columns can share the best score, pick one of them at random
  return random.choice([move for move, score in scores.items() if score == best])

def make_move(board, player, player_piece, depth=DEPTH):
  if not legal_moves(board):
    return None # board is full

  # 1. Win now, or block a win now
  possible_move = bot_1(board, player, player_piece)
  if possible_move != None:
    #print(f"Bot 1 found a win or block in column {possible_move}")
    return possible_move

  # 2. Block the enemy from getting two ways to win
  possible_move = block_double_threat(board, player, player_piece)
  if possible_move != None:
    #print(f"Blocked a double threat in column {possible_move}")
    return possible_move

  # 3. Try every move depth moves ahead
  possible_move = brute_force(board, player, player_piece, depth)
  #print(f"Brute force chose column {possible_move}")
  return possible_move
