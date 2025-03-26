#Utilizando list comprenitiin crea una lista de solo numeros pares proibido utlizar el range, otra lista que almazene todos los numeros inpares usuario elige
x = 0
numpares =[]
while x < 100:
    x = x + 1
    if x % 2 == 0:
        numpares.append(x)
print(numpares)
    