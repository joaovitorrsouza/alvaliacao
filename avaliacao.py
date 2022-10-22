"""""exe01
print("Olá mundo")
"""
"""""exe02
numero = input("Digite o número:"
print(f"O número informado foi:{numero}
"""
"""""exe03
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

soma = num1 + num2;

print(f"O valor total da soma é: {soma}")
"""
"""""exe04
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digete a quarta nota:"))

média = nota1 + nota2 + nota3 + nota4/4;

print(f"O valor da média é: {média}")
"""
"""""exe05
metros = int(input("Digite a medida em metros a ser convertida em centímetros:"))

conversao = metros*100;

print(f"O valor convertido é: {conversao}cm")
"""
"""""exe06
raio = float(input("Digite o raio do círculo:"))
area = 3.14*(raio*2);

print(f"A área do círculo é {area}:")
"""
"""""exe07
quadcomp = float(input("Digite o comprimento do quadrado:"))
quadlarg = float(input("Digite a largura do quadrado:"))

areaquad = quadcomp*quadlarg;
dobarea = areaquad*2;

print(f"A área do quadrado é {areaquad}:")
print(f"O dobro dessa área é {dobarea}:")
"""
"""""exe08
salario_hora = float(input("Digite o quanto voce ganha por hora:"))
hora_trab = float(input("Digite o número de horas trabalhadas:"))

salario_final = salario_hora*hora_trab*30;

print(f"O seu salário esse mes é de {salario_final}")
"""
"""""exe09
F = float(input('Entre com a temperatura em graus Fahrenheit: '))
  C = (F - 32) * (5 / 9)
  print('Valor em Celsius: {0}°C'.format(C))
"""
"""""exe10
C = float(input('Entre com a temperatura em graus Celsius: '))
  F = C * (9 / 5) + 32
  print('Valor em Fahrenheit: {0}°F'.format(F))
"""
"""""exe11
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
numero_real = float(input("Digite o numero Real:"))
r1 = n1*2*(n2/2)
print (f'o produto do dobro do primeiro com metade do segundo: {r1}')

r2 = n1*3 + numero_real
print(f'a soma do triplo do primeiro com o terceiro: {r2}')

r3 = numero_real ** 3
print(f'o terceiro elevado ao cubo:{r3}')
"""
"""""exe12
h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))
"""
"""""exe13
sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))
"""
"""""exe01Estrutura de decisão
num1 = int (input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))

if num1 > num2:
    print(f'O maior número foi: {num1}')
else:
    print(f' O maior número foi: {num2}')
"""
"""""exe02Estrutura de decisão
n = int(input("Aqui vai o valor que o usuário irá digitar:"))

if(n < 0):

print("O valor digitado é negativo!")

else:

print("O valor digitado é positivo!")
"""
"""""exe03Estrutura de decisão
sexo = input("Digite F para Feminino ou M para Masculino: ")
if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else:
    print("Sexo Inválido")
"""
"""""exe04Estrutura de decisão
alfa = input("Informe uma letra ou consoante:")

if alfa.isalpha():
    if alfa =="a":
        print("Vogal")
    elif alfa == "e":
        print("Vogal")
    elif alfa == "i":
        print("Vogal")
    elif alfa == "o":
        print("Vogal")
    elif alfa == "u":
        print("Vogal")
        print("Insira uma letra ou consoante")
    else:
        print("Consoante")
else:
    print("Não é uma letra!")
"""
"""""exe05Estrutura de decisão
nota1= float(input("Digite nota 1:"))
nota2=float(input("Digite nota 2:"))
media_final = float(nota1 + nota2)/2

if media_final == 7.0 or media_final== 9.99:
  print(f'Sua média é {media_final:=7}')
  print(f'Aprovado')

if media_final == 10.0:
    print(f'Sua média é {media_final:=10}')
    print(f'Aprovado com Distinção')
else:
  print(f'Sua média é {media_final:>= 7}')
  print(f'- Reprovado')
"""
"""""exe06Estrutura de decisão
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

if num1 > num2 and num3:
    print("O número um é o maior: ", num1)
elif num2 > num1 and num3:
    print("O número dois é o maior: ", num2)
elif num3 > num1 and num2:
    print("O número três é o maior: ", num3)
"""
"""""exe07Estrutura de decisão
a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
"""
"""""exe08Estrutura de decisão
preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))
if preco1 < preco2 and preco1 < preco3:
    print(f"O produto com o menor preco é o 1, custando R${preco1:.2f}")
elif preco2 < preco1 and preco2 < preco3:
    print(f"O produto com o menor preco é o 2, custando R${preco2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${preco3:.2f}")
"""
"""""exe09Estrutura de decisão
a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >=c and c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a and c >= b and a >=b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b and b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')
"""
"""""exe10Estrutura de decisão
turno = input("Digite M para Matutino, V Vespertino ou N Noturno: ")
if turno == "M" or turno =="m":
    print("Bom dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde")
elif turno == "N" or turno == "n":
    print("Boa Noite")
else:
    print("Turno Inválido")
"""
"""""exe11Estrutura de decisão
salario_fixo = float(input ("Digite o sálario fixo:"))
Percentual_aumento1= 20/100
Percentual_aumento2 = 15/100
Percentual_aumento3 = 10/100
Percentual_aumento4 = 5/100
aumento_salario1 = salario_fixo * Percentual_aumento1
aumento_salario2 = salario_fixo * Percentual_aumento2
aumento_salario3 = salario_fixo * Percentual_aumento3
aumento_salario4 = salario_fixo * Percentual_aumento4
salario_final1= salario_fixo - aumento_salario1
salario_final2= salario_fixo - aumento_salario2
salario_final3= salario_fixo - aumento_salario3
salario_final4= salario_fixo - aumento_salario4

if salario_fixo<=280:
  print(f'O salário antes do reajuste era:{salario_fixo}')
  print("O valor do percentual de aumento foi 20%")
  print(f'O valor do aumento foi:{aumento_salario1}')
  print(f'Salário final é:{salario_final1}')

elif salario_fixo >=280.01 and salario_fixo<= 700:
  print(f'O salário antes do reajuste era:{salario_fixo}')
  print("O valor do percentual de aumento foi 15%")
  print(f'O valor do aumento foi:{aumento_salario2}')
  print(f'Salário final é:{salario_final2}')

elif salario_fixo >= 700.01 and salario_fixo <= 1500:
  print(f'O salário antes do reajuste era:{salario_fixo}')
  print("O valor do percentual de aumento foi 10%")
  print(f'O valor do aumento foi:{aumento_salario3}')
  print(f'Salário final é:{salario_final3}')

elif salario_fixo >= 1500.01:
  print(f'O salário antes do reajuste era:{salario_fixo}')
  print("O valor do percentual de aumento foi 10%")
  print(f'O valor do aumento foi:{aumento_salario4}')
  print(f'Salário final é:{salario_final4}')
"""
"""""exe01Estrutura de repetição
nota = float(input("Digite uma nota entre 0 e 10: "))
while (nota < 0 or nota > 10):
    nota = float(input("Nota digitada incorretamente. Digite uma nota entre 0 e 10: "))
"""
"""""exe02Estrutura de repetição
print("faça já seu cadastro")
usuario=str(input("usuário: "))
senha=str(input("senha:"))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("usuário--> "))
	senha=str(input("senha-->"))
else:
	print("cadastrado efetuado com sucesso")
"""
"""""exe03Estrutura de repetição
nome = str(input("informe um nome--> "))
while (len(nome) <= 3):
    nome = str(input("informe um nome--> "))

idade = int(input("informe a idade--> "))
while (idade > 150 or idade < 0):
    idade = int(input("informe a idade--> "))

salario = float(input("informe um salário--> "))
while (salario < 0):
    salario = float(input("informe um salário--> "))

sexo = str(input("informe a inicial do seu sexo--> "))
while sexo != "f" and sexo != "m":
    sexo = str(input("informe a inicial do seu sexo--> "))

estado_civil = str(input("informe a inicial do seu estado civil-->"))
while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
    estado_civil = str(input("informe a inicial do seu estado civil-->"))
"""
"""""exe04Estrutura de repetição
a = 80000
b = 200000
ano = 0

while a <= b:
	a += a * 0.03
	b += b * 0.015
	ano += 1

print ( "A ultrapassa ou iguala a B em %d anos" %ano )
"""
"""""exe05Estrutura de repetição
a = float(input("Digite o número de habitantes do primeiro País:"))
taxa_crescimento1= float(input("Digite a taxa anual de crescimento da população do primeiro País:"))
b = float(input("Digite o número de habitantes do segundo País:"))
taxa_crescimento2= float(input("Digite a taxa anual de crescimento da população do segundo País:"))
ano = 0
while a <= b:
	a += a * taxa_crescimento1/100
	b += b * taxa_crescimento2/100
	ano += 1

print ("A ultrapassa ou iguala a B em %d anos" %ano )
"""
"""""exe06Estrutura de repetição
for i in range (21):
	print (i)
print(list(range(1,21)))
"""
"""""exe07Estrutura de repetição
numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um número: ")))

maiorNumero = numeros[0]

cont = 1
while cont < len(numeros):
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1

print("O maior número é: " + str(maiorNumero))
"""
"""""exe08Estrutura de repetição
num1=float(input("digite o 1º numero--> "))
num2=float(input("digite o 2º numero--> "))
num3=float(input("digite o 3º numero--> "))
num4=float(input("digite o 4º numero--> "))
num5=float(input("digite o 5º numero--> "))
soma=num1+num2+num3+num4+num5
print("soma-->",soma,)
print("média-->",soma/5)
"""
"""""exe09Estrutura de repetição
for i in range(1,51,2):
    print (i)
"""
"""""exe10Estrutura de repetição
num1=int(input("digite um numero--> "))
num2=int(input("digite outro numero--> "))
while num2<num1:
	num1=int(input("digite um numero--> "))
	num2=int(input("digite outro numero--> "))
else:
	for i in range(num1,num2,1):
		print(i)
"""
"""""exe01exercicios com string
string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")
tamanho_str_1 = len(string_1)
tamanho_str_2 = len(string_2)
print(string_1 + " " + str(tamanho_str_1))
print(string_2 + " " + str(tamanho_str_2))
"""
"""""exe02Estrutura de repetição
print('Pode digitar seu nome com letras maiúsculas, minúsculas ou mistas.')
nome = input('Digite seu nome: ').upper()
invNome = nome[::-1]
print('{} ---> {}'.format(nome, invNome))
"""
"""""exe03Estrutura de repetição
nome = input('Digiete a palavra: ')
for i in nome:
    print(str.upper(i))
"""
"""""exe04Estrutura de repetição
nome = str(input('Digite seu nome: ')).upper()
for i in range(0,len(nome)+1):
    print(nome[:i])
"""
"""""exe05Estrutura de repetição
nome = str(input('Digite seu nome: ')).upper()
for i in range(0,len(nome)+1):
    print(nome[i:])
"""
"""""exe06Estrutura de repetição
dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
meses = ['janeiro', 'fevereiro', 'março', 'abril','maio', 'junho', 'julho', 'agosto', 'setembro','outubro', 'novembro', 'dezembro']
print('Você nasceu em: ')
print('%s de %s de %s' %(dia, meses[int(mes)-1], ano))
"""
"""""exe07Estrutura de repetição
string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")
tamanho_str_1 = len(string_1)
tamanho_str_2 = len(string_2)
print(string_1 + " " + str(tamanho_str_1))
print(string_2 + " " + str(tamanho_str_2))
if tamanho_str_1 != tamanho_str_2:
    print("As duas strings são de tamanhos diferentes")
else:
    print("As duas strings são do mesmo tamanho")
if string_1 == string_2:
    print("O conteúdo das duas string são idênticas")
else:
    print("O conteúdo das duas string são diferentes")
"""



























