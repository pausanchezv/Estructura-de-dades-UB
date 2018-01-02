# autores: Pau Sanchez Valdivieso y Albert Espin Roman
import random # para usar randint y obtener enteros aleatorios en un rango dado

class Card:
    '''esta clase representa una carta, con numero y color'''
    
    # constructor con numero y color
    def __init__(self, color, number): 
        self.__color = color
        self.__number = number
        
    def __str__(self):
        return ("Color:  {}, Numero: {}").format(self.get_color(), self.get_number())
     
    # getters de los atributos privados, color y number   
    def get_color(self):
        return self.__color
    
    def get_number(self):
        return self.__number
        
    # comprobar con booleano si dos cartas son compatibles (mismo numero o color)
    def check_card(self, other):
        return (self.get_color() == other.get_color() or self.get_number() == other.get_number())

    
    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):
        print "{CARD TEST}"
        carta2 = Card("yellow", 2)
        print "carta: {}".format(self)
        print "carta2: {}".format(carta2)
        print ("Son compatibles la carta {} \ny la carta {}? {}\n").format(self, carta2, self.check_card(carta2)) 

        
        
class Player:
    '''Esta clase representa a un jugador con nombre y lista de cartas'''
    
    # constructor
    def __init__(self, name):
        self.__name = name
        self.__cards = []
    
    # sobrecarga para mostrar con print
    def __str__(self):
        return ("{}, con cartas:\n{}").format(self.get_name(),self.show_cards())

    
    # sobrecarga de len para mostrar el numero de cartas del jugador
    def __len__(self):
        return len(self.get_cards())
    
    # setters y getters de los atributos privados, color y number
    def get_name(self):
        return self.__name
        
    def get_cards(self):
        return self.__cards
    
        
    # comprobar si puede jugar, si una de sus cartas es compatible con la pasada como parametro
    def can_play_card(self, card):
        for card_i in self.get_cards():
            if card.check_card(card_i): # comprueba cada carta de la iteracion
                return True
        return False
    
    # quita de las cartas del jugador la carta del indice escogido, para enviarla a la pila        
    def play_a_card(self, index, discard_pile):
        discard_pile.append(self.get_cards().pop(index))
    
    # dado un numero devuelve la primera carta del jugador con tal numero
    def select_card(self, number):
        for card_i in self.get_cards():
            if card_i.get_number() == number:
                return card_i
        return None
    
    # anyadir una carta cogida del mazo
    def add_card(self, card):
        self.get_cards().append(card)
        
    # muestra las cartas en forma de lista, para __str__
    def show_cards(self):
        text = ""
        count = 0
        for card in self.get_cards():
            count += 1
            text += "{" + str(count) + "} " + str(card) + "\n"
        return text
    
    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):  
        print "{PLAYER TEST}"
        self.add_card(Card("red",9))
        self.add_card(Card("green",1))
        print "Datos de un jugador: " + str(self)
        card = Card("blue",1)
        print "Puede jugar con la carta " + str(card) + "? " +str(self.can_play_card(card))
        print "Numero de cartas: " + str(len(self))
        card2 = Card("yellow",8)
        player.add_card(card2)
        print "El jugador coge la carta " + str(card2) 
        print "Numero de cartas: " + str(len(self)) +"\n" 
                
        
        
class Deck:
    '''Esta clase representa el mazo, con una lista de cartas'''
    
    # variables de clase
    N = 7 # constante que representa las cartas que se reparten a cada jugador al principio del juego
    COLOR_TUPLE = ("blue", "green", "red", "yellow") # tupla con los colores de cartas posibles
    
    # constructor que crea una lista de 80 cartas, que representa dos veces todas las combinacions de colores y numeros posibles
    def __init__(self):
        self.__cards = [Card(color, number) for i in range(2) for color in Deck.COLOR_TUPLE for number in range (0,9+1)] # comprension iterativa para obtener todas las combinaciones de cartas deseadas
        
    # sobrecarga de getitem para devolver carta de la lista con []
    def __getitem__(self, i):
        return self.get_cards()[i]
    
    # sobrecarga de len para devolver el numero de cartas del mazo
    def __len__(self):
        return len(self.get_cards())

    # getter
    def get_cards(self):
        return self.__cards
    
        
    # borrar la carta de una posicion en la lista del mazo
    def remove(self, i):
        self.get_cards().remove(self.get_cards()[i])
    
    # anyade al jugador especificado una carta aleatoria del mazo    
    def deal_one_card(self, player):
        player.add_card(self.get_random_card())
        
    # quita y devuelve una carta aleatoria del mazo
    def get_random_card(self):
        return self.get_cards().pop(random.randint(0,len(self.get_cards())-1))
    
    # reparte N cartas a cada jugador
    def deal(self, player_list):
        [player.add_card(self.get_random_card()) for player in player_list for i in range (Deck.N)]
                
    # retorna si el mazo esta vacio
    def is_empty(self):
        return not(len(self))
                
    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):  
        print "{DECK TEST}"
        print "Carta con indice 19: {}".format(self[19])
        print "Numero de cartas: {}".format(len(self))
        print "Primeras diez cartas:"
        for i in range(0,10):
            print self.get_cards()[i]
        player = Player("Jugador1")
        print "Un jugador coge una carta del mazo:"
        self.deal_one_card(player)
        print player.get_cards()[len(player) - 1]
        player2 = Player("Jugador2")
        print "El mazo reparte cartas a dos jugadores;"
        self.deal([player,player2])
        print "Carta en posicion 6 del segundo jugador:\n{}".format(player2.get_cards()[6]) 
        print "Carta sacada al azar: {}\n".format(self.get_random_card())
        
        
    
class Discard_Pile:
    '''esta clase representa la pila de cartas jugadas'''
    
    # constructor que coge una carta al azar del mazo y la pone en la lista de cartas descartadas
    def __init__(self, deck):
        self.__discard_pile = [deck.get_random_card()]
        
    # sobrecarga de len para mostrar el numero de cartas en la pila
    def __len__(self):
        return len(self.get_discard_pile())
    
    # getter
    def get_discard_pile(self):
        return self.__discard_pile
    
    # retorna como muestra la ultima carta de la pila
    def show_last_card(self):
        return self.get_discard_pile()[len(self.get_discard_pile()) - 1]
    
    # anyade una carta a la pila
    def append(self, card):
        self.get_discard_pile().append(card)
        
    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):  
        print "{DISCARD_PILE TEST}"
        print "Numero de cartas: {}".format(len(self))
        card = Card("blue",9)
        print "Se pone en la pila otra carta: {}".format(str(card)) 
        self.append(card)
        print "La ultima carta de la pila es: {}".format(str(self.show_last_card()))
        print "La primera carta es: {}".format(self.get_discard_pile()[0])
        print "Numero de cartas: {}\n".format(len(self))
 

# ejemplo de test de Card:
card = Card("blue",2)
card.test()

# ejemplo de test de Player:
player = Player("Yo")
player.test()

# ejemplo de test de Deck:
deck = Deck()
deck.test()

# ejemplo de test de Discard_Pile:
my_deck = Deck()
discard_pile = Discard_Pile(my_deck)
discard_pile.test()
