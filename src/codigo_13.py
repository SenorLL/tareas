pizzas = ["pepperoni", "hawaiana", "margarita"]
for pizza in pizzas:
    if pizza == "pepperoni":
        print(f"Me encanta la pizza de {pizza}")
    if pizza == "hawaiana":
        print(f"No me gusta la pizza de {pizza}")
    if pizza == "margarita":
        print(f"No conozco la pizza de {pizza}")
pizzas.append("3 carnes")
print("Me gusta la pizza de 3 carnes")