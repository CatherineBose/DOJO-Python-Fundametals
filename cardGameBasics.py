from random import shuffle

class Card(object):
    def __init__(self,suits,cardvalue):
        self.suits = suits
        self.cardvalue = cardvalue

class Deck(object):
    def __init__(self):
        self.numcards = []
        self.totalCardsAvailable = len(self.numcards)
 
    def createDeck(self):
        suits=["spades","diamonds","hearts","clubs"]
        cardvalue=["1","2","3","4","5","6","7","8","9","10","11","12","13 "]
        print "Deck created"
        for i in range(0,4):
            for x in range(0,13):
                cardsInDeck = Card(suits[i],cardvalue[x])
                # all cards are stored in num array
                self.numcards.append(cardsInDeck)
                # print "card1 Suits {} card1 value {}".format( card1.suits,card1.cardvalue)
               
        return self
    def shufflecards(self):
        shuffle(self.numcards)
        print "Array of cards", self.numcards 

    def deal(self,user):
        print "Hi player",user.name
        print "Total cards available in deck",self.totalCardsAvailable
        print "######## We are Dealing now lets shuffle!!!##########"
        self.shufflecards()
        self.totalCardsAvailable = len(self.numcards) 
        
        print "Each player gets 1 card by default" 
        user.hand.append(self.numcards.pop())
        user.totalCardsInHand += 1
        print "Card added in hand is",user.hand[(len(user.hand))-1].suits,":",user.hand[(len(user.hand))-1].cardvalue
        return user.hand

class Player(object):
    def __init__(self,name,deckOBj):
        self.name = name
        self.hand = []
        self.totalCardsInHand = 0
        self.deck = deckOBj
        # decklist is obj of deck
    def drawfromdeck(self):
        print "########Drawing a card from deck!!#######"
        for i in range (1, 2):
            self.hand.append(self.deck.numcards.pop())
            self.totalCardsInHand += 1
            self.deck.totalCardsAvailable -= 1
            print "One card drawn from deck, total avilable cards:", len(self.deck.numcards)
            print "Total no of cards in hand is:", self.totalCardsInHand
    
        return self
      
    def showcardsinhand(self):
        print "######Show Cards player {}#########".format(self.name)
        lengthOfHand = len(self.hand)
        print "totalCardsInHand: ", self.totalCardsInHand
        for x in range (0,lengthOfHand):
            print "Suit: {} Card Value: {}".format(self.hand[x].suits,self.hand[x].cardvalue)
          
        return self

    def discardCard(self):
        print "Discarding one card at a time:"
        self.hand.pop()
        self.totalCardsInHand -= 1


# instance of deck
deck1 = Deck()
# create a player
player1 = Player("Phil", deck1)
# # # create a deck and deal
deck1.createDeck().deal(player1)
# # # Players shows the cards
player1.showcardsinhand()
# #  Player draws from deck
player1.drawfromdeck()
# # Discarding a card
player1.discardCard()
# player1.showcardsinhand()
player1.drawfromdeck()
player1.showcardsinhand()
# # print "player1.name:" , player1.name