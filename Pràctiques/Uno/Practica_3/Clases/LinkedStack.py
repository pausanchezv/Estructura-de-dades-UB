# autors: Pau Sanchez Valdivieso y Albert Espin Roman

from LinkedList import *

class LinkedStack(LinkedList):
    ''' Define a TDA stack '''
    
    def __init__(self):
        LinkedList.__init__(self)
    
    def push(self, item):
        self.insertLast(item)
        
    def pop(self):
        return self.removeLast()
    
    def peek(self):
        return self.get_items()[len(self) - 1] if len(self) else None
    
    def test(self):
        print "{TEST DE LINKED STACK}"
        self.push(2)
        self.push("Pau")
        self.traverse()
        print ("Anyadimos varios elementos a una pila: {}").format(self)
        print ("El ultimo elemento es: {}").format(self.peek())
        self.pop()
        print ("Sacamos el ultimo elemento y la pila queda asi: {}\n").format(self)
 
# test de LinkedStack
stack = LinkedStack()
stack.test()