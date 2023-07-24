'''
Faça um programa que mostre na tela uma contagem regressiva para 
o estouro de fogos de artificio, indo de 10 ate 0 e apos  0 mostre 'BOOOM!'.
'''
for b in range(10, -1, -1):
    if b > 0:
        print(b)
    else:
        print("BOOOM!")   