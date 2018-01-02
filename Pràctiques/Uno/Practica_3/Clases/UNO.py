# autors: Pau Sanchez Valdivieso y Albert Espin Roman
import random # para usar randint y obtener enteros aleatorios en un rango dado
from LinkedStack import *
from LinkedQueue import *
from LinkedPriorityQueue import *
from CircularDoubleLinkedList import *

class Card:
    '''esta clase representa una carta, con numero y color'''
    
    # constructor con numero y color
    def __init__(self, color, number, special=""): 
        self.__color = color
        self.__number = number
        self.__special = special #si se trata de una carta especial
        
    def __str__(self):
        if self.get_color() == "":
            return ("Tipo de especial: {}").format(self.get_special())
        elif self.get_special() == "":
            return ("Color:  {}, Numero: {}").format(self.get_color(), self.get_number())
        else:
            return ("Color:  {}, Tipo de especial: {}").format(self.get_color(), self.get_special())
    
    #sobrecarga de cmp para comparar cartas segun color y numero
    def __cmp__(self, other):
        if((self.get_color() == other.get_color()) and (self.get_number() == other.get_number())):
            return 0 # son iguales
        
        color_index_one = self.get_color_index(self)
        color_index_other = self.get_color_index(other)
        # si los colores son iguales, el de menor numero se considera primero
        if (color_index_one == color_index_other):
            if (self.get_number() > other.get_number()):
                return 1
            return -1

        #si los colores son diferentes:
        else: 
            if (color_index_one > color_index_other):
                return 1
            return -1

        
    # setters y getters de los atributos privados, color y number   
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        self.__number = number
    
    def get_special(self):
        return self.__special
        
    # comprobar con booleano si dos cartas son compatibles (mismo numero o color)
    def check_card(self, other):
        if (self.get_color() == "") or(other.get_color() == ""):
            return True # siempre se puede tirar una carta de cambio de color        
        if (not self.get_special()) and (not other.get_special()):
            return (self.get_color() == other.get_color() or self.get_number() == other.get_number())
        return self.get_color() == other.get_color() # si es especial solo se tiene en cuenta el color
    
    # obtiene un indice de color segun la tupla de colores posibles para las cartas
    def get_color_index(self, card):
        i = 0
        COLOR_TUPLE = ("blue", "green", "red", "yellow") # tupla con los colores de cartas posibles
        while (i < len(COLOR_TUPLE)) and (COLOR_TUPLE[i] != card.get_color()): 
            i+=1

        return i         

    
    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):
        print "{CARD TEST}"
        carta2 = Card("yellow", 2)
        print "carta: {}".format(self)
        print "carta2: {}".format(carta2)
        print ("Son compatibles la carta {} \ny la carta {}? {}\n").format(self, carta2, self.check_card(carta2)) 

        
        
class Player(LinkedPriorityQueue):
    '''Esta clase representa a un jugador con nombre y lista de cartas'''
    
    # constructor
    def __init__(self, name):
        LinkedPriorityQueue.__init__(self)
        self.__name = name
        # aunque no se muestre, tiene una lista de items, las cartas, heredada, que comienza vacia
    
    # sobrecarga para mostrar con print
    def __str__(self):
        return ("{}, con cartas:\n{}").format(self.get_name(),self.show_cards())
    
    # setters y getters de los atributos privados
    def get_name(self):
        return self.__name         
        
    # comprobar si puede jugar, si una de sus cartas es compatible con la pasada como parametro
    def can_play_card(self, card):
        for card_i in self.get_items():
            if card.check_card(card_i): # comprueba cada carta de la iteracion
                return True
        return False
    
    # quita de las cartas del jugador la carta del indice escogido, para enviarla a la pila        
    def play_a_card(self, index, discard_pile):
        array = []
        for i in range(index):
            array.append(self.dequeue())
        selected_card = self.dequeue()
        
        for i in range(len(array)):
            self.enqueue(array[i])
        
        
        # ponemos en primer lugar la carta a jugar para que dequeue, que quita la primera, la quite efectivamente
        discard_pile.push(selected_card)
    
    # anyadir una carta cogida del mazo
    def add_card(self, card):
        self.enqueue(card)
      
    # muestra las cartas en forma de lista, para __str__
    def show_cards(self):
        text = ""
        count = 0
        for card in self.get_items():
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
                
        
        
class Deck(LinkedQueue):
    '''Esta clase representa el mazo, con una lista de cartas'''
    
    # variables de clase
    N = 7 # constante que representa las cartas que se reparten a cada jugador al principio del juego
    COLOR_TUPLE = ("blue", "green", "red", "yellow") # tupla con los colores de cartas posibles
    SPECIAL_TUPLE = ("Reverse", "Skip","+2","+4","ChangeColor")

    # constructor que crea una lista de 80 cartas, que representa dos veces todas las combinacions de colores y numeros posibles
    def __init__(self, player_num):
        # factor usado para poder ofrecer un numero de cartas razonable ajustado al numero de jugadores escogidos, sin limites
        card_factor = self.calculate_card_factor(player_num)
        LinkedQueue.__init__(self)
        # iteracion para obtener todas las combinaciones de cartas deseadas
        for number in range (0,9+1):
            for color in Deck.COLOR_TUPLE:
                for i in range(card_factor):
                    self.enqueue(Card(color, number))

        for i in range(len(self.SPECIAL_TUPLE)-1):
            for color in Deck.COLOR_TUPLE:
                for j in range(card_factor):
                    self.enqueue(Card(color, -1, self.SPECIAL_TUPLE[i]))
                    
        for color in Deck.COLOR_TUPLE:
            for j in range(card_factor):
                self.enqueue(Card("",-2, self.SPECIAL_TUPLE[-1]))# ChangeColor
                            
        
    # calcula las cartas a generar segun el numero de jugadores
    def calculate_card_factor(self, player_num):
        num = player_num
        if num < 4: return 2        
        while (True):
            if num % 4 == 0:                
                return num/2
            else: num+=1        
            
    
    # anyade al jugador especificado una carta aleatoria del mazo    
    def deal_one_card(self, player):
        player.add_card(self.get_random_card())
        
    # quita y devuelve una carta aleatoria del mazo
    def get_random_card(self):
        index = random.randint(0,len(self)-1)
        earlier_first = self[0].getData()
        self[0].setData(self[index].getData())
        self[index].setData(earlier_first)
        return self.dequeue()
    
    # reparte N cartas a cada jugador
    def deal(self, player_list):
        for i in range(Deck.N):
            for j in range(len(player_list)):
                player_list.get_items()[j].add_card(self.get_random_card())
                
                
    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):  
        print "{DECK TEST}"
        print "Carta con indice 19: {}".format(self[19])
        print "Numero de cartas: {}".format(len(self))
        print "Primeras diez cartas:"
        for i in range(0,10):
            print self[i]
        player = Player("Jugador1")
        print "Un jugador coge una carta del mazo:"
        self.deal_one_card(player)
        print player.get_items()[len(player) - 1]
        player2 = Player("Jugador2")
        print "El mazo reparte cartas a dos jugadores;"
        player_list = CircularDoubleLinkedList()
        player_list.insertFirst(player2)
        player_list.insertFirst(player)
        self.deal(player_list)
        print "Carta en posicion 6 del segundo jugador:\n{}".format(player2.get_items()[6]) 
        print "Carta sacada al azar: {}\n".format(self.get_random_card())
        
        
    
class Discard_Pile (LinkedStack):
    '''esta clase representa la pila de cartas jugadas'''
    
    # constructor que coge una carta al azar del mazo y la pone en la lista de cartas descartadas
    def __init__(self, deck):
        LinkedStack.__init__(self) # iniciamos el constructor de la superclase
        self.push(deck.get_random_card())
    
    # retorna como muestra la ultima carta de la pila
    def show_last_card(self):
        return self.peek()

    # funcion para probar la funcionalidad de los objetos de esta clase
    def test(self):  
        print "{DISCARD_PILE TEST}"
        print "Numero de cartas: {}".format(len(self))
        card = Card("blue",9)
        print "Se pone en la pila otra carta: {}".format(str(card)) 
        self.push(card)
        print "La ultima carta de la pila es: {}".format(str(self.show_last_card()))
        print "La primera carta es: {}".format(self.get_items()[0])
        print "Numero de cartas: {}\n".format(len(self))
    
    
    
class ONE():
    '''clase principal del juego UNO'''
    
    # constructor que crea jugadores, mazo y pila
    def __init__(self):
        self.__player_list = CircularDoubleLinkedList() # para gestionar el orden con las particularidades de la cola
        self.__names_list = []
        self.__current_player = None # jugador cuyo turno es actual
        self.__deck = list() # ahora es algo vacio, se inicializa con el numero de jugadores preguntado luego
        self.__discard_pile = Discard_Pile(deck)
        
    # getters y setters
    def get_player_list(self):
        return self.__player_list
    
    def set_player_list(self, player_list):
        self.__player_list = player_list
    
    def get_names_list(self):
        return self.__names_list
    
    def get_current_player(self):
        return self.__current_player
    
    def set_current_player(self, current_player):
        self.__current_player = current_player
        
    def get_deck(self):
        return self.__deck
    
    def get_discard_pile(self):
        return self.__discard_pile
    
    
    # FUNCIONES MAS RELEVANTES:
    
    # muestra una bienvenida, define los jugadores, reparte cartas iniciales y genera un orden de juego
    def prepare_game(self):
        self.show_welcome()
        self.define_players()
        self.get_deck().deal(self.get_player_list()) # reparte cartas
        self.generate_order()

    
    # clase principal que ejecuta el juego    
    def run_game(self):
        self.prepare_game()
        # configura como jugador actual el primero en la lista de jugadores
        self.set_current_player(self.get_player_list().get_items()[0])
        
        # comprobamos si empieza el juego con una carta especial
        self.check_special_card_in_game()
        
        # mientras no se gana o acaba el juego se sigue jugando
        while (not self.stop_criterion(self.get_current_player())):
            # si va a robar cartas, muestra antes las iniciales, por criterio estetico
            if (not self.current_can_play()):
                self.visualize_state() # mostrar estado
                
            # mientras no puede jugar, roba cartas del mazo
        
            while(not self.current_can_play()):
                print "No puedes tirar."
                # roba una carta para el jugador actual
                self.current_pick_card()
            

            # una vez puede jugar:
            
            # mientras no tiene que robar cartas, puede ir jugando y tirando
            while(self.current_can_play()):
                # se muestra de nuevo el estado, para comprobar las cartas que se tienen
                self.visualize_state()
                
                # se pregunta el numero de carta que quiere jugar hasta que da uno que la carta de la pila en juego acepta
                index = self.ask_card_number()
                while (not self.is_selected_card_allowed(index)):
                    print "Esa carta no coincide ni en numero ni en color!\n"            
                    index = self.ask_card_number()
                
                # una vez se ha escogido una carta valida, se juega con ella
                print "\nHas tirado una carta.\n"
                self.get_current_player().play_a_card(index,self.get_discard_pile())
                # comprobamos si la carta tirada es especial, para desencadenar sus efectos
                # si alguien se queda sin cartas al lanzar una carta especial, se acaba aqui el juego
                winner = self.check_special_card_in_game()
                if winner != None: 
                    self.announce_champion(winner)
                    return
            
            # si el jugador actual no ha ganado, hay cambio de turno
            if(not self.stop_criterion(self.get_current_player())): 
                self.change_turn()
        
        # si el jugador actual se queda sin cartas, gana y es felicitado    
        self.announce_champion(self.get_current_player())
            
    
    # muestra el estado del juego por pantalla        
    def visualize_state(self):
        print "Carta en juego: " + str(self.get_discard_pile().show_last_card())
        print "Es el turno de " + str(self.get_current_player())
    
        
    # determina si se acaba el juego (si al jugador actual le quedan 0 cartas)    
    def stop_criterion(self, current_player):
        return len(current_player) == 0
    
    
    # felicita al jugador actual por su victoria
    def announce_champion(self, winner):
        print "############################################\n  Enhorabuena, " + str(winner.get_name()) + ", has ganado el juego! \n############################################"  
      
        #########
    # cambia de turno, de uno jugador al siguiente en la lista
    def change_turn(self, jumped=False, multiPick=False):
        if (not jumped) and (not multiPick):
            print "No puedes tirar.\nCambio de turno.\n"
        elif jumped: 
            print "La carta especial ha dejado sin turno al siguiente jugador, {}!".format(self.get_player_list().get_items()[1].get_name())
        # basandonos en la forma de operar de las colas, para alternar el orden pasamos el que era el jugador actual, con indicde 0 en la lista, al final, y por tanto el segundo pasa a primero
        new_current_player = self.get_player_list().removeFirst().getData()
        self.get_player_list().insertLast(new_current_player)
         
        # configura como jugador actual el primero en la lista de jugadores
        self.set_current_player(self.get_player_list().get_items()[0])            
            
        
    # FUNCIONES AUXILIARES:
    
    # muestra un mensaje de bienvenida al inicio del juego
    def show_welcome(self):
        print "\n######################\n# BIENVENIDO/A A UNO #\n######################\n"
    
    # define los jugadores a partir de preguntar la cantidad y sus numbres    
    def define_players(self):   
        player_num = self.ask_player_num()
        self.__deck = Deck(player_num) # llenamos de cartas el deck segun el numero de jugadores
        player_names = self.ask_player_names(player_num)
        
        # anyade el numero de jugadores necesarios con sus nombres preguntados
        for i in range(player_num):
            self.get_player_list().insertLast(Player(player_names[i]))           
     
    # pregunta y retorna el numero de jugadores 
    def ask_player_num(self):
        while (True):
            # preguntamos cuantos jugadores juegan, insistiendo hasta que el input tiene validez
            try:
                player_num = int(raw_input("Cuantos jugadores hay? (1-infinito) "))
                if player_num >= 1:
                    break # valor con validez
                print "Eso es negativo!"
            except ValueError: # si se introduce un caracter no numerico
                print "Eso no es un numero!"
        return player_num
        
    # retorna el nombre de los jugadores, pedidos al usuario    
    def ask_player_names(self, player_num):
        name = ""
        for i in range(player_num):
            name = (raw_input("Como se llama el jugador " + str(i+1) + "? "))
            # comprueba que no haya repeticiones de nombre, va pidiendo hasta que se teclea uno nuevo
            while (self.is_name_repeated(name)):
                name = (raw_input("Nombre repetido!\nComo se llama el jugador " + str(i+1) + "? "))            
            self.get_names_list().append(name)
        return self.get_names_list()
    
    # comprueba y retorna si un nombre ya esta en uso
    def is_name_repeated(self, name):
        for name_i in self.get_names_list():
            if name == name_i:
                return True
        return False        
    
    # altera el orden en la lista de jugadores, y se aprovechan las nuevas posiciones como ordren         
    def generate_order(self):
        num = random.randint(0,len(self.get_player_list()))
        for i in range(0, num):
            picked = self.get_player_list().removeLast().getData()
            self.get_player_list().inserti(i,picked)
        print "Se ha generado un orden de turnos aleatorio.\n"
            
    # devuelve si el jugador actual puede jugar       
    def current_can_play(self):
        return self.get_current_player().can_play_card(self.get_discard_pile().show_last_card())
        
    # rellena el mazo con todas las cartas de la pila menos la visible
    def fill_deck(self):
        # llena mientras la pila no se quede con una sola carta
        i = 0
        while(i < len(self.get_discard_pile()) -1):
            self.get_deck().enqueue(self.get_discard_pile().pop()) 
            i += 1
        print "\nMAZO RENOVADO!\n"
        
    # coge carta del mazo y la da al jugador actual, que roba
    def current_pick_card(self):
        # si el mazo esta lleno se rellena con cartas de la pila
        if (self.get_deck().isEmpty()):
            self.fill_deck()
            
        added_card = self.get_deck().get_random_card()
        self.get_current_player().add_card(added_card)
        print "Carta robada: " + str(added_card) + "\n"
            
    
    # devuelve el indice de una carta del jugador, preguntada e introducida por teclado   
    def ask_card_number(self):
        num = 0
        while (True):
            try:
                num = int(raw_input("Introduce el numero de la carta a jugar: ")) -1 # restamos 1 porque en pantalla empiezan desde 1 y no desde 0 los numeros
                if num < len(self.get_current_player()):
                    break
                else: print "No tienes tantas cartas!\n"
            except ValueError: # si se introduce un caracter no numerico
                print "Eso no es un numero!\n"
        return num
    
    # devuelve si el jugador actual puede jugar con la carta que ha seleccionado
    def is_selected_card_allowed(self, index):
        return self.get_current_player().get_items()[index].check_card(self.get_discard_pile().show_last_card())
    
    # cambia el turno de juego
    def invert_turns(self):
        turned_list= CircularDoubleLinkedList()
        reversed_list = reversed(self.get_player_list().get_items())
        for elem in reversed_list:
            turned_list.insertLast(elem)
        self.set_player_list(turned_list)
        
        self.set_current_player(self.get_player_list().get_items()[0])
     
    # gestiona los efectos de las cartas especiales y devuelve un ganador si lo hay a causa de tirar una carta especial   
    def check_special_card_in_game(self):
        special = self.get_discard_pile().show_last_card().get_special()
        if(special):
            if not len(self.get_current_player()):
                return self.get_current_player()
            else:
                if(special == "Reverse"):
                    print "Se ha producido una inversion en el orden de turnos de juego.\n"
                    self.invert_turns()
                elif(special == "Skip"):
                    self.change_turn(True)
                    self.change_turn()
                elif(special == "+2"):
                    self.change_turn(False,True)
                    print "La carta especial castiga a {} a robar 2 cartas y perder el turno.\n".format(self.get_current_player().get_name())
                    for i in range(2): self.current_pick_card()
                    self.change_turn()
                elif(special == "+4"):
                    self.change_turn(False,True)
                    print "La carta especial castiga a {} a robar 4 cartas y perder el turno.\n".format(self.get_current_player().get_name())
                    for i in range(4): self.current_pick_card()
                    self.change_turn()
                else: #ChangeColor
                    self.get_discard_pile().show_last_card().set_color(self.get_color_from_menu())
                    if (not self.current_can_play()): self.change_turn()
                while(not self.current_can_play()):
                    print "No puedes tirar."
                    # roba una carta para el jugador actual
                    self.current_pick_card()                    
                return None
        
    # pregunta el color al que cambiar la carta especial de cambio de color    
    def get_color_from_menu(self):
        while(True):
            try:
                print "Selecciona el color al que quieres cambiar:"
                for i in range(len(self.get_deck().COLOR_TUPLE)):
                    print "{}: {}\n".format(i+1,self.get_deck().COLOR_TUPLE[i])
                num = int(raw_input())
                if num >0 and num<=len(self.get_deck().COLOR_TUPLE): 
                    break
                else: print "Ese numero no pertenece al rango esperado!"
            except ValueError: print "Eso no es un entero!"
        print "Color cambiado a {}.".format(self.get_deck().COLOR_TUPLE[num-1])
        return self.get_deck().COLOR_TUPLE[num-1]
            
# ejemplo de test de Card:
card = Card("blue",2)
card.test()

# ejemplo de test de Player:
player = Player("Yo")
player.test()

# ejemplo de test de Deck:
deck = Deck(4)
deck.test()

# ejemplo de test de Discard_Pile:
my_deck = Deck(0)
discard_pile = Discard_Pile(my_deck)
discard_pile.test()

# ejecucion del juego UNO
one = ONE()
one.run_game()