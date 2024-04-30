from cards import Deck, Card

class Player(object):
	
	def __init__(self, cards):
		self._cards = cards
		for card in self._cards:
			card.turn()

	def __str__(self):
		result = ", ".join(map(str, self._cards))
		result += "\n  " + str(self.getPoints()) + " points"
		return result
		
	def hit(self, card):
		self._cards.append(card)
		
	def getPoints(self):
		count = 0
		for card in self._cards:
			if card.rank > 9:
				count += 10
			elif card.rank == 1:
				count += 11
			else:
				count += card.rank
		#Deduct 10 if Ace is available and need as 1
		for card in self._cards:
			if count <= 21:
				break
			elif card.rank == 1:
				count -= 10
		return count
		
	def hasBlackjack(self):
		return len(self._cards) == 2 and self.getPoints() == 21
		
	def getCards(self):
		return self._cards

class Dealer(Player):
	
	def __init__(self, cards):
		Player.__init__(self, cards)
		self._showOneCard = True
		self._cards[0].turn()
		
	def __str__(self):
		if self._showOneCard:
			return str(self._cards[0])
		else:
			return Player.__str__(self)
			
	def hit(self, deck):
		while self.getPoints() < 17:
			card = deck.deal()
			card.turn()
			self._cards.append(card)
			
	def turnFirstCard(self):
		self._showOneCard = False
		self._cards[0].turn()

class Blackjack(object):
	
	def __init__(self):
		self._deck = Deck()
		self._deck.shuffle()
		
		#Pass the player and the dealer two cards each
		self._player = Player([self._deck.deal(), self._deck.deal()])
		self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

	def getPlayerCards(self):
		return self._player.getCards()
		
	def getDealerCards(self):
		return self._dealer.getCards()
		
	def hitPlayer(self):
		card = self._deck.deal()
		card.turn()
		self._player.hit(card)
		return (card, self._player.getPoints())
		
	def hitDealer(self):
		self._dealer.turnFirstCard()
		playerPoints = self._player.getPoints()
		if playerPoints > 21:
			return "You bust and lose!"
		else:
			self._dealer.hit(self._deck)
			dealerPoints = self._dealer.getPoints()
			if dealerPoints > 21:
				return "Dealer busts, you win!"
			elif dealerPoints > playerPoints:
				return "Dealer wins :("
			elif dealerPoints < playerPoints and playerPoints <= 21:
				return "Congrats! You win!"
			elif dealerPoints == playerPoints:
				if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
					return "Blackjack! You Win!"
				elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
					return "Dealer Blackjack! You lose!"
				else:
					return "There is a tie"
