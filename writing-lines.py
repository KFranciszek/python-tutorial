fob = open('a.txt','r')
listme = fob.readlines()
print listme
fob.close
listme[2] = 'mm i sure love bacon'

print listme

fob = open('a.txt','w')

fob.writelines(listme)
fob.close()

