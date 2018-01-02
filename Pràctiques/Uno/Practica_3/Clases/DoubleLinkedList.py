from TwoWayNode import *
from LinkedList import *

class DoubleLinkedList(LinkedList):

    def __init__(self):
	LinkedList.__init__(self)
        self._tail = None

    
    #######################################
    ### Metodes per gestionar la classe ###  
    #######################################    
	    
    def initialize(self,until):
	'''Add X twowaynodes to the linked structure'''
	self._head=TwoWayNode(0)
	self._tail=self._head
	self._size += 1

	for count in xrange(1, until):
	    self._tail.setNext(TwoWayNode(count, self._tail))
	    self._tail = self._tail.getNext()
	    self._size += 1
		
	    
    def traverse(self):
	''' Recorre la llista enllasada imprimint els valors i enllasos '''
	probe = self._head
	while (probe):
	    print probe.getPrevious()," <---- ", probe, " ----> ", probe.getNext()
	    probe = probe.getNext()
    
    
    def find(self, targetItem):
	''' Busca item a la llista (per valor), per index ja tenim redefinit el __getitem__'''
	probe = self._head
	while (probe and (targetItem != probe.getData())):
	    probe = probe.getNext()
	return (False if (not(probe)) else True)     
	
    def insertFirst(self, data):
	''' Inserta un nou Node al principi '''
	if(not(self._head)):
	    self._head = TwoWayNode(data, None, self._head) 
	else:
	    self._head = TwoWayNode(data, None, self._head) # l'enllas apunta a l'anterior primer Node
	    self._head.getNext().setPrevious(self._head)
	    self._size += 1
	
    def insertLast(self, data):
	''' Inserta un Node al final, si l'array no cal iterar '''
	probe = self._head
	if (not(probe)):
	    probe = TwoWayNode(data) # Si l'array esta buit inserta el Node
	else: 
	    while (probe.getNext()):
		probe = probe.getNext()
	    probe.setNext(TwoWayNode(data, probe)) # canvia l'enllas del penultim node per apuntar al nou al mateix temps que crea el nou Node
	self._size += 1
	
    def inserti(self, index, data):
	''' Inserta un Node en qualsevol posicio '''
	if (index == 0):
	    self.insertFirst(data)
	    self._size += 1
	    return
	if ((not(self._head)) or index < 0):  			          
	    self._head = TwoWayNode(data)
	else: 
	    probe = self._head
	    while (probe.getNext() and index > 1):
		probe = probe.getNext()
		index -= 1
	    probe.setNext(TwoWayNode(data, probe, probe.getNext()))
	    probe.getNext().setPrevious(probe)
	    #probe.getNext().getNext().setPrevious(probe.getNext())
	    self._size += 1
	    
    def removeFirst(self):
	''' Elimina el primer Node i retorna el seu valor '''
	if (not(self._head)):
	    return None
	res = self._head.getData()
	self._head = self._head.getNext()
	self._head.setPrevious(None)
	self._size -= 1
	return res     
    
    def removei(self, index):
	''' Esborra el node de la iessima posicio i retorna el seu valor '''
	if (index == 0):
	    return self.removeFirst()
	if (not(self._head)):
	    removedItem = None
	elif (index <= 0 or not(self._head.getNext())):
	    removedItem = self._head.getData()
	    self._head = None
	else: 
	    probe = self._head
	    while (probe.getNext().getNext() != None and index > 1):
		probe = probe.getNext()
		index -= 1
	    removedItem=probe.getNext().getData()
	    probe.setNext(probe.getNext().getNext())
	    probe.getNext().setPrevious(probe)
	    self._size -= 1
	    return removedItem    
    
    def replace(self, targetItem, newItem):
	''' Remplasa un valor existent per un de nou (busca per valor no per index) i nomes la primera coincidencia '''
	probe = self._head
	while (probe and targetItem != probe.getData()):
	    probe = probe.getNext()
	if (probe):
	    probe.setData(newItem)
	    return True
	return False
    
    
    # funcio de proves
    def test(self):
	print "\n{TEST DE DOUBLE LINKED LIST}"
	print ("Tenemos una lista enlazada con varios elementos.")
	self.inserti(0,"seeeerti")
	self.inserti(1,[1,2,3,4])
	self.insertLast("fff")
	self.insertLast("pau")
	print self
	print ("La lista enlazada tiene estos nodos:\n{}").format(self)
	print ("La longitud de la lista es {}").format(len(self))
	elem_name = "pau"
	print ("Esta el elemento {} en la lista? {}").format(elem_name, self.find(elem_name))
	print ("Cual es el primer elemento? {}").format(self.getHead())
	self.replacei(0, "nou")
	print ("Ahora lo hemos cambiado por este: {}").format(self.getHead())
	elem = [1,2,3,4]
	self.replace(elem, "canviat")
	print ("Ahora cambiamos el segundo elemento: {}").format(self[1])
	elem1, elem2 = "pau", "albert"
	self.replaceAll(elem1, elem2)
	print ("Hemos remplazado {} por {} en todas sus apariciones.\nAhora la lista tiene este aspecto:").format(elem1,elem2)
	self.traverse()
	print ("Recorremos la lista para remplazar todos los elementos:")
	for elemento in self:
	    elemento.setData("remplazado")
	print self, len(self)
	print ("Insertamos un elemento al principio, otro al final y otro en medio:")
	self.insertFirst("primero")
	self.insertLast("ultimo")
	self.inserti(len(self)/2, "medio")
	print self, "\n"
	
	

d = DoubleLinkedList()
d.test()

