def chessboard(list):
  for i in range(0, len(list), 3):
    print "|", list[i], "|", list[i+1], "|", list[i+2], "|"
    print "-------------"

def marker():
  mark = ""
  while not (mark == "O" or mark == "X"):
    mark = raw_input("Which side do you choose, X or O? ").upper()
  if mark == "X":
    return ("X", "O")
  if mark == "O":
    return ("O", "X")

def Plays(player):
  xP = raw_input("Player " + player + "'s turn: ")
  if xP.isdigit():
    xP = int(xP) - 1
    if 0 <= xP <= 8:
      if isinstance(ll[xP], int):
        ll[xP] = player
      else:
        print "Wrong play, input your play again!"
        Plays(player)
    else:
      print "Wrong play, input your play again!"
      Plays(player)
  else:
    print "Wrong play, input your play again!"
    Plays(player)
  
def win(player):
  if (ll[0] == ll[1] == ll[2] == player) or \
  (ll[3] == ll[4] == ll[5] == player) or \
  (ll[6] == ll[7] == ll[8] == player) or \
  (ll[0] == ll[3] == ll[6] == player) or \
  (ll[1] == ll[4] == ll[7] == player) or \
  (ll[2] == ll[5] == ll[8] == player) or \
  (ll[0] == ll[4] == ll[8] == player) or \
  (ll[2] == ll[4] == ll[6] == player):
    return True

def tictac():
  a, b = side
  Plays(a)
  chessboard(ll)
  if win(a):
    print "Player " + a + " is the winner!"
    replay()
  else:
    if gameover():
      print "It's a draw!"
    else:
      Plays(b)
      chessboard(ll)
      if win(b):
        print "Player " + b + " is the winner!"
        replay()
      else:
        if gameover():
          print "It's a draw!"
        else:
          tictac()
  
def gameover():
  for num in ll:
    if isinstance(num, int):
      return False
  return True

def replay():
  answer = ""
  while not (answer == "Y" or answer == "N"):
    answer = raw_input("Do you want to play it again? Yes(y) or No(n)>").upper()
  if answer == "Y":
    newgame()
  else:
    print "Thank you for playing the game!"
    
def newgame():
  ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  global ll
  chessboard(ll)
  side = marker()
  global side
  tictac()
  
ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chessboard(ll)
side = marker()
tictac()