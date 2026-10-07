
def check_vertical(x, y, player_piece, player, board):
  counter = 0
  for n in range(4):
    try:
      if board[x][y + n] == str(player_piece[player]):
        counter += 1
        #print(counter)
      else:
        return False
    except:
      return False

    if counter == 4:
      return True

def check_horizontal(x, y, player_piece, player, board):
  counter = 0
  for n in range(-3, 4):
    cx = x + n
    cy = y

    if cx < 0 or cx >= len(board):
      continue

    if board[cx][cy] == player_piece[player]:
      counter += 1
      if counter == 4:
        return True
    else:
      counter = 0
      
  return False
  

def check_diagonal_right(x, y, player_piece, player, board):
  counter = 0
  for n in range(-3, 4):
    cx = x + n
    cy = y - n

    if cx < 0 or cx >= len(board) or cy < 0 or cy >= len(board[0]):
      continue

    if board[cx][cy] == player_piece[player]:
      counter += 1
      if counter == 4:
        return True
    else:
      counter = 0

  return False


def check_diagonal_left(x, y, player_piece, player, board):
  counter = 0
  for n in range(-3, 4):
    cx = x + n
    cy = y + n

    if cx < 0 or cx >= len(board) or cy < 0 or cy >= len(board[0]):
      continue

    if board[cx][cy] == player_piece[player]:
      counter += 1
      if counter == 4:
        return True
    else:
      counter = 0

  return False


def check_win(x, y, player_piece, player, board):
  return (check_vertical(x, y, player_piece, player, board)
       or check_horizontal(x, y, player_piece, player, board)
       or check_diagonal_left(x, y, player_piece, player, board)
       or check_diagonal_right(x, y, player_piece, player, board))