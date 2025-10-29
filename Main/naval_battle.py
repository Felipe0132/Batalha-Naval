from random import randint
import builtins
import copy
import os
import sys

def limpar_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


#Cores terminal
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
LIGHT_BLUE = "\033[38;2;135;206;250m"  
RED = "\033[38;2;255;0;0m"        
GRAY_DARK = "\033[38;2;50;50;50m" 
ORANGE = "\033[38;2;255;165;0m"    

old_print = builtins.print

def custom_print(*args, **kwargs):
    new_args = []
    for arg in args:
        if isinstance(arg, str):
            new_text = ""
            for char in arg:
                if char == "A":
                    new_text += f"{BLUE}{char}"
                elif char == "E":
                    new_text += f"{GRAY_DARK}{char}"
                elif char == "X":
                    new_text += f"{RED}{char}"
                elif char == "O":
                    new_text += f"{LIGHT_BLUE}{char}"
                else:
                    new_text += f"{RESET}{char}"
            arg = new_text + RESET  # aplica reset só no final
        new_args.append(arg)
    old_print(*new_args, **kwargs)

builtins.print = custom_print


# Batalha Naval

largura = 10
altura = 10
num_embarcacoes = 5

def imprime_tabuleiro(tabuleiro):
    print("*", end=' ')
    for i in range(altura):
        print(i+1,end=" ")
    print()
    for x in range(largura):
        if(x >= 9):
            print(x+1, end="")
        else:
            print(x+1, end=" ")

        for y in range(altura):
            if y >= 9:
                print(tabuleiro[x][y], end="  ")
            else:
                print(tabuleiro[x][y], end=" ")
            
        print()

def imprime_visivel(tabuleiro):
    tabuleiro_visivel = copy.deepcopy(tabuleiro) 
    print("*", end=' ')
    for i in range(altura):
        print(i+1,end=" ")
    print()
    for x in range(largura):
        if(x >= 9):
            print(x+1, end="")
        else:
            print(x+1, end=" ")

        for y in range(altura):
    
            if tabuleiro_visivel[x][y] not in "OX":
                tabuleiro_visivel[x][y] = "?" 

            if y >= 9:
                print(tabuleiro_visivel[x][y], end="  ")
            else:
                print(tabuleiro_visivel[x][y], end=" ")
        
        print()
    

def montando_tabuleiro(tabuleiro):
    for x in range(largura):
        for y in range(altura):
            tabuleiro[x][y] = "A"

def monta_escolha(tabuleiro):
    for i in range(num_embarcacoes):
        while True:
            print(f'Posicionando embarcação {i+1}')
            try:
                x = int(input("Digite a posicao x: "))
                y = int(input("Digite a posicao Y: "))

                x -= 1
                y -= 1

                if x >= largura or y >= altura or y < 0 or x < 0:
                    print('Posição inválida! Fora dos limites')
                    continue

                if tabuleiro[x][y] == 'E':
                    print('Posição ja marcada!')
                else:
                    tabuleiro[x][y] = 'E'
                    break

            except ValueError:
                print("Digite um intiro!")
            

def monta_sortido(tabuleiro):
    for i in range(num_embarcacoes):
        while True:
            x = randint(0, altura-1)
            y = randint(0, largura-1)

            if tabuleiro[x][y] != "E":
                tabuleiro[x][y] = "E"
                break

def verifica_ataca(mapa, x, y):
    return mapa[x][y] not in ("X", "O")

def atacar(mapa, x, y):
    if(mapa[x][y] == "E"):

        mapa[x][y] = "X"

        return -1
    else:
            mapa[x][y] = "O"
            return 0

def user_ataque():
    while True:
        try:

            y = int(input(f"Digite o x que deseja atacar (1 a {largura}): "))
            x = int(input(f"Digite o y que deseja atacar (1 a {altura}): "))

            x -= 1
            y -= 1

            # para testes, valores aleatorios para ir mais rapido
            #y = randint(0, altura-1)
            #x = randint(0, largura-1)

            if x < 0 or y < 0 or x >= altura or y >= largura:
                print(f"Posição precisa estar entre (1,1) e ({altura, largura})")
                continue

            if not verifica_ataca(tabuleiro_computador, x, y):
                print("Posição já atacada!")
                continue
                    
            break
                        
        except ValueError:
            print("Digite valores inteiros!")

    print(f"Ataque em ({x},{y})")
    #return atacar(tabuleiro_computador, x-1, y-1)
    return atacar(tabuleiro_computador, x, y)

def comp_ataque():
    while True:
        y = randint(0, altura-1)
        x = randint(0, largura-1)

        if not verifica_ataca(tabuleiro_jogador, y, x):
                continue
        
        break
    
    print(f"Ataque em ({x+1},{y+1})")
    return atacar(tabuleiro_jogador, y, x)


def comecarpartida(tabuleiro_computador, tabuleiro_jogador):
    cont = 0
    embarcacoes_jogador = num_embarcacoes
    embarcacoes_computador = num_embarcacoes
    while(embarcacoes_jogador != 0 and embarcacoes_computador != 0):
        if(cont % 2 == 0):
            print("Vez Usuario!")
            print("Veja como esta marcado o tabuleiro adiversario:\n")
            imprime_visivel(tabuleiro_computador)

            embarcacoes_computador += user_ataque()

            print("\nVeja como esta marcado o seu tabuleiro:\n")
            imprime_tabuleiro(tabuleiro_jogador)

            try:
                resp = input("Deseja ver o tabuleiro adversario completo para verificar erros(Digite Sim para ver)?: ")
                resp = resp.lower()
                if resp.startswith("sim"):
                    print("Tabuleiro Computador\n")
                    imprime_tabuleiro(tabuleiro_computador)
            except Exception as e:
                print(f"Erro obtido: {e}")

        else:
            print("Vez Computador\n")


            embarcacoes_jogador += comp_ataque()
        cont+=1   

        input("Precisone ENTER para seguir...")
        limpar_terminal()
    
    if embarcacoes_computador <= 0:
        print("Usuário venceu!")
    elif embarcacoes_jogador <= 0:
        print("Computador venceu!")

    print(f"Tiveram {cont} ataques totais!")

    input("Precisone ENTER para seguir...")
    



tabuleiro_jogador = [[" " for _ in range(altura)] for _ in range(largura)]

montando_tabuleiro(tabuleiro_jogador)
while True:
    try:
        resp = int(input("Deseja escolher posição das embarcações?\n[1] SIM\n[2] NAO\n"))
        if resp == 1:
            monta_escolha(tabuleiro_jogador)
            break
        else:
            monta_sortido(tabuleiro_jogador)
            break
    except Exception as e:
        print(f"Error: {e}")





#print(f"\nTABULEIRO JOGADOR")
#imprime_tabuleiro(tabuleiro_jogador)

tabuleiro_computador = [[" " for _ in range(altura)] for _ in range(largura)]

montando_tabuleiro(tabuleiro_computador)

monta_sortido(tabuleiro_computador)

#print(f"\nTABULEIRO COMPUTADOR")
#imprime_tabuleiro(tabuleiro_computador)

comecarpartida(tabuleiro_computador, tabuleiro_jogador)

print("\n")

try:
    resp = input("Deseja ver o resultado final(Digite Sim para ver)?: ")
    resp = resp.lower()

    if resp.startswith("sim"):
        print(f"\nTABULEIRO JOGADOR")
        imprime_tabuleiro(tabuleiro_jogador)
        print(f"\nTABULEIRO COMPUTADOR")
        imprime_tabuleiro(tabuleiro_computador)
except Exception as e:
    print(f"\nERROR.{e}")
