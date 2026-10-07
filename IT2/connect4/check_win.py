def check_vertical(x, y, player_piece, player, board):

  counter = 0
  for n in range(4):
    try:
      if board[x][y + n] == str(player_piece[player]):
        counter += 1
        #print(counter)
    except:
      return False

    if counter == 4:
      return True

def check_horizontal(x, y, player_piece, player, board):
  counter = 0
  for n in range(-4, 4):
    try:
      if board[x + n][y] == str(player_piece[player]):
        counter += 1
        print(counter)
    except:
      return False

    if counter == 4:
      return True
  

def check_diagonal_right(x, y, player_piece, player, board):
  pass

def check_diagonal_left(x, y, player_piece, player, board):
  pass
