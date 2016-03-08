def name(first,last):
	print '%s %s' % (first, last)

print name('bucky','Martin')

def name(first='tom', last='smith'):
	print '%s %s' % (first, last)

print name()

print name('Martin', 'Madej')

print name(last='roberts')

