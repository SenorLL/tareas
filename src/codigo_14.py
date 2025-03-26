#Pienza en al menos 3 animales diferentes que tengan caracteristicas similares. Almacenalos en una lista e imprime la lista de animales en un for A) imprime un mensaje para cada animal ej. "Un perro seria un gran amigo" B) agrega un elemento a la lista e imprimelo despues del for todos estos animales serian una gran mascota

animales = ["perro","gato","conejo"]
for animal in animales:
    if animal == "gato":
        print(f"Un {animal} es un animal muy inquieto")
    if animal == "perro":
        print(f"Un {animal} es el mejor amigo del hombre")
    if animal == "conejo":
        print(f"Un {animal} es un animal muy tierno")
animales.append("pez")
print(f"Un {animales[3]} es un animal muy tranquilo")
print("Todos estos animales son mascotas")


