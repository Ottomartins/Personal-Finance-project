import os
from Student import Pergunta

#this is

perguntas_linhas = [
    "Qual a cor de uma banana?\n(a) Vermelho\n(b) Amarelo\n(c) Roxo\n\n",
    "Qual a cor de uma maçã?\n(a) Amarelo\n(b) Verde/Vermelho\n(c) Laranja\n\n",
    "Qual a cor de um morango?\n(a) Verde\n(b) Vermelho\n(c) Azul\n\n"
]

perguntas = [
    Pergunta(perguntas_linhas[0], "b"),
    Pergunta(perguntas_linhas[1], "b"),
    Pergunta(perguntas_linhas[2], "b"),
]

def iniciar_teste(perguntas):
    pontuação = 0
    for pergunta in perguntas:
        resposta = input(pergunta.linha)
        if resposta == pergunta.resposta:
            pontuação += 1
    print('Você acertou ' + str(pontuação) + ' de ' + str(len(perguntas)) + ' perguntas')



def guess_game():
    palavra_secreta = "banana"
    resposta = ""
    resposta_contagem = 0
    resposta_limite = 5
    limite_de_erros = False

    while resposta != palavra_secreta and not(limite_de_erros):
        if resposta_contagem < resposta_limite:
            resposta = input("\nAdivinhe qual fruta eu estou pensando: ")
            os.system('cls')
            resposta_contagem += 1
        else:
            limite_de_erros = True
    if limite_de_erros:
        print("Limite de respostas, você PERDEU!\n\n")
        os.system("pause")
    else:
        print("Parabens você GANHOU!!!")
        jogar_novamente = input("\nGostaria de ver outra? S para SIM, N para NAO: ")

        if jogar_novamente.upper() == "S" or jogar_novamente.upper() == "SIM":
            os.system('cls')
            madlib()
        elif jogar_novamente.upper() == "N" or jogar_novamente.upper() == "NAO" or jogar_novamente.upper() == "NÃO":
            os.system('cls')
            print('\nNesse caso, até a próxima.\n')
            os.system("pause")


def welcome():
    print('''Olá Andreia!!''')
welcome()

def piada(frase):
    traducao = ""
    for letra in frase:
        if letra in "13579":
            traducao = traducao + "Seres "
        else:
            letra in "24680"
            traducao = traducao + "Onomatopeios "
    return traducao


def madlib():
    color = input("\nDigite uma cor no plural feminino: ")
    pluralNoun = input("\nDigite um substantivo no Plural: ")
    celebrity = input("\nNome de alguma comida: ")
    os.system('cls')
    print("Rosas são", color)
    print(pluralNoun + " são azuis")
    print("Eu amo", celebrity)
    os.system('cls')
    iniciar_teste(perguntas)

def calculator():
    op = input('''
Escolha a operação desejada\n+ Para adição\n- Para subtração\n* Para multiplicação\n/ Para divisão\n% Para Porcentagem\n* Para elevar ao poder: ''')
    num1 = float(input('''
Coloque o primeiro número: '''))
    num3 = float(input('''
Coloque o segundo número: '''))
    if op == "+":
        print('\n{} + {} = {}'.format(num1, num3, (num1 + num3)))
    elif op == "-":
        print('\n{} - {} = {}'.format(num1, num3, (num1 - num3)))
    elif op == "/":
        try:
            print('\n{} / {} = {}'.format(num1, num3, (num1 / num3)))
        except ZeroDivisionError:
            print("Impossível dividir por 0.")
            denovo()
    elif op.upper() == "X":
        print('\n{} x {} = {}'.format(num1, num3, (num1 * num3)))
    elif op == "%":
        print('\n{}% de {} = {}'.format(num1, num3, ((num1/100) * num3)))
    elif op == "*":
        def raise_to_power(num1, num3):
            result = 1
            num1 = int(num1)
            num3 = int(num3)
            for x in range(num3):
                result = result * num1
            return result
        print('\n{} elevado a {} = {}'.format(num1, num3, (raise_to_power(num1, num3))))
    else:
        print('''
Operação inválida.
''')
    denovo()

def denovo():
    repetir = input('''
Você gostaria de fazer mais algum cálculo?\nDigite S para SIM e N para NÃO ou P para a brincadeira secreta: ''')
    if repetir.upper() == "S" or repetir.upper() == "SIM":
        os.system('cls')
        calculator()
    elif repetir.upper() == "N" or repetir.upper() == "NAO" or repetir.upper() == "NÃO":
        os.system('cls')
        print('\nNesse caso, até a próxima.\n')
        os.system("pause")
    elif repetir.upper() == "P":
        os.system('cls')
        guess_game()
    else:
        denovo()

calculator()
