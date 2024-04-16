inicial = int(input("Qual valor deseja inicial a contagem?"))
final = int(input("Qual valor deseja encerrara contagem?"))

x = inicial
while (x <= final):
    #Verfica se o número é par
    if (x % 2 == 0 ):
        print(x)
    x = x + 1
    