from Node import *

class TwoWayNode(Node):
    
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.__previous = previous
        
    def getPrevious(self):
	''' Retorna l'enllac al seguent Node '''
	return self.__previous 
    
    def setPrevious(self, previous):
	self.__previous = previous
        
    # Tots els altres metodes necessaris hereden de Node
