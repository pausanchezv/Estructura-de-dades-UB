 # -*- coding: utf-8 -*-

from BalancedBTree import *
from BTreeWordFinder import *

class BalancedBTreeWordFinder(BTreeWordFinder):
    '''classe de cerca binària implementada amb un arbre binari balancejat; hereta de BTreeWordFinder i aprofita així els seus mètodes'''
    def __init__(self, file, btree=None):
        '''Metode constructor'''
        BTreeWordFinder.__init__(self, file, btree) 
     
    @staticmethod 
    def main():
        '''versió de mètode principal de la classe per al cercador implementat amb un arbre balancejat'''
        b = BalancedBTreeWordFinder(BalancedBTreeWordFinder.askFile(), BalancedBTree())
        b.findOcurrencesInFile('dictionary.txt')
        b.viewIndex()
        b.showDepth()
    
BalancedBTreeWordFinder.main()