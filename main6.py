#Valores "Truthy e "Falsey"
nome = "" #Falsey
while not nome: #not Falsey (Truthy/True)
    # Encerra o laço quando nome não estiver vazio
    nome = input("Digite seu nome:")

valor = int(input("Digite um número qualquer: "))
if valor: # Equivalente if valor != 0:
    print("Você digitiou um valor diferente de zero.")
else:
    print("Você digitou zero.")
