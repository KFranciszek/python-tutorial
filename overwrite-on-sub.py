class parent:
	var1="bacon"
	var2="snausage"


class child(parent):
	var2="toast"

pob=parent()
cob=child()

print pob.var1
print pob.var2

print cob.var1
print cob.var2

class Mom:
	var1="hey im mom"

class Dad:
	var2="hey there son im a dad"


class child(Mom,Dad):
	var3='im a new varibale'


childObject=child()
print childObject.var1

print childObject.var2

print childObject.var3
