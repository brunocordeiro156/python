import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo Jokenpô!")
    print("*********************************")

    aleatorio = random.randint(1,3)
    escolha_computador = ""

    #pode usar lista para a escolha do computador
    if(aleatorio == 1):
        escolha_computador = "PEDRA"
    elif(aleatorio == 2):
        escolha_computador = "PAPEL"
    elif (aleatorio == 3):
        escolha_computador = "TESOURA"

    escolha_p1 = input("Digite: ")
    escolha_p1 = escolha_p1.strip().upper()

    if(escolha_p1 == escolha_computador):
        print(escolha_computador)
        print(f"EMPATE! {escolha_p1} = {escolha_computador}")
    elif(escolha_p1 == "PEDRA"):
        if(escolha_computador == "TESOURA"):
            print(f"GANHOU! {escolha_p1} > {escolha_computador}")
        else:
            print(f"PERDEU! {escolha_p1} < {escolha_computador}")
    elif(escolha_p1 == "PAPEL"):
        if (escolha_computador == "PEDRA"):
            print(f"GANHOU! {escolha_p1} > {escolha_computador}")
        else:
            print(f"PERDEU! {escolha_p1} < {escolha_computador}")
    elif (escolha_p1 == "TESOURA"):
        if (escolha_computador == "PAPEL"):
            print(f"GANHOU! {escolha_p1} > {escolha_computador}")
        else:
            print(f"PERDEU! {escolha_p1} < {escolha_computador}")

if(__name__ == "__main__"):
    jogar()