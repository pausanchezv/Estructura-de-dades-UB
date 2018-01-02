 # -*- coding: utf-8 -*-
from BTree import *
import copy


class BalancedBTree(BTree):
    '''arbre binari que es balanceja si cal quan esdevé actualitzat'''
    def __init__(self, val = None, left = None, right = None):
        BTree.__init__(self, val, left, right)
	
	
    def calculateBFactor(self,node):
	''' calcula el factor de balanceig d'un node'''
	return self.calculateNodeAmountBelow(node.getLeft()) - self.calculateNodeAmountBelow(node.getRight())
    
    def insertWord(self, item, probe=None):
	'''inserta un paraula, amb l'afegit que després de fer-ho comprova si cal modificar l'estructura de l'arbre tot balancejant-lo'''
	if not probe:
	    probe = self.getRoot()
	if probe:	    
	    if (item < probe.getVal()):
		if (probe.getLeft() != None):
		    self.insertWord(item, probe.getLeft())
		else:
		    probe.setLeft(Node(item,None,None,probe))
		    self.updateBalance(probe) # hem insertat; revisem si cal balancejar
	    elif (item > probe.getVal()):
		if (probe.getRight() != None):
		    self.insertWord(item, probe.getRight())
		else:
		    probe.setRight(Node(item,None,None,probe))
		    self.updateBalance(probe) # hem insertat; revisem si cal balancejar
	    else: # iguals
		probe.getVal().getCoords().append(item.getCoords())
	else: self.setRootVal(item)	
		
    def updateBalance(self,node):
	'''comprova, partint del node insertat i cap amunt, si cal fins l'arrel, si hi ha descompensació de balanceig i per tant cal balancejar'''
	# el procediment és com segueix: inicialment s'arriba a aquesta funció amb el node pare de l'últim node insertat com a paràmetre, i s'analitza el factor de balanç d'aquest pare; recursivament es va comprovant el factor de balanç del node pare de l'anterior fins que s'arriba a l'arrel (l'únic node sense pare) o bé es troba un desequilibri en el balanç i es condueix a balancejar l'arbre amb les rotacions prenent el node on s'ha detectat la descompensació com a punt de partida per a aquestes
	bfactor = self.calculateBFactor(node) 
	if bfactor >= 2 or bfactor <= -2:
	    self.balance(node)
	elif node.getParent():
	    if self.calculateBFactor(node.getParent()) != 0:
		    self.updateBalance(node.getParent())
    
    def balance(self, node):
	'''condueix a les rotacions del balanceig, segons hi hagi cas intern (iniciant per dreta o esquerra) o extern (per dreta o esquerra)'''
	if node:
	    if self.calculateBFactor(node) <= -2: 
		if self.calculateBFactor(node.getRight()) > 0: # cas intern que comença rotant cap a la dreta
		    self.redistributeToRight(node.getRight())
		    self.redistributeToLeft(node)
		else:
		    self.redistributeToLeft(node) # cas extern en què es rota cap a l'esquerra
	    elif self.calculateBFactor(node) >= 2:
		if self.calculateBFactor(node.getLeft()) < 0: # cas intern que comença rotant cap a l'esquerra
		    self.redistributeToLeft(node.getLeft())
		    self.redistributeToRight(node)
		else:
		    self.redistributeToRight(node) # cas intern en què es rota cap a l'esquerra	
   
    def redistributeToLeft(self,node):
	'''reajustament cap a l'esquerra de posicions de nodes per a balancejar'''
	newRoot = node.getRight()
	node.setRight(newRoot.getLeft())
	if newRoot.getLeft():
	    newRoot.getLeft().setParent(node)
	newRoot.setParent(node.getParent())
	if not node.getParent():
	    self.setRoot(newRoot)
	else:
	    if node.getParent() and (node is node.getParent().getLeft()):
		node.getParent().setLeft(newRoot)
	    else:
		node.getParent().setRight(newRoot)
	newRoot.setLeft(node)
	node.setParent(newRoot)
   
    def redistributeToRight(self, node):
	'''reajustament cap a la dreta de posicions de nodes per a balancejar'''
	newRoot = node.getLeft()
	node.setLeft(newRoot.getRight())
	if newRoot.getRight():
	    newRoot.getRight().setParent(node)
	newRoot.setParent(node.getParent())
	if not node.getParent():
	    self.setRoot(newRoot)
	else:
	    if node.getParent() and (node is node.getParent().getRight()):
		node.getParent().setRight(newRoot)
	    else:
		node.getParent().setLeft(newRoot)
	newRoot.setRight(node)
	node.setParent(newRoot)