from TwoWayNode import *
from DoubleLinkedList import *

class CircularDoubleLinkedList(DoubleLinkedList):
    ''''llista doblement enllasada'''

    def __init__(self):
	DoubleLinkedList.__init__(self)
	
    def __str__(self):
	''' Imprimeix tots els nodes de la llista circular '''
	if (not(self._head)): 
	    return ''     
	res=""
	for item in self:
	    res+= str(item.getData()) + ", "
	return res
		    
    def initialize(self, until):
	''' Crea un array predeterminat de nodes on els valors son numeros de 1 a n '''
	for i in xrange(0, until):
	    self.insertFirst(until - i) 
	    
    def traverse(self):
	''' Recorre la llista enllasada circular imprimint els valors i enllasos '''
	probe = self._head
	i = 0
	while (i < len(self)):
	    print probe.getPrevious(), "<----", probe, " ----> ", probe.getNext()
	    probe = probe.getNext() 
	    i += 1	    
	    
    def find(self, targetItem):
	''' Busca item a la llista (per valor), per index ja tenim redefinit el __getitem__ '''
	i = 0
	probe = self._head
	while (i < len(self) and targetItem != probe.getData()):
	    probe = probe.getNext()
	    i += 1
	return (False if (i >= len(self)) else True)	  
    
    def insertFirst(self, data):
	''' Inserta un nou Node al principi '''
	if(not(self._head)):
	    self._head = TwoWayNode(data, self._tail, self._head)
	    self._tail = self._head
	    self._size += 1  
	else:
	    self._head = TwoWayNode(data, self._tail, self._head) # l'enllas apunta a l'anterior primer Node
	    self._head.getNext().setPrevious(self._head)
	    self._tail.setNext(self._head)
	    self._size += 1   
	    
    def insertLast(self, data):
	''' Inserta un Node al final, si l'array no cal iterar '''
	probe = self._head
	if (not(probe)):
	    self.insertFirst(data) # el efecto es el mismo ya que esta vacio
	else: 
	    probe = self._tail
	    probe.setNext(TwoWayNode(data, probe, probe.getNext())) # canvia l'enllas del penultim node per apuntar al nou al mateix temps que crea el nou Node
	    self._tail = probe.getNext()
	    self._head.setPrevious(self._tail)
	    self._size += 1	    
	
    def inserti(self, index, data):
	''' Inserta un Node en qualsevol posicio '''
	if (index <= 0 or (not(self._head))):
	    self.insertFirst(data)
	    return
	elif index >= len(self)-1:
	    self.insertLast(data)
	else: 
	    probe = self._head
	    while (probe.getNext() and index > 1):
		probe = probe.getNext()
		index -= 1
	    probe.setNext(TwoWayNode(data, probe, probe.getNext()))
	    probe.getNext().setPrevious(probe)
	    if probe.getNext().getNext():probe.getNext().getNext().setPrevious(probe.getNext())
	    self._size += 1 
    
    def removeFirst(self):
	''' Elimina el primer Node i el retorna '''
	if (not(self._head)):
	    return None
	res = self._head
	self._head = self._head.getNext()
	self._head.setPrevious(self._tail)
	self._tail.setNext(self._head)
	self._size -= 1
	return res  
    
    def removeLast(self):
	''' Elimina l'ultim Node i el retorna '''
	if (not(self._head)):
	    return None
	res = self._tail
	self._tail = self._tail.getPrevious()
	self._tail.setNext(self._head)
	self._head.setPrevious(self._tail)
	self._size -= 1
	return res     
    
    def removei(self, index):
	''' Esborra el node de la iessima posicio i retorna el seu valor '''
	if (index < 0 or index >= len(self) or not(self._head)):
	    removedItem = None # acabamos porque el indice no tiene sentido
	elif (index == 0):
	    return self.removeFirst()
	elif index == len(self)-1:
	    return self.removeLast()
	elif (not(self._head.getNext())):
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
	i=0
	while (i < len(self) and targetItem != probe.getData()):
	    probe = probe.getNext()
	    i += 1
	if (probe):
	    probe.setData(newItem)
	    return True
	return False
    
    def replaceAll(self, targetItem, newItem):
	''' Remplasa totes les coincidencies existents per un nou valor '''
	i = 0
	probe = self._head
	while (i < len(self)):
	    if(self[i].getData() == targetItem):
		self[i].setData(newItem)
	    i += 1
	
    def test2(self):
	#self.initialize(10)
	#self.traverse()
	self.insertFirst("pau")
	self.insertFirst("albert")
	self.insertFirst("pebrot")
	print self.find("pau")
	self.inserti(0,"epepe")
	self.insertLast("fora")
	self.traverse()
	'''
	print
	self.inserti(3,"pau")
	self.traverse()
	print
	self.replaceAll("epepe","CANVIAT")
	self.traverse()
	'''
	print
	self.removei(100)
	self.traverse()
	'''
	print
	self.insertLast("ULTIM")
	self.traverse()
	print
	self.inserti(len(self)/2, "MIDDLE")
	self.traverse()
	print
	self.removeFirst()
	self.traverse()
	print
	self.removeLast()
	self.traverse()
	print
	self.removei(1)
	self.traverse()
	print
	self.replace(1,"Rep")
	self.traverse()
	print
	self.replacei(6,"Rep")
	self.traverse()
	print
	self.replaceAll("Rep","Rerep")
	self.traverse()
	print
	print self
	'''
    
    # funcio de proves
    def test(self):
	print "\n{TEST DE CIRCULAR DOUBLE LINKED LIST}"
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
	
	
circdouble = CircularDoubleLinkedList()
circdouble.test()