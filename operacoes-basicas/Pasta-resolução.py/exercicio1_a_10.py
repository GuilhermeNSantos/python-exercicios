import math


# Exercício 1 - Faça um algoritmo para ler as dimensões de um terreno e depois exibir a área do terreno?

altura = float(input("Informe qual a altura do terreno em metros : "))
largura = float(input("Informe qual a largura do terreno em metros :"))

area = (altura * largura)
print(f"O terreno possui {area} m²")


# Exercício 2 - Quantas ferraduras para cavalos?

cavalos = int(input("Qual a quantidade cavalos? "))
ferraduras = cavalos * 4
print("A quantidade ferraduras necessárias para a quantidade de cavalos é:", ferraduras)

# Exercício 3 - Ler a quantidade de pães e broas vendidos, calcular o total arrecadado e 10% para a poupança?

broas = int(input("Qual a quantidade de broas? "))
pao = int(input("Qual a quantidade de pães? "))

valor_broas = broas * 2.5
valor_pao = pao * 1.20
vtotal = valor_broas + valor_pao
poupanca = vtotal * 0.10
print("O valor total foi:", vtotal)
print("O valor das broas foi:", valor_broas)
print("O valor dos paes foi:", valor_pao)
print("o valor para colocar na poupança é :", poupanca)

# Exercício 4 -Ler nome e idade e calcular quantos dias a pessoa já viveu ?

nome = str(input("Informe seu nome: "))
idad = int(input("Informe sua idade: "))

dias_vividos = idad * 365
print(f"{nome}, você possui esses dias vividos:", dias_vividos)

# Exercício 5 - Calcular a quantidade de litros a partir do preço da gasolina e exibir?

gasolina = float(input("Infome o preço do litro da gasolina:R$ "))
dinheiro = float(
    input("Informe o valor a ser inserido para compra da gasolina:R$ "))

litros = dinheiro / gasolina
print(f"Você conseguiu colocar {litros} litros no tanque")

# Exercício 6 - Ler o peso do prato e calcular o valor a pagar por quilo (R$55,00/kg)?

quilos = float(input("Quantos quilo o seu prato tem? "))
valor_total = quilos * 55
print(" O valor a pagar é: R$ ", valor_total)

# Exercício 7 - Ler dia e mês e calcular quantos dias se passaram no ano?

dias = int(input("Informe a quantidade de dias: "))
meses = int(input("Informe a quantidade meses que já passaram: "))
valor_diaspormes = meses * 30
valor_final = valor_diaspormes + dias
print("A quantidade de dias finais é: ", valor_final)

# Exercício 8 - Ler três notas e calcular a média ponderada.

nota1, nota2, nota3 = map(int, input("Informe as três notas: ").split())
media_ponderada = ((nota1 * 4) + (nota2 * 3) + (nota3 * 2))/9
print("A média ponderada das notas foram: ", media_ponderada)

# Exercício 9 - Ler quantidades de camisetas e calcular o valor arrecadado.

camisa_pequena = int(input("Informe a quantidade camisas pequenas: "))
camisa_media = int(input("Informe a quantidade camisas médias: "))
camisa_grande = int(input("Informe a quantidade camisas grandes: "))

conf = (camisa_pequena * 40) + (camisa_media * 42) + (camisa_grande * 45)
print("O valor total foi de:R$ ", conf)


# Exercício 10 - Calcular a distância entre dois pontos do plano cartesiano.

x1, y1 = map(float, input(
    "Informe as coordenadas do primeiro ponto: ").split())
x2, y2 = map(float, input("Informe as coordenadas do segundo ponto: ").split())

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("A distância entre os pontos é:", distancia)
