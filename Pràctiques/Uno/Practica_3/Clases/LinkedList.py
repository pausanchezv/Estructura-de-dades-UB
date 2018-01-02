from Node import *

class LinkedList(object):
      
    def __init__(self):
        self._head = None
	self._size = 0
	
    ##############################
    #### Metodes sobreescrits ####
    ##############################
	
    def __len__(self):
	''' Retorna el length de la llista de Nodes '''
	return self._size
    
    def __str__(self):
	''' Imprimeix la llista de nodes sencera '''
	probe = self._head
	res = ""
	while (probe):
	    res += str(probe) + ", "
	    probe = probe.getNext()
	return res
    
    def __getitem__(self, index):
	''' Retorna un item de la llista '''
	if ((index > len(self) - 1) or (index < 0)):
	    return None
	probe = self._head
	while (index and probe.getNext()):
	    probe = probe.getNext()
	    index -= 1
	return (probe if(not(index)) else None)
    
    def __setitem__(self, index, item):
	''' Canvia el valor d'un Node '''
	self[index].setData(item)
	
    def __iter__(self):
	''' Permet iterar sobre la llista de Nodes '''
	i = 0
	while (i < len(self)):
	    yield self[i]
	    i += 1
    
    #######################################
    ### Metodes per gestionar la classe ###  
    #######################################
    
    # comprueba si esta vacia la lista
    def isEmpty(self):
	return len(self) == 0
    
    # retorna todos los elementos contenidos como datos en los nodos de la lista (para la lista de jugadores de ONE)
    def get_items(self):
	items = []
	probe = self._head
	for i in range(len(self)):
	    items.append(probe.getData())
	    probe = probe.getNext()
	return items
	
    
    def initialize(self, until):
	''' Crea un array predeterminat de nodes on els valors son numeros de 1 a n '''
	for i in xrange(0, until):
	    self._head = Node((until - i), self._head) # el __head sera el primer Node de l'array
	    self._size += 1
            
    def getHead(self):
	''' Retorna el Node de capcelera'''
        return self._head
    
    def traverse(self):
	''' Recorre la llista enllasada imprimint els valors i enllasos '''
	probe = self._head
	while (probe):
	    print probe, " ----> ", probe.getNext()
	    probe = probe.getNext()
	    
    def find(self, targetItem):
	''' Busca item a la llista (per valor), per index ja tenim redefinit el __getitem__'''
	probe = self._head
	while (probe and targetItem != probe.getData()):
	    probe = probe.getNext()
        return (False if (not(probe)) else True)
    
    
    def replace(self, targetItem, newItem):
	''' Remplasa un valor existent per un de nou (busca per valor no per index) i nomes la primera coincidencia '''
	probe = self._head
	while (probe and targetItem != probe.getData()):
	    probe = probe.getNext()
	if (probe):
	    probe.setData(newItem)
	    return True
	return False
    
    def replaceAll(self, targetItem, newItem):
	''' Remplasa totes les coincidencies existents per un nou valor '''
	probe = self._head
	while (probe):
	    if (probe and probe.getData() == targetItem):
		probe.setData(newItem)
	    probe = probe.getNext()
  
    def replacei(self, index, newItem):
	''' Remplasa un item buscant per l'index i no pel valor '''
	index -= 1
	if (index < -1 or index >= len(self)):
	    return False
	probe = self._head
	while (probe and index >= 0):
	    probe = probe.getNext()
	    index -= 1
	if (index < 0):
	    probe.setData(newItem)
	    return True
	return False
    
    def insertFirst(self, data):
	''' Inserta un nou Node al principi '''
	self._head = Node(data, self._head) # l'enllas apunta a l'anterior primer Node
	self._size += 1
    
    def insertLast(self, data):
	''' Inserta un Node al final, si l'array no cal iterar '''

	probe = self._head
	if (not(probe)):
	    self.insertFirst(data) # Si l'array esta buit inserta el Node
	else: 
	    while (probe.getNext()):
		probe = probe.getNext() 
	    probe.setNext(Node(data)) # canvia l'enllas del penultim node per apuntar al nou al mateix temps que crea el nou Node
	    self._size += 1
	
    def inserti(self, index, data):
	''' Inserta un Node en qualsevol posicio '''
	if (index == 0):
	    self.insertFirst(data)
	    return
	if ((not(self._head)) or index < 0):  			          
	    self._head = Node(data)
	else: 
	    probe = self._head
	    while (probe.getNext() and index > 1):
		probe = probe.getNext()
		index -= 1
	    probe.setNext(Node(data,probe.getNext()))
	    self._size += 1
    
    def removeFirst(self):
	''' Elimina el primer Node i retorna el seu valor '''
	if (not(self._head)):
	    return None
	res = self._head.getData()
	self._head = self._head.getNext()
	self._size -= 1
	return res   
    
    def removeLast(self):
	''' Borra el Node del final de l'array i retorna el seu valor '''
	if (not(self._head)): 
	    return None
	if (not(self._head.getNext())): 
	    res, self._head = self._head.geData(), None
	else: 
	    probe = self._head
	    while (probe.getNext().getNext()): # han d'existir dos Nodes mes enlla
		probe = probe.getNext() # llavors ja tenim l'element que volem eliminar
	    res = probe.getNext().getData()
	    probe.setNext(None) # i el deixem sense enllas
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
	    self._size -= 1
	    return removedItem
    
    # funcio de proves
    def test(self):
	print "\n{TEST DE LINKED LIST}"
	print ("Tenemos una lista enlazada con varios elementos.")
	self.inserti(0,"seeeerti")
	self.inserti(1,[1,2,3,4])
	self.insertLast("pau")
	self.insertLast("pau")
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
	print self
	print ("Insertamos un elemento al principio, otro al final y otro en medio:")
	self.insertFirst("primero")
	self.insertLast("ultimo")
	self.inserti(len(self)/2, "medio")
	print self, "\n"

	
	

linkedList = LinkedList()
linkedList.test()


