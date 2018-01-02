# -*- coding: utf-8 -*-
from TextWord import * 
from HashSlot import *

class HashMap(object):
    def __init__(self):
        self._array = [] 
        self._size = 0 # s'incrementa quan resulta necessari
        self._filledSlots = 0 # quantitat de cel·les omplertes
        self._collisionAmount = 0 # nombre de col·lisions produïdes en el procés de hash
        self._maxElemAmountInSlot = 0
	
    def prepareTable(self, size):
	'''plena de cel·les buides la taula fins als requeriments indicats'''
	for i in range(size - self._size):
	    self._array.append(HashSlot())
	    self._size += 1  
        
    def getIndex(self, key):
        '''donada una clau, retorna la seva posició a la taula hash'''
        return self.doHash(key)
    
    def getCollisionAmount(self):
	'''retorna el nombre de col·lisions en la taula'''
        return self._collisionAmount
    
    def getMaxElemAmountInSlot(self):
        '''troba i retorna el nombre d'elements que han estat insertats en la cel·la amb més afegiments'''
        return self._maxElemAmountInSlot   
    
    def __str__(self):
        text = ""
        for i in range(self._size):
	    if self._array[i].getValues():
		text += str(self._array[i])+"\n"
        return text   
    
    def put(self, key, value):
	'''afegeix un element al heap'''
        index = self.doHash(key)
		
        # si la cel·la no té clau, donem clau i valor a la cel·la
	if self._array[index].getKey() == -1:
	    self._array[index].setKey(key)
	    self._array[index].getValues().append(value)
	    self._filledSlots += 1
            
        else:
            # si és coincident, afegim les coordenades
	    i = 0
	    found = False
	    while (not found) and (i < len(self._array[index].getValues())):
		if self._array[index].getValues()[i].getWord() == value.getWord():
		    self._array[index].getValues()[i].getCoords().append(value.getCoords()[0])
		    found = True
		i += 1
                
	    # col·lisió: ampliem els valors de la cel·la
	    if not found:
		self._collisionAmount += 1
		self._array[index].getValues().append(value)
		if len(self._array[index].getValues()) > self._maxElemAmountInSlot:
		    self._maxElemAmountInSlot = len(self._array[index].getValues())		
        
    def doHash(self, word):
        '''mètode hash que retorna l'índex de la taula hash a què correspon una clau'''
        sum = 0
	i = 0
        for char in word:
	    i += 1
            sum += ord(char)*i
        return sum % self._size
    
    def insertWord(self, textWord):
        '''crida el put per insertar una paraula: la clau es generarà de l'ASCII de les lletres de la paraula en si, el valor és tot l'objecte paraula de text'''
        self.put(textWord.getWord(), textWord)
        
    def get(self, key):
        '''retorna el valor associat a la clau donada'''
        if self._size > self.getIndex(key) - 1:
	    return self._array[self.getIndex(key) -1]
	return None
    
    def calcEmptyPercentage(self):
        '''calcula i retorna el percetnatge de cel·les buides a la taula hash'''
        return float(self._size - self._filledSlots)/self._size*100
        
    def findOcurrences(self, word):
	'''si una paraula es troba a la taula hash, la mostrem'''
	index = self.getIndex(word)
	if self._array[index]:
	    for i in range(len(self._array[index].getValues())):
		if word == self._array[index].getValues()[i].getWord():
		    print self._array[index].getValues()[i]