class Node(object):
    '''classe d'objecte que compon un arbre'''
    def __init__(self, val = None, left = None, right = None, parent = None):
        '''constructor'''
        self._val = val
        self._left = left
        if self._left: self._left.setParent(self)
        self._right = right
        if self._right: self._right.setParent(self)
        self._parent = parent 
        '''parent representa el node pare; tenir-lo en compte facilita en gran mesura els canvis duts a terme en les rotacions de balanceig de l'arbre balancejat'''
        
    def getVal(self):
        return self._val
    
    def setVal(self, item):
        self._val = item
        
    def getLeft(self):
        return self._left
   
    def getRight(self):
        return self._right
    
    def setLeft(self, node):
        self._left = node
        
    def setRight(self, node):
        self._right = node
        
    def getParent(self):
        return self._parent
    
    def setParent(self, node):
        self._parent = node
        
    def __str__(self):
        return str(self._val)