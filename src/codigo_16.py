# haga un programa que calcule el factorial de un numero dado

num = input("Escribe un numero el cual quiera calcular su factorial: ")
if num.isnumeric() == True:
    num = int(num)
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    print(f"El factorial de {num} es {factorial}")