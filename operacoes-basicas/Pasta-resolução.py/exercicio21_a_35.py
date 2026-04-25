import math

# Exercício 21 - Calcular o valor total economizado com moedas.

moeda_de1 = int(input("Quantas moedas de 1 centavos você possui guardadas: "))
moeda_de5 = int(input("Quantas moedas de 5 centavos você possui guardadas: "))
moeda_de10 = int(input("Quantas moedas de 10 centavos você possui guardadas: "))
moeda_de25 = int(input("Quantas moedas de 25 centavos você possui guardadas: "))
moeda_de50 = int(input("Quantas moedas de 50 centavos você possui guardadas: "))
moeda_de100 = int(input("Quantas moedas de 1 real você possui guardadas: "))

soma_dasmoedas = ((moeda_de1 * 1) + (moeda_de5 * 5) + (moeda_de10 * 10) + (moeda_de25 * 25) + (moeda_de50 * 50) + (moeda_de100 * 100)) / 100
print("A quantidade de reais no cofrinho é: R$", soma_dasmoedas)

# Exercício 22 - Calcular a altura de um prédio usando sombras.

altura_pessoa = float(int("Qual a altura da pessoa? "))
sombra_pessoa = float(int("Qual a somba da pessoa? "))
sombra_predio = float(int("Qual a sombra do prédio? "))

altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa
print("A altura do prédio é: ", altura_predio)

# Exercício 23 - Calcular quantos litros de água e suco são necessários para o refresco.

litros = int("Qual a quantidade de litros")
litrosconvertidos = (litros * 1000)
agua_mineral = litrosconvertidos * 0.8
suco = litrosconvertidos * 0.2

print(f"A quantidade de água e maracujá é : {agua_mineral}, e {suco} ml")

# Exercício 24 - Calcular o volume de uma caixa d’água cilíndrica.

raio_da_base = int(input("Qual o raio da base do cilindro? "))
altura_cilindro = int(input("Qual a altura do cilindro? "))

volume = (math.pi * (raio_da_base ** 2)) * altura_cilindro
print("O volume do cilindro é: ", volume)

# Exercício 25 - Calcular a multiplicação de três números.

numero1, numero2, numero3 = map(int, input("Informe três números: ").split())
multiplicacao = numero1 * numero2 * numero3
print("A multiplicação dos números é: ", multiplicacao)

# Exercício 26 - Calcular a divisão de dois números.

numero_1 = int(input("Informe um número: "))
numero_2 = int(input("Informe um segundo número: "))

if numero_2 == 0:
    print("Não foi possível dividir pois um dos termos foi o zero")
else:

    divisao = numero_1 / numero_2
    print("A divisão dos números foram de: ", divisao)

# Exercício 27 - Calcular a média ponderada de duas notas.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media_ponderada = ((nota1 * 2) + (nota2 * 3))/5
print("A media ponderada das notas é : ", media_ponderada)

# Exercício 28 - Calcular o novo preço de um produto com 10% de desconto.

produto = int(input("Qual o valor do produto: "))
desconto = produto * 0.90
print("O produto com desconto é: ", desconto)

# Exercício 29 - Calcular comissão e salário final de um funcionário.

salario = int(input("Informe o seu salário: "))
vendas = int(input("Informe as vendas: "))
calculo_partedacomissao = vendas * 0.04
comissao = salario + calculo_partedacomissao
print("O salário final com comissão é de: ", comissao)

# Exercício 30 - Converter peso de quilos para gramas.

peso = float(input("Qual o seu peso em KG: "))
conversao_peso = peso * 1000
print("O seu peso em gramas é de: ", conversao_peso)

# Exercício 31 - Calcular a área de um trapézio.

basemenor = float(input("Informe a base menor do trapézio: "))
basemaior = float(input("Informe a base maior do trapézio: "))
altura = float(input("Informe a altura do trapézio: "))
areadotrapezio = ((basemenor + basemaior) * altura)/2
print("A área do trapézio é de: ", areadotrapezio)

# Exercício 32 - Calcular a área de um quadrado.

lado_quadrado = float(input("Informe o lado do quadrado: "))
area_quadrado = lado_quadrado ** 2
print("A área do quadrado é de: ", area_quadrado)

# Exercício 33 - Calcular a área de um losango.

diagonal_menor = float(input("Qual a diagonal menor: "))
diagonal_maior = float(input("Qual a diagonal maior: "))
area_losango = (diagonal_menor * diagonal_maior)/2
print("A área do losando é de: ", area_losango)

# Exercício 34 - Calcular quantos salários mínimos um funcionário recebe.

valor_salariominimo = float(input("Qual o valor do salário mínimo: "))
valor_recebido = float(input("Quanto você recebe"))
quantidade_desalariominimo = valor_recebido / valor_salariominimo
print("Você possui essa quantidade de salário mínimos: ",
      quantidade_desalariominimo)

# Exercício 35 - Exibir a tabuada de um número digitado.

numbers = int(input("Forneça um número de 0 a 10?"))
print("A tabuada do número é: ")

for i in range(11):
    tabuada_number = numbers * i
    print(f" {numbers} x {i} = {tabuada_number}")
