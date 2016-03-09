class parentClass:
	var1="i am var1"
	var2="i am var2"


class childClass(parentClass): # klasa dziecko dziedziczy klase rodzica

	pass

parentObject=parentClass()

print parentObject.var1

childObject=childClass()

print childObject.var1

print childObject.var2
