 # -*- coding: utf-8 -*-

class TextWord():
    '''classe que representa una paraula de text, formada per dos elements: la paraula en si (un String) i una llista de tuples que simbolitzen les aparicions al text d'aquesta paraula; cada tupla compta amb dues coordenades: la línia on s'ha trobat la paraula i la posició en aquesta'''
    
    def __init__(self, word, line, position):
        '''constructor'''
        self._word = word
        self._coords = [(line,position)]
    
    def getWord(self):
        return self._word
    
    def getCoords(self):
        return self._coords
    
    def __str__(self):
        return ("{} : {}").format(self._word,self._coords)
    
    def __cmp__(self,other):
        '''mètode de comparació sobrecarregat; permet comparar dues paraules de text, amb la particularitat que es comparen els seus Strings (cosa que, internament, comporta la comparació dels valors ASCII dels seus caràcters)'''
        if self.getWord() > other.getWord(): return 1
        elif self.getWord() < other.getWord(): return -1
        else: return 0