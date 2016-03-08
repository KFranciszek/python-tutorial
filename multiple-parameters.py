def list(*food):
	print food

list('apples')
print list
list('apples','peaches','beef')
print list

def profile(name, *ages): # drugi parametr przyjmuje sie jako tupla 
	print name
	print ages
	
	print sorted(ages)


profile('bucky', 42,43,75,98,54)

zarcie = ['zupa','kupa','ziom']

print zarcie 

zarcie.sort()

print zarcie