 # -*- coding: utf-8 -*-
from BTree import *
import time
from TextWord import *


class BTreeWordFinder(object):
    '''classe per fer cerca binària amb arbres binaris'''
    def __init__(self, file, tree = None):
        '''Metode constructor'''
        self.bTree = None
        if not tree:
            self._bTree = BTree()
        else: self._bTree = tree
        self.appendText(file)    
      
    def getBTree(self):
        return self._bTree
        
    def viewIndex(self):
        ''' Mostra les paraules alfabèticament amb les seves aparicions'''
        print u"\nL'organització alfabètica de les paraules de l'arbre és la següent:"
        self.getBTree().doInOrden()
                     
    def appendText(self, file):
        '''Llegeix el fitxer i el desglossa en línies i paraules per línia'''
        try:
            with open(file, 'r') as reader:
                numLine = 1
                t1 = time.clock()
                for line in reader.readlines():
                    numWord = 1
                    if (line):
                        for word in line.split():
                            item = word.lower()
                            self.getBTree().insertWord(TextWord(item, numLine, numWord))
                            numWord += 1
                    numLine += 1
                t2 = time.clock()
                print u"\nS'han insertat les paraules del text a l'arbre. El temps d'inserció ha estat de {} ms.".format((t2-t1)*1000)
        except IOError: print "El nom de l'arxiu donat no existeix."
 
    def findOcurrencesInFile(self, file):
        '''mostra les aparicions de les paraules d'un text en l'arbre'''
        try:
            print u"\nLes aparicions de paraules de {} en l'arbre són:".format(file)
            t1 = time.clock() 
            with open(file, 'r') as reader:
                for word in reader.read().split():
                    item = word.lower()
                    self.getBTree().findOcurrences(item)
            t2 = time.clock()
            print "El temps de cerca ha estat de {} ms.".format((t2-t1)*1000)
        except IOError: print "El nom de l'arxiu donat no existeix."          
        
    def showDepth(self):
        '''mostra la profunditat de l'arbre'''
        print u"\nLa profunditat de l'arbre és de {} nivells.".format(self.getBTree().calculateDepth())
       
    @staticmethod
    def askFile():
        ''' demana un arxiu'''
        file = raw_input ("Entra el nom d'un fitxer (Ex: smallText.txt) --> ")
        return file
    
    @staticmethod
    def main():
        '''mètode principal de l'aplicació. Crea el cercador, demana a l'usuari el nom d'un text i en ell cerca i mostra les paraules d'un diccionari trobades, a més de mostrar ordenades alfabèticament les paraules del text i la profunditat de l'arbre'''
        b = BTreeWordFinder(BTreeWordFinder.askFile())
        b.findOcurrencesInFile('dictionary.txt')
        b.viewIndex()
        b.showDepth()    

if __name__ == "__main__":
    BTreeWordFinder.main()