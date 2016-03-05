example = [ 0,1,2,3,4,5,6,7,8,9 ]
print example[4:8] # pokazuje od 4 do 8 ale bez 8 wlacznie

print example[4:9] # tu juz pokazuje od 4 do 8 ( bez 9 )

print example[4:10] # tu juz od 4 do 9 wlacznie ( 10 i tak nie ma w tupli )

print example[-5:-1] # od 5 od konca do 1 od konca 

print example[-5:] # od 5 od konca do konca koncow hah!

print example[:7] # od poczatku do 7 ale nie wlacznie

print example[1:8:2] # trzecia pozycja to jest " krok " tak jak w petli for 

print example[10:0:-2] # od konca do poczatku i krok co 2 ;) 

print example[::-2] # jak wyzej od poczatku do konca i krok co dwa w tyl ;) 