import random
# define player and his hand
class Player(object):
  hand1 = 0
  hand2 = 0
  bet = 0
  playerHand = []
  bust = False
  win = False
  
  def result(self):
    if self.hand1 == 21 or self.hand2 == 21:
      print "-" * 10
      print "%s has BlackJack!" % self.name
      self.win = True
      self.calcu()
    elif self.hand1 > 21:
      self.bust = True
      print "%s's hands were busted!" % self.name
      self.calcu()
      
  def calcu(self):
    if self.win == True and self.bust == False:
      print "%s has won!" % self.name
      self.bankroll += self.bet
    elif self.win == False and self.bust == True:
      print "%s lost!" % self.name
      self.bankroll -= self.bet
    print "%s's bank amount is: $%d." % (self.name, self.bankroll)
  
  def __init__(self, name, bankroll):
    self.name = name
    self.bankroll = bankroll
    
  def startbet(self, amount):
    self.bet = amount
    print "%s bet $%d!" % (self.name, self.bet)
    print "-" * 10
  
  def double(self):
    self.bet *= 2
 
  def hit(self):
    pick = random.randint(0, len(deck)-1)
    draw = deck.pop(pick)
    self.playerHand.append(draw)
    print "%s draws a card, it is %s" % (self.name, draw)
    print "-" * 10

  def hand(self):
    handValue1 = 0
    handValue2 = 0
    print "%s's hands are:" % self.name
    for card in self.playerHand:
      handcard = Card(card)
      print handcard.showCard(card)
      if handcard.value == [1, 11]:
        handValue1 += 1
        handValue2 += 11
      else:
        handValue1 += handcard.value
        handValue2 += handcard.value
        
    self.hand1 = handValue1
    self.hand2 = handValue2 
    print "-" * 10
    print "The total value of %s's hands is: %d or %d." % (self.name, handValue1, handValue2)  

  def clear(self):
    self.playerHand = []
    self.bet = 0
    self.win = False
    self.bust = False


# define the cards
class Card(object):
  
  def __init__(self, card):
    a, b = card
    self.suit = a
    self.value = b
    if b == 'Jack' or b == 'Queen' or b == 'King':
      self.value = 10
    elif b == 'Ace':
      self.value = [1, 11]
      
  def showCard(self, card):
    a, b = card
    return "%s %s" % (a, b)
    
# generate a deck
class Deck(object):
  deck = []
  
  def createDeck(self):
    for suit in ['Spade', 'Heart', 'Club', 'Diamond']:
      for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']:
        self.deck.append((suit, value))
  
    return self.deck

# game process
def wholeGame():  

  def gameBegin():
    deck = Deck().createDeck()
    global deck
    dealer.clear()
    player.clear()
    if dealer.bankroll > 10 and player.bankroll > 10:
      print ""
      print "--- Game starts! ---"
      while True:
        try:
          num = int(raw_input("How much do you want to bet? >>"))
        except:
          print "Sorry, I cannot hear you, say it again."
        else:
          if num < 5:
            print "Sorry, the minimum amount for bet is $5."
          else:
            break
      print "-" * 10
      dealer.startbet(num)
      player.startbet(num)
      dealer.hit()
      player.hit()
      player.hit()
      player.hand()
      player.result()
      if player.win == True:
        dealer.bust = True
        dealer.calcu()
        replay()
      else:
        playerTurn()
    else:
      print "Not enough money for game, come again next time!"
  
  def playerTurn():
    answer = ""
    while not (answer == "hit" or answer == "double" or answer == "stand" or answer == "surrender"):
      answer = raw_input("What will you do, hit, stand, surrender or double? >").lower()
    if answer == "hit":
      player.hit()
      player.hand()
      player.result()
      if player.win == False and player.bust == False:
        playerTurn()
    elif answer == "double":
      player.double()
      dealer.double()
      print "The bet is %d now." % player.bet
      player.hit()
      player.hand()
      print
      player.result()
      if player.win == False and player.bust == False:
        playerTurn()
    elif answer == "stand":
      dealerTurn()
    else:
      print "You surrender, lose all the bets!"
      player.bust = True
      player.bet /= 2
      player.calcu()
      dealer.win = True
      dealer.bet /= 2
      dealer.calcu()
    replay()
      
  def dealerTurn():
    dealer.hand()
    while dealer.hand1 < 17 or dealer.hand2 < 17:
      dealer.hit()
      dealer.hand()
    dealer.result()
    if dealer.win == True:
      player.bust = True
      player.calcu()
    elif dealer.bust == True:
      player.win = True
      player.calcu()
    else:
      if dealer.hand2 < 21:
        if player.hand2 < 21:
          if player.hand2 < dealer.hand2:
            payout(dealer, player)
          elif dealer.hand2 < player.hand2:
            payout(player, dealer)
          else:
            print "It's a draw game. Take back own bet."
        else:
          if player.hand1 < dealer.hand2:
            payout(dealer, player)
          elif dealer.hand2 < player.hand1:
            payout(player, dealer)
          else:
            print "It's a draw game. Take back own bet."
      else:
        if player.hand2 < 21:
          if player.hand2 < dealer.hand1:
            payout(dealer, player)
          elif dealer.hand1 < player.hand2:
            payout(player, dealer)
          else:
            print "It's a draw game. Take back own bet."
        else:
          if player.hand1 < dealer.hand1:
            payout(dealer, player)
          elif dealer.hand1 < player.hand1:
            payout(player, dealer)
          else:
            print "It's a draw game. Take back own bet."
            
  def payout(p1, p2):
    p1.win = True
    p2.bust = True
    p1.calcu()
    p2.calcu()
     
  def replay():
    query = ""
    while not (query == "yes" or query == "y" or query == "no" or query == "n"):
      query = raw_input("Do you want to play it again, Yes or No? > ").lower()
    if query == "yes" or query == "y":
      gameBegin()
    else:
      print "Goodbye, see you next time!"
      quit()
        
  print "===== Welcome to the Blackjack game ====="
  name = raw_input("What's your name? >")
  while True:
    try:
      bank = int(raw_input("How much do you bring to the table? >"))
    except:
      print "not right number, show us your money again."
    else:
      break
  dealer = Player('Dealer', 1000)
  player = Player(name, bank)
  gameBegin()

wholeGame()
