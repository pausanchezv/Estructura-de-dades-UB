from LinkedQueue import *

class LinkedPriorityQueue(LinkedQueue):    
    """ PriorityQueue inherits from a queue, but inserts the elements in order, by default ascending """        
    
    def __init__(self):        
        LinkedQueue.__init__(self)
        

    def enqueue(self, item):
        if (self.isEmpty() or (item <= self[0].getData())):
            self.inserti(0, item)
        else:
            inserted, i = False, 0              
            while i < (len(self) - 1) and (not(inserted)):                
                if (self[i].getData() < item and item <= self[i+1].getData()): 
                    self.inserti(i + 1, item)
                    inserted = True  
                i += 1             
            if (not(inserted)):
                self.inserti(len(self), item)
                
    def test(self): 
        print "{TEST DE LINKED PRIORITY QUEUE}"        
        self.enqueue(111)
        self.enqueue(333)
        self.enqueue(222)
        self.enqueue(555)
        print ("Tenemos una cola de prioridad con los siguientes elementos: {}").format(self)
        num1, num2 = 999, 888
        print ("Anyadimos, por este orden, los numeros {} y {}.").format(num1,num2)
        self.enqueue(num1)
        self.enqueue(num2)
        print ("La cola de prioridad los ordena, y queda con esta disposicion: {}").format(self)
        self.dequeue()
        print ("Quitamos el primer elemento (first out) y queda asi: {}\n").format(self)
        

# test de LinkedPriotyQueue
priority_queue = LinkedPriorityQueue()
priority_queue.test()