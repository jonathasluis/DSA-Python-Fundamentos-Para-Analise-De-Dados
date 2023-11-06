# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

controle = 0 #contrloe do while
while (controle == 0):
    print("\nselecione a operação desejada:")
    print("\n1 - soma")
    print("\n2 - subtração")
    print("\n3 - multiplicação")
    print("\n4 - divisão")
    print("\n5 - SAIR")

    opcao = input("\nDigite sua opção (1/2/3/4/5): ")

    if (opcao == '1'):
        num1 = float(input("\nDigite o primeiro numero: "))
        num2 = float(input("\nDigite o segundo numero: "))
        print("\n",num1," + ", num2," = ",soma(num1,num2))

    elif (opcao == '2'):
        num1 = float(input("\nDigite o primeiro numero: "))
        num2 = float(input("\nDigite o segundo numero: "))
        print("\n",num1," - ", num2," = ",subtracao(num1,num2))

    elif (opcao == '3'):
        num1 = float(input("\nDigite o primeiro numero: "))
        num2 = float(input("\nDigite o segundo numero: "))
        print("\n",num1," * ", num2," = ",multiplicacao(num1,num2))

    elif (opcao == '4'):
        num1 = float(input("\nDigite o primeiro numero: "))
        num2 = float(input("\nDigite o segundo numero: "))
        print("\n",num1," / ", num2," = ",divisao(num1,num2))

    elif (opcao == '5'):
        controle = 1

    else:
        print("\nopção inválida!")

    print('\n*********************************************************\n')






