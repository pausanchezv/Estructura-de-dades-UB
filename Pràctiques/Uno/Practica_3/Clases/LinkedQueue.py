from LinkedList import *
class LinkedQueue(LinkedList):    
    ''' Define a TDA Queque ''' 

    def __init__(self):        
        LinkedList.__init__(self)
        
    
    def enqueue(self, item):        
        self.insertLast(item)
        
    def dequeue(self):      
        return self.removeFirst()
    
    
    def test(self):
        print "{TEST DE LINKED QUEUE}"
        self.enqueue(1)
        self.enqueue(["hola", "test"])
        print ("Anyadimos diveros elementos a una cola vacia: {}").format(self)
        self.enqueue(True)
        print ("Hemos anyadido un elemento (first in); esta es ahora la cola: {}").format(self)
        self.dequeue()
        print ("Ahora eliminamos un elemento, que por ser pila exige ser el primero\n(first out); ahora la cola es esta: {}\n").format(self)

# test de LinkedQueue
queue = LinkedQueue()
queue.test()