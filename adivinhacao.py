import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1,100)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: "))
    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 6
    elif(nivel == 3):
        total_tentativas = 3


    for rodada in range(1, total_tentativas + 1):
        #print("Tentativa {} de {}".format(rodada, total_tentativas))
        print(f"Tentativa {rodada} de {total_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100" )
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos}!")
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior.")
            elif(menor):
                print("Você errou! Seu chute foi menor.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()