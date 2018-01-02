 # -*- coding: utf-8 -*-

from Heap import *
from TextWord import *
import time

class HeapWordFinder(object):
    '''classe per fer cerca binària amb heaps'''
    def __init__(self, file):
        '''Metode constructor'''
        self._heap = Heap()
        self.appendText(file)
         
    def getHeap(self):
        return self._heap
        
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
                            self._heap.insertWord(TextWord(item, numLine, numWord))
                            numWord += 1
                    numLine += 1
                    t2 = time.clock()
                print u"\nS'han insertat les paraules del text al heap. El temps d'inserció ha estat de {} ms.".format((t2-t1)*1000)
        except IOError: print "El nom de l'arxiu donat no existeix."
        
    def viewIndex(self):
        '''Mostra les paraules alfabèticament amb les seves aparicions'''
        print u"\nL'organització alfabètica de les paraules del heap és la següent:"
        words = []
        for textWord in self.getHeap().getSortedList():
            print textWord
          
    def findOcurrencesInFile(self, file):
        '''mostra les aparicions de les paraules d'un text en el heap'''
        try:
            print u"\nLes aparicions de paraules de {} al heap són:".format(file)
            t1 = time.clock() 
            with open(file, 'r') as reader:
                for word in reader.read().split():
                    item = word.lower()
                    self.getHeap().findOcurrences(item)
            t2 = time.clock()
            print "El temps de cerca ha estat de {} ms.".format((t2-t1)*1000)
        except IOError: print "El nom de l'arxiu donat no existeix."
        
    def showDepth(self):
        '''mostra la profunditat del heap'''
        print u"\nLa profunditat del heap és de {} nivells.".format(self.getHeap().calculateDepth())
        
    @staticmethod
    def askFile():
        '''demana un arxiu'''
        file = raw_input ("Entra el nom d'un fitxer (Ex: smallText.txt) --> ")
        return file  
    
    @staticmethod
    def main():
        '''mètode principal de l'aplicació. Crea el cercador, demana a l'usuari el nom d'un text i en ell cerca i mostra les paraules d'un diccionari trobades, a més de mostrar ordenades alfabèticament les paraules del text i la profunditat del heap'''
        h = HeapWordFinder(HeapWordFinder.askFile())
        h.showDepth()   
        h.getHeap().heapSort() # associem al heap una llista ordenada dels seus elements
        h.findOcurrencesInFile('dictionary.txt')
        h.viewIndex() 

if __name__ == "__main__":
    HeapWordFinder.main()