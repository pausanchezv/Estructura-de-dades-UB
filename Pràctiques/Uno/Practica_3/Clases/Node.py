class Node(object):
    
    def __init__(self, data, next = None):
        self.__data = data
	self.__next = next
	
    def __str__(self):
	return str(self.__data)
    
    def getNext(self):
	''' Retorna l'enllac al seguent Node '''
	return self.__next 
    
    def setNext(self, next):
	''' Canvia l'enllac del Node '''
	self.__next = next
	
    def getData(self):
	''' Retorna el valor del Node '''
	return self.__data 
    
    def setData(self, data):
	''' Canvia el valor del node '''
	self.__data = data
