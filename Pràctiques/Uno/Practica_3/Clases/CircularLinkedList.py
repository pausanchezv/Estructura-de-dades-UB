from Node import *
from LinkedList import *

class CircularLinkedList(LinkedList):
  
  def __init__(self):
    LinkedList.__init__(self)
    self._tail = None

      
  ##############################
  #### Metodes sobreescrits ####
  ##############################  
  
  
  def __str__(self):
      ''' Imprimeix tots els nodes de la llista circular '''
      if (not(self._head)): 
          return ''     
      res=""
      for item in self:
	res+= str(item.getData()) + ", "
      return res
    
    
  def getTail(self):
    ''' Retorna el Node final'''
    return self._tail
  
  #######################################
  ### Metodes per gestionar la classe ###  
  #######################################
  
  def initialize(self, until):
    ''' Crea un array predeterminat de nodes on els valors son numeros de 1 a n '''
    for i in xrange(0, until):
	self.insertFirst(until - i) 
    
  def insertFirst(self, data):
      ''' Inserta un Node al principi de la llista circular '''
      if self._head == None:
	self._head = Node(data,self._head)
	self._tail = self._head              
	self._head.setNext(self._head)       
      else:
	self._head = Node(data,self._head.getNext())
	self._tail.setNext(self._head)
	
      self._size += 1
                  

      
   
      
  def insertLast(self, data):
      ''' Inserta un node al final de la llista circular '''
      self.inserti(len(self), data)
      

	       
  
  def traverse(self):
      ''' Recorre la llista enllasada circular imprimint els valors i enllasos '''
      probe = self._head
      i = 0
      while (i < len(self)):
	  print probe, " ----> ", probe.getNext()
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
  
  def removeFirst(self):
      ''' Elimina el primer Node i el retorna '''
      if (not(self._head)):
	  return None
      res = self._head
      self._head = self._head.getNext()
      self._size -= 1
      return res
    
  def removei(self, index):
      ''' Esborra el node de la iessima posicio i retorna el seu valor '''
      if (index == 0):
	  return self.removeFirst()
      if (not(self._head)):
	  removedItem = None
      else: 
	  probe = self[index - 1]
	  removedItem = probe.getNext().getData()
	  probe.setNext(probe.getNext().getNext())
	  self._size -= 1
	  return removedItem
	
  def removeLast(self):
      ''' Esborra el Node de la ultima posicio i en retorna el valor '''
      return self.removei(len(self) - 1)
    
  def replace(self, targetItem, newItem):
      ''' Remplasa un valor existent per un de nou (busca per valor no per index) i nomes la primera coincidencia '''
      i = 0
      probe = self._head
      while (i < len(self)):
          if(self[i].getData() == targetItem):
	      self[i].setData(newItem)
	      return True
	  i += 1
      return False 
    
  def replaceAll(self, targetItem, newItem):
      ''' Remplasa totes les coincidencies existents per un nou valor '''
      i = 0
      probe = self._head
      while (i < len(self)):
	  if(self[i].getData() == targetItem):
	      self[i].setData(newItem)
	  i += 1
	  
  def replace(self, index, newItem):
      ''' Remplasa un valor existent buscant per index '''
      if(index < 0 or index > len(self) - 1):
	    return False
      self[index].setData(newItem)
      return True
	
  
  
  # funcio de proves
  def test(self):
      print "{TEST DE CIRCULAR LINKED LIST}"
      print ("Tenemos una lista enlazada con varios elementos.")
      self.inserti(0,"hola")
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
      self.inserti(len(self)/2, "medio")      
      self.insertLast("ultimo")
      print self
      
      
      
circular = CircularLinkedList()
circular.test()
