while  True:
    nome = input("Qual seu nome?")
    if (nome != "Lenhadorzinho"):
        continue # Volta para o início do laço

    senha = input("Qual a sua senha?")
    if (senha == "Uninter"):
        break # Encerra o laço

print("Acesso concebido.")
