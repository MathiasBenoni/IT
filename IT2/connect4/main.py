WIDTH = 7
HEIGHT = 6

board = []

def create_board():
  for i in range(WIDTH):
    
    row = []
    print(i, "-----------")
    for n in range(HEIGHT):
      row.append(n)
      print(n)
    board.append(row)



create_board()
print(board)
for row in board:
    print(*row)