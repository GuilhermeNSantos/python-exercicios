import math


# Exercício 11 - Converter dias em anos, meses e dias.

anos_semacidente = (int(input("Informe a quantidade de anos sem acidentes? ")))

total_meses = anos_semacidente * 12
total_dias = total_meses * 30
print(f"O tempo foi sem acidentes em meses é : {total_meses} e em dias é: {total_dias}")


# Exercício 12 - Calcular salário com aumento de 15% e desconto de 8% de impostos.

salario = float(input("Informe o salário o seu salário: "))
aumento = salario * 1.15
desconto = aumento * 0.92
print("O valor final do seu salário com aumentos e descontos é: ", desconto)

# Exercício 13 - Ler um número e separar centena, dezena e unidade.

number = int(input("Informe um número: "))

unidade = number % 10
dezena = (number // 10) % 10
centena = (number // 100) % 10
print("A centena do número é: ", centena)
print("A dezena do número fornecido é: ", dezena)
print("A unidade fornecida é: ", unidade)

# Exercício 14 - Calcular a área de uma pizza pelo raio.

raio = float(input("Informe o raio da pizza: "))
area = math.pi * (raio ** 2)
print("A área fornecida da pizza é de: ", area)

# Exercício 15 - Dividir a conta entre três amigos conforme as regras dadas.

conta = float(input("Informe o valor total da conta: "))

valor_inteiro = conta // 3
valor_felipe = conta - (valor_inteiro * 2)

print(f"Carlos pagará: R$ {valor_inteiro:.2f}")
print(f"André pagará: R$ {valor_inteiro:.2f}")
print(f"Felipe pagará: R$ {valor_felipe:.2f}")

# Exercício 16 - Calcular a quantidade de ingredientes para fazer sanduíches.

hamburguer = int(input("Forneça a quantidade de hamburguers: "))
queijo = hamburguer * 2
presunto = hamburguer * 1
carne = hamburguer * 1

quantidade_queijo = (queijo * 50) / 1000
quantidade_presunto = (presunto * 50) / 1000
quantidade_carne = (carne * 100) / 1000

valor_total = (quantidade_queijo + quantidade_presunto + quantidade_carne)
print(f"A quantidade de quilos de queijo é: KG {quantidade_queijo}")
print(f"A quantidade de quilos de presunto é: KG {quantidade_presunto}")
print(f"O valor de quilos da quantidade de carnes é: KG {quantidade_carne}")
print(f"O valor total de quilos necessário é {valor_total}")

# Exercício 17 - Converter temperatura de Celsius para Fahrenheit.

celsius = float(input("Forneça a temperatura em Celsiuns: "))
fahrenheit = (celsius * 1.8) + 32
print(f"A temperata convertirada para fahrenheit é: {fahrenheit}")

# Exercício 18 - Calcular salário bruto e líquido com horas normais e extras.

hora_normais = int(input("Qual a quantidade de horas normais trabalhadas: "))
valorhora_normais = hora_normais * 20

hextra = float(input("Qual a quantidade de horas extras trabalhadas: "))
valorhora_extra = hextra * 25

salario = valorhora_normais + valorhora_extra
salario_liquido = salario * 0.90
print(f"O salário bruto é de: {salario}")
print(f"O salário líquido é de {salario_liquido}")

# Exercício 19 - Calcular o gasto para marcar todos os frangos com anéis.

quantidade_frango = int(input("Qual a quantidade de frangos? "))
chip_identificacao = (quantidade_frango * 1) * 4
print("O valor do chip de identificação é: ", chip_identificacao)

chip_alimentacao = (quantidade_frango * 2) * 3.5
print("O valor do chip de alimentação é:", chip_alimentacao)

# Exercício 20 - Calcular quantos litros de refrigerante foram comprados.

garrafas_pequenas = int(input("Quantas garrafas de 350ml vc comprou: "))
garrafas_medias = int(input("Quantas garrafas médias de 600ml vc comprou: "))
garrafas_grandes = int(input("Quantas garrafas grandes de 2LITROS vc comprou: "))

quantidade_total = ((garrafas_pequenas * 350) + (garrafas_medias * 600) + (garrafas_grandes * 2000)) / 1000
print(f"A quantidade de litros compradas foram de: {quantidade_total}")
