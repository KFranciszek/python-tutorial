book = {'Dad':'Bob','Mom':'Lisa','Bro':'Joe'} # tworzymy slownik { klucz:atrybut} cos jak bazy danych? do sprawdzenia

print book

print book['Dad'] # wyswietli sie nam atrybut klucza Dad czyli "Bob"


ages = {'Dad':'42','Mom':'37'} # atrybuty to tez liczby nie tylko napisy
print ages

print ages['Dad']

book.clear() # czysci caly slownik

print book

tuna = ages.copy() # kopjuje caly slownik

print tuna

print tuna.has_key('Mom') # wielkosc liter ma znaczenie  pokazuje czy ma dany klucz w slowniku i zwraca true/false

print tuna.has_key('Apples')