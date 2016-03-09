class className:
	def createName(self,name):# metotdy nazywamy self, bo pozniej nie wiemy jak bedzie nazywac sie obiekt

		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print "hello %s" % self.name


print className


first=className()

second=className()

first.createName('bucky')

second.createName('tony')

print first.displayName()

first.saying()

print first.name # sywietla bucky bo metoda self przyjmuje wartosc first 
