 # -*- coding: utf-8 -*-

from TextWord import *
import math

class Heap(object):
    def __init__(self):
        self._heap = list()
	self._size = 0
	self._sortedList = list()
	
    def getHeap(self):
	return self._heap

    def getSortedList(self):
	return self._sortedList
    
    def insertWord(self,item):
	'''inserta una paraula de text al lloc adient del heap'''
    	self._heap.append(item)
	self._size += 1
	curPos=len(self._heap)-1	
	found = False
	while curPos> 0 and not found:
	    parent = (curPos-1) / 2
	    parentItem	= self._heap[parent]	
	    if parentItem <= item:	
		found = True	
	    else:
		# upHeap que intercanvia el valor d'un node i del seu pare perquè el d'aquest és major que el de baix i cal invertir-ho per respectar els principis del heap
		self._heap[curPos] = self._heap[parent]	
		self._heap[parent] = item	
		curPos = parent			

    def downHeap(self,i):
	'''mentre el valor d'un node és major que el d'algun dels seus fills, es va desplaçant avall de l'estructura'''
	while (i * 2 + 1) < self._size:
	    smallesti = self.smallestChild(i)
	    if self._heap[i] > self._heap[smallesti]:
		value = self._heap[i]
		self._heap[i] = self._heap[smallesti]
		self._heap[smallesti] = value
	    i = smallesti    
	    
    def smallestChild(self,i):
	'''torna l'índex del node fill de menor valor donat el node d'una posició'''
	if i * 2 + 2 == self._size or self._heap[i*2+1] < self._heap[i*2+2]:
	    return i * 2 + 1
	else:
	    return i * 2 + 2 
    
    def removeMin(self):
	'''elimina del heap i retorna el node amb valor menor, tot restructurant el heap per respectar que els valors menors estiguin més amunt''' 
	if self._size >= 0:
	    elem = self._heap[0]
	    self._heap[0] = self._heap[self._size -1]
	    self._size -= 1
	    self._heap.pop()
	    self.downHeap(0)
	    return elem    
	return None
    
    def heapSort(self, sortedList=[]):	
	sortedList = list()
	sortedList.append(self.removeMin())
	while (self._size>0):
	    newElem = self.removeMin()
	    if sortedList[-1] != newElem:
		sortedList.append(newElem)
	    else: # compactar coordenades
		sortedList[-1].getCoords().append(newElem.getCoords())
	self._sortedList = sortedList
	return self._sortedList
	
    def binarySearch(self, array, value, left=None, right=None):
	'''retorna l'índex d'un valor en una llista o -1 si no hi és'''
	if not left and not right:
		left = 0
		right = len(array) -1
	if right < left:
		return -1
	mid = (left + right) / 2
	if value > array[mid].getWord():
		return self.binarySearch(array, value, mid + 1, right)
	elif value < array[mid].getWord():
		return self.binarySearch(array, value, left, mid - 1)
	else:
		return mid    
    
    def findOcurrences(self, item):
	'''cerca una paraula dins el heap; en cas de trobar-la, la mostra amb les seves coordenades'''
	index = self.binarySearch(self._sortedList, item)
	if index != -1:
	    print self._sortedList[index]
	
    def calculateDepth(self):
	'''calcula i retorna la profunditat de l'arbre, que no és altra que el logaritme en base 2 del nombre de valors que conté'''
	return int(math.ceil(math.log(self._size,2)))