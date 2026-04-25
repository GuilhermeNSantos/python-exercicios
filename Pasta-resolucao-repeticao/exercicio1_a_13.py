import math

# Exercício 1 - Exibir 20 vezes a mensagem “Eu gosto de estudar Algoritmos!”

for i in range(20):
    print("Eu gosto de estudar Algoritmos!")


# Exercício 2 - Calcular a soma dos números de 1 a 15.

soma = 0

for i in range(1, 16):
    soma += i

print("Soma:", soma)


# Exercício 3 - Ler um nome e exibi-lo 10 vezes.

nome = input("Digite seu nome: ")

for i in range(10):
    print(nome)


# Exercício 4 - Ler um nome e um número N e exibir o nome N vezes.

nome = input("Digite seu nome: ")
n = int(input("Digite quantas vezes deseja exibir: "))

for i in range(n):
    print(nome)


# Exercício 5 - Ler 10 números e calcular a soma deles.

soma = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    soma += numero

print("Soma dos números:", soma)


# Exercício 6 - Ler a idade de 20 pessoas e calcular a soma das idades.

soma_idades = 0

for i in range(20):
    idade = int(input("Digite a idade: "))
    soma_idades += idade

print("Soma das idades:", soma_idades)


# Exercício 7 - Ler a idade de 20 pessoas e calcular a média das idades.

soma_idades = 0

for i in range(20):
    idade = int(input("Digite a idade: "))
    soma_idades += idade

media = soma_idades / 20

print("Média das idades:", media)


# Exercício 8 - Ler a idade de 20 pessoas e contar quantas são maiores de idade.

maiores = 0

for i in range(20):
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        maiores += 1

print("Quantidade de maiores de idade:", maiores)


# Exercício 9 - Ler nome e idade de 10 pessoas e exibir o nome da mais nova.

menor_idade = 999999
nome_mais_nova = ""

for i in range(10):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade < menor_idade:
        menor_idade = idade
        nome_mais_nova = nome

print("Pessoa mais nova:", nome_mais_nova)


# Exercício 10 - Ler um número e exibir sua tabuada.

numero = int(input("Digite um número: "))

for i in range(11):
    print(numero, "x", i, "=", numero * i)


# Exercício 11 - Ler 20 números e contar quantos são maiores que 8.

contador = 0

for i in range(20):
    numero = int(input("Digite um número: "))

    if numero > 8:
        contador += 1

print("Quantidade maiores que 8:", contador)


# Exercício 12 - Ler 20 números e contar quantos são pares.

pares = 0

for i in range(20):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        pares += 1

print("Quantidade de números pares:", pares)


# Exercício 13 - Ler 20 números e contar quantos estão entre 0 e 100.

contador = 0

for i in range(20):
    numero = int(input("Digite um número: "))

    if 0 < numero < 100:
        contador += 1

print("Quantidade entre 0 e 100:", contador)
