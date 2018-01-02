from HashMap import *
import time 
class HashMapWordFinder(object):
    def __init__(self, file):
        '''Mètode constructor'''
        self._hashMap = HashMap()
        self.appendText(file)
        
    def appendText(self, file):
        '''Llegeix el fitxer i el desglossa en lí­nies i paraules per lí­nia'''
        try:
            with open(file, 'r') as reader:
                numLine = 1
                t1 = time.clock()
                array = []
                for line in reader.readlines():
                    numWord = 1
                    if (line):
                        for word in line.split():
                            item = word.lower()
                            array.append(item)
                            numWord += 1
                    numLine += 1
                self._hashMap.prepareTable(HashMapWordFinder.nextPrime(len(array)))
                for item in array:
                    self._hashMap.insertWord(TextWord(item, numLine, numWord))
                t2 = time.clock()
                print u"\nS'han insertat les paraules del text a la taula hash. El temps d'inserció ha estat de {} ms.".format((t2-t1)*1000)
        except IOError: print "El nom de l'arxiu donat no existeix."
 
    def findOcurrencesInFile(self, file):
        '''mostra les aparicions de les paraules d'un text en la taula hash'''
        try:
            print u"\nLes aparicions de paraules de {} a la taula hash són:".format(file)
            t1 = time.clock() 
            with open(file, 'r') as reader:
                for word in reader.read().split():
                    item = word.lower()
                    self._hashMap.findOcurrences(item)
            t2 = time.clock()
            print "El temps de cerca ha estat de {} ms.".format((t2-t1)*1000)
        except IOError: print "El nom de l'arxiu donat no existeix."
        
    def showHashData(self):
        '''mostra el nombre de col·lisions de la taula hash, quants elements té la cel·la amb més elements i el percentatge de cel·les buides'''
        print u"\nEl nombre de col·lisions ha estat de", self._hashMap.getCollisionAmount()
        print u"El nombre d'elements en la cel·la de més elements és de", self._hashMap.getMaxElemAmountInSlot()
        print u"El percentatge de cel·les buides és de", self._hashMap.calcEmptyPercentage()
        
    @staticmethod
    def askFile():
        ''' demana un arxiu'''
        file = raw_input ("Entra el nom d'un fitxer (Ex: smallText.txt) --> ")
        return file  
    
    @staticmethod
    def main():
        '''mètode principal de l'aplicació. Crea el cercador, demana a l'usuari el nom d'un text i en ell cerca i mostra les paraules d'un diccionari trobades, a més de mostrar ordenades alfabèticament les paraules i mostrar certes dades de la taula hash'''
        h = HashMapWordFinder(HashMapWordFinder.askFile())  
        h.findOcurrencesInFile('dictionary.txt')
        h.showHashData()
      
    @staticmethod    
    def isPrime(n):
        '''retorna si un nombre és primer'''
        return not any(n % i == 0 for i in range(2, n))
    
    @staticmethod
    def nextPrime(n):
        '''retorna el primer nombre primer a partir del número indicat'''
        found = False
        result = 0
        while not found:
            if HashMapWordFinder.isPrime(n): 
                found = True
            else: n += 1
        return n    

if __name__ == "__main__":
    HashMapWordFinder.main()