def cart(**items):
	print items

print cart(apples=4,peaches=6,beef=60)


def profile(first,last,*ages,**items):
	print first, last
	print ages
	print items


print profile('bucky','robert',32,34,54,56,76,24,52, bacon=4,saus=40)

