#Número pares de 1 a 100

soma = 0
qtd = 0
for i in range(1,101,1):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print(f"A média dos pares de 1 até 100 é: {media}")