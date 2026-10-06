WIDTH = 7
HEIGHT = 6

board = []

def create_board():
  for i in range(HEIGHT):
    
    row = []
    #print(i, "-----------")
    for n in range(WIDTH):
      cell = "| " + str(n)
      #board.append("|")
      row.append(cell)
      #board.append("|")
      #print(n)

    board.append(row)

def print_board():
  print("±---------------------------±")
  for row in board:
    print(*row, "|")
    
  print("|---------------------------|")
  print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
  print("±---------------------------±")


create_board()
print_board()


