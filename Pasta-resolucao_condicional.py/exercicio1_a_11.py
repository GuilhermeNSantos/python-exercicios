import math

# Exercício 1 - Raiz quadrada ou quadrado do número

numero = float(input("Informe o número: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz do número é: {raiz}")
else:
    quadrado = numero * numero
    print(f"O quadrado do número é: {quadrado}")


# Exercício 2 - Soma e ajuste do resultado

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

soma = numero1 + numero2

if soma > 20:
    resultado = soma + 8
    print(f"O valor final é {resultado}")
else:
    resultado = soma - 5
    print(f"O valor final é {resultado}")


# Exercício 3 - Desconto no combustível

tipo_combustivel = input(
    "Informe o combustível (A-álcool, G-gasolina): ").upper()

quantidade_litros = float(input("Informe a quantidade de litros: "))

if tipo_combustivel == "A" and quantidade_litros <= 20:
    valor = 0.97 * quantidade_litros * 2.5
    print("Valor a pagar:", valor)

elif tipo_combustivel == "A" and quantidade_litros > 20:
    valor = 0.95 * quantidade_litros * 2.5
    print("Valor a pagar:", valor)

elif tipo_combustivel == "G" and quantidade_litros <= 20:
    valor = 0.96 * quantidade_litros * 3.9
    print("Valor a pagar:", valor)

elif tipo_combustivel == "G":
    valor = 0.94 * quantidade_litros * 3.9
    print("Valor a pagar:", valor)

else:
    print("Valor inválido")


# Exercício 4 - Dosagem de medicamento

idade = int(input("Informe sua idade: "))
peso = int(input("Informe seu peso: "))

if idade <= 12 and peso > 60:
    print("Quantidade de gotas: 40")

elif idade <= 12 and peso <= 60:
    gotas = (875 / 500) * 20
    print(f"Quantidade de gotas: {gotas}")

elif idade > 12 and peso < 9:
    gotas = (125 / 500) * 20
    print(f"Quantidade de gotas: {gotas}")

elif idade > 12 and peso < 16:
    gotas = (250 / 500) * 20
    print(f"Quantidade de gotas: {gotas}")

elif idade > 12 and peso < 24:
    gotas = (375 / 500) * 20
    print(f"Quantidade de gotas: {gotas}")

elif idade > 12 and peso < 30:
    gotas = (500 / 500) * 20
    print(f"Quantidade de gotas: {gotas}")

elif idade > 12 and peso >= 30:
    gotas = (750 / 500) * 20
    print(f"Quantidade de gotas: {gotas}")

else:
    print("Valor errado")


# Exercício 5 - Dias do mês

mes = input("Informe o nome do mês sem acento: ").lower()

if mes == "janeiro":
    print("31 dias")

elif mes == "fevereiro":
    print("28 dias")

elif mes == "marco":
    print("31 dias")

elif mes == "abril":
    print("30 dias")

elif mes == "maio":
    print("31 dias")

elif mes == "junho":
    print("30 dias")

elif mes == "julho":
    print("31 dias")

elif mes == "agosto":
    print("31 dias")

elif mes == "setembro":
    print("30 dias")

elif mes == "outubro":
    print("31 dias")

elif mes == "novembro":
    print("30 dias")

elif mes == "dezembro":
    print("31 dias")  # corrigido

else:
    print("Valor errado")


# Exercício 6 - Alta ou baixa temporada

mes_temporada = input("Informe o mês sem acento: ").lower()

if mes_temporada in ["janeiro", "fevereiro", "junho", "julho", "dezembro"]:
    print("Alta temporada")

elif mes_temporada in ["marco", "abril", "maio", "agosto",
                       "setembro", "outubro", "novembro"]:
    print("Baixa temporada")

else:
    print("Valor errado")


# Exercício 7 - Divisível por 3

numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print("Número divisível por 3")
else:
    print("Número não divisível por 3")


# Exercício 8 - Dia útil

dia_semana = int(input(
    "Domingo=1 até sábado=7: "
))

if dia_semana == 1:
    print("Domingo não é útil")

elif dia_semana == 2:
    print("Segunda é útil")

elif dia_semana == 3:
    print("Terça é útil")

elif dia_semana == 4:
    print("Quarta é útil")

elif dia_semana == 5:
    print("Quinta é útil")

elif dia_semana == 6:
    print("Sexta é útil")

elif dia_semana == 7:
    print("Sábado não é útil")

else:
    print("Dia inválido")


# Exercício 9 - Calculadora simples

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe um segundo número: "))
operacao = input("Escolha +, -, * ou / : ")

if operacao == "+":
    print(numero1 + numero2)

elif operacao == "-":
    print(numero1 - numero2)

elif operacao == "*":
    print(numero1 * numero2)

elif operacao == "/":
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print("Divisão por zero não permitida")

else:
    print("Operação inválida")


# Exercício 10 - Conta bancária

saldo_conta = float(input("Informe saldo da conta: "))
atividade = input("Depósito(D) ou saque(S): ").upper()

if atividade == "D":
    deposito = float(input("Valor depósito: "))
    saldo_final = saldo_conta + deposito
    print("Saldo final:", saldo_final)

elif atividade == "S":
    saque = float(input("Valor saque: "))
    saldo_final = saldo_conta - saque
    print("Saldo final:", saldo_final)

else:
    print("Valor inválido")


# Exercício 11 - Conta de energia

salario_minimo = float(input("Informe o salário mínimo: "))
valor_kw = salario_minimo / 8

tipo_consumidor = int(
    input("1-Residencial 2-Comercial 3-Industrial: ")
)

if tipo_consumidor == 1:
    valor_total = valor_kw * 1.05
    print("Valor a pagar:", valor_total)

elif tipo_consumidor == 2:
    valor_total = valor_kw * 1.10
    print("Valor a pagar:", valor_total)

elif tipo_consumidor == 3:
    valor_total = valor_kw * 1.15
    print("Valor a pagar:", valor_total)

else:
    print("Informação errada.")
