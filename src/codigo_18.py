num = int(input("Escribe un numero limite para mostrar la serie fibonacci: "))
prim = 0
seg = 1
tot = 0
print(prim)
print(seg)
for i in range(num):
    tot = prim + seg
    prim = seg
    seg = tot
    print(tot)