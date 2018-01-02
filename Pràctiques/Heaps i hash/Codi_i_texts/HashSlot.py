# -*- coding: utf-8 -*-
class HashSlot(object):
    '''classe que representa una casella de la taula hash'''
    def __init__(self, key=-1, value=None):
        self._key = key
        self._values = []
        if value: self._values.append(value)
        
    def getKey(self):
        return self._key
    
    def getValues(self):
        return self._values
    
    def setKey(self, key):
        self._key = key
                
    def __str__(self):
        valuesText = ""
        for i in range(len(self._values)):
            valuesText += str(self._values[i])+", "
        return "key: {}; values: {}".format(self.getKey(), valuesText)