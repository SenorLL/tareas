#Realice un programa que dadas dos palabras me diga si es un anagramada
palabras = []
coincidencias = 0
palabras.append(input("Introduce una palabra: "))
palabras.append(input("Introduce otra palabra: "))
for i in range(len(palabras[0])):
    for j in range(len(palabras[1])):
        if palabras[0][i] == palabras[1][j]:
            coincidencias = coincidencias+1
if coincidencias == len(palabras[0]):
    print("Las palabras son un anagrama")
else:
    print("Las palabras no son un anagrama")
