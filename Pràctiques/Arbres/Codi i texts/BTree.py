 # -*- coding: utf-8 -*-
from Node import *


class BTree(object):
    '''classe que representa un arbre binari'''
    def __init__(self, val = None, left = None, right = None):
        if (not(val)):
            self._root = None
        elif (not(left) and not(right)):
            self._root = Node(val)
        elif (not(left) and right):
            self._root = Node(val, None, right.getRoot())
        elif (left and not(right)):
            self._root = Node(val, left.getRoot(), None)
        else:
            self._root = Node(val, left.getRoot(), right.getRoot())
	self._left = left
	self._right = right
	
    def setRootVal(self, item):
	if (self._root):
	    self._root.setVal(item)
	else:
	    self._root = Node(item)	
                
    def getRoot(self):
        return self._root
    
    def setRoot(self, root):
	self._root = root
    
    def getLeft(self):
        if ((self._root) and (self._root.getLeft())):
            return self._root.getLeft().getVal()
        return None
    	    
    def getRight(self):
	if ((self._root) and (self._root.getRight())):
	    return self._root.getRight().getVal()
	return None    
    

    def insertWord(self, item, probe=None):
	'''inserta una paraula a l'arbre binari'''
	if not probe:
	    probe = self.getRoot()
	if probe:	    
	    if (item < probe.getVal()): # si el nou valor és menor que el d'un node, ens fixem en la seva descendència esquerra
		if (probe.getLeft() != None): # si té fill esquerre, analitzarem a partir d'ell
		    self.insertWord(item, probe.getLeft())
		else: # si no té fill esquerre, l'insertem
		    probe.setLeft(Node(item,None,None,probe)) 
	    elif (item > probe.getVal()): # si el nou valor és major que el d'un node, ens fixem en la seva descendència dreta
		if (probe.getRight() != None): # si té fill dret, analitzarem a partir d'ell
		    self.insertWord(item, probe.getRight()) 
		else: # si no té fill dret, l'insertem
		    probe.setRight(Node(item,None,None,probe))
	    else: # valors iguals; ampliem les aparicions de la paraula, ja present a l'arbre, amb les coordenades al text de l'aparició actual
		probe.getVal().getCoords().append(item.getCoords())
	else: self.setRootVal(item)

    def findOcurrences(self, item, probe=None):
	'''cerca una paraula dins l'arbre mitjançant cerca binària: en cas de trobar-la, la mostra amb les seves coordenades'''
	if not probe:
	    probe = self.getRoot()
	if probe:	    
	    if (item < probe.getVal().getWord()):
		if (probe.getLeft() != None):
		    self.findOcurrences(item, probe.getLeft())
		return None
	    elif (item > probe.getVal().getWord()):
		if (probe.getRight() != None):
		    self.findOcurrences(item, probe.getRight())
		return None
	    # paraula trobada
	    print item, " : ", probe.getVal().getCoords()
	return None
    
    def doInOrden(self):
	'''desencadena el recorregut de mostra inorden sobre l'abre sencer, ja que s'indica l'arrel com a punt base de l'estructura a recórrer'''
	self.inOrden(self.getRoot())
    
    def inOrden(self, probe):
	'''recorregut inorden de l'arbre'''
	if not probe:
	    probe = self.getRoot()
	if probe:	
	    if(probe.getLeft()):
		self.inOrden(probe.getLeft())
	    self.visit(probe)
	    if(probe.getRight()):
		self.inOrden(probe.getRight())    
	    
    def calculateNodeAmountBelow(self, node): 
	''' retorna quants nodes hi ha per sota d'aquest pel camí mes llarg'''
	if not node:
	    return -1
	return max(self.calculateNodeAmountBelow(node.getLeft()), self.calculateNodeAmountBelow(node.getRight())) + 1
    
    def calculateDepth(self):
	'''calcula i retorna la profunditat o nombre de nivells de l'arbre'''
	return self.calculateNodeAmountBelow(self.getRoot()) + 1 # la profunditat ve donada pel nombre de nodes descendents de l'arrel pel camí més llarg (i més profund) sumant, a més, el nivell 1 del node arrel 
    
    def visit(self, node):
	'''mostra per pantalla del valor d'un node de l'arbre'''
        print node