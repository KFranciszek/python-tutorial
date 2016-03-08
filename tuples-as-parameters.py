def example(a,b,c):
	return a+b*c

tuna = (5,7,3)

print example(*tuna) # uzywamy tupli/listy jako parametry

def example2(**this):
	print this

bacon = {'mom':42,'dad':54}

print example2(**bacon)