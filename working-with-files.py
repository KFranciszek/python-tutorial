fob = open('a.txt','w') # otwieramy plik tekstowy do pisania
fob.write('hey now brown cow') # piszemy w pliku tekstowym
fob.close() # zamykamy plik tekstowy
fob = open('a.txt','r') # otwieramy plik do czytania
print fob.read(10) # w nawiasie mozemy okreslic ile znakow chcemy wczytac
print fob.read() # wyswietla tylko od 11 znaku bo 10 wczesniej juz wczytalismy
fob.close() # zawsze zamykamy na koncu 