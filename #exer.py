


soma = 0
qnt_pares = 0

for i in range(1,7):
    n = int(input("digite um numero:"))
    if n % 2 == 0:
        soma += n
        qnt_pares += 1
    
print("Soma =", soma)
print("Pares =", qnt_pares)  