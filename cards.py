import random

class Card:

	RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

	SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

	BACK_NAME = 'DECK/b.gif'

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self._filename = 'DECK/' + str(rank) + suit[0].lower() + '.gif'
		self._faceup = False
	
	def turn(self):
		self._faceup = not self._faceup
		
	def getFilename(self):
		if self._faceup:
			return self._filename
		else:
			return Card.BACK_NAME
        
	def __str__(self):
		if self.rank == 1:
			rank = 'Ace'
		elif self.rank == 11:
			rank = 'Jack'
		elif self.rank == 12:
			rank = 'Queen'
		elif self.rank == 13:
			rank = 'King'
		else:
			rank = self.rank
		return str(rank) + ' of ' + self.suit

class Deck(object):

	def __init__(self):
		self._cards = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				c = Card(rank, suit)
				self._cards.append(c)

	def shuffle(self):
		random.shuffle(self._cards)

	def deal(self):
		if len(self) == 0:
			return None
		else:
			return self._cards.pop(0)

	def __len__(self):
		return len(self._cards)

	def __str__(self): 
		self.result = ''
		for c in self._cards:
			self.result = self.result + str(c) + '\n'
		return self.result
