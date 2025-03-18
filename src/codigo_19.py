num = int(input("Escribe un numero: "))
x = 0
for i in range(2,num-1):
    if num % i == 0:
        x = x+1
if num == 0 or num == 1:
    print("El numero no es primo")
else:
    if x == 0:
        print("El numero es primo")
    else:
        print("El numero no es primo")