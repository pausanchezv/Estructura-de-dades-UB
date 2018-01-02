# autores: Pau Sanchez Valdivieso y Albert Espin Roman

class Time(object):
    def __init__ (self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    # setters y getters    
    def getHour(self):
        return self.hour
    
    def setHour(self, hour):
        self.hour = hour
    
    def getMinute(self):
        return self.minute
    
    def setMinute(self,minute):
        self.minute = minute
        
    def getSecond(self):
        return self.second
        
    def setSecond(self,second):
        self.second = second
	
    # otras funciones 
    
    # muestra el tiempo en formato estandar
    def print_time(self):
	print ("{s.hour}:{s.minute}:{s.second}").format(s = self)
    
    # incrementa el tiempo unos dados segundos    
    def increment(self, seconds):
	self.setSecond(self.getSecond() + seconds)
	while self.getSecond() >= 60:
	    self.setSecond(self.getSecond() - 60)
	    self.setMinute(self.getMinute() + 1)
	while self.getMinute() >= 60:
	    self.setMinute(self.getMinute() - 60)
	    self.setHour(self.getHour() + 1)
    
    # convertir tiempo a segundos
    def time_to_int(self):
	self.minutes = self.hour * 60 + self.minute
	self.seconds = self.minutes * 60 + self.second # recuperamos los datos del objeto con self
	return self.seconds

    # sumar a un tiempo otro
    def add_time(self, t2): #t1, t2 objetos de tipo Time
	sum = Time()
	sum.setHour(self.getHour() + t2.getHour()) 
	sum.setMinute(self.getMinute() + t2.getMinute())
	sum.setSecond(self.getSecond() + t2.getSecond())
	if sum.getSecond() >= 60:
	    sum.setSecond(sum.getSecond() - 60)
	    sum.setMinute(sum.getMinute() + 1)
	if sum.getMinute() >= 60:
	    sum.setMinute(sum.getMinute() - 60)
	    sum.setHour(sum.getHour() + 1)
	return sum
     
    # indica si el tiempo del objeto propio es posterior a otro    
    def is_after(self, other):
	return self.time_to_int() > other.time_to_int()    
        
def ej1(): # funcion global
    t1=Time(22,15,55) # se crea un objeto Time, t1, inicializando sus atributos mediante el constructor definido
    t1.print_time() # muestra los atributos del objecto t1, mostrado separado por ":" como un tiempo
    t2=Time(1,22,34) # se crea un objeto Time, t2, inicializando sus atributos mediante el constructor definido
    t2.print_time() # muestra los atributos del objecto t1, mostrado separado por ":" como un tiempo
    t1.add_time(t2).print_time() # muestra el tiempo t1 una vez se ha incrementado con el valor del tiempo t2
    t1.increment(1000) # incrementa el valor de t1 en 1000 segundos, distribuidos 
    #segun el convenio de segundos, minutos y horas
    t1.print_time() # muestra el valor de t1 una vez incrementado
	
    
ej1() # llamada a la funcion