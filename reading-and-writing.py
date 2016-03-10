fob = open("a.txt",'r')
print fob.readline()

print fob.readlines()
fob.close()

fob = open("a.txt",'w')

fob.write('this is a new line\n nowa linia nowa linia\na to jest trzecia linia \n')
fob.close()


