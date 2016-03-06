example = list('easyhoss') # polecenie lista dzieli wyraz/slowo na liste zlozona z pojedynczych znakow


print example

example[4:]=list('baby') # od 4 pozycji ( od zera zaczynamy) zmienia elementy listy

print example

example[4:] = list("racecars")

print example # to samo co wczesniej

example = [7,8,9] #zmieniamy elementy listy

print example

example[1:1] = [3,3,3]

print example

example[1:5] = [] # ustawia jako puste od 1 pozycji do 5 ale nie wlacznie
print example