
"""print('-=' * 20)
print('ANALISADOR de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')"""

"""salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    reaj = salario + (salario * 10 / 100)
else:
    reaj = salario + (salario * 15 / 100)
print('O salário desse funcionário deverá ser de {}'.format(reaj))"""

"""a = int(input('Primeiro valor:'))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi o {}'.format(menor))
print('O maior valor digitado foi o{}'.format(maior))"""

"""from datetime import date

ano = int(input('Que ano queres analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))"""

# via = float(input('Qual é a distância da sua viagem? '))
# pre = via *0.50 if via <= 200 else via * 0.45
# if via <= 200:
#    pre = via * 0.50
# else:
#    pre = via * 0.45
# print('O percurso de sua viagem é de {} \nO preço de sua viagem é de R${}'.format(via, pre))
# print('Tenha uma boa viagem!')

"""nu = int(input('Me diga um número qualquer: '))
result = nu % 2
if result == 1:
    print('O número {} é Impar'.format(nu))
else:
    print('O número {} é par'.format(nu))

Velo = float(input('Qual é a velocidade atual do carro? '))
if Velo > 80:
    print('MULTADO! Você excedeu o limite permitido de velocidade que é 80km/h')
    Multa = (Velo - 80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(Multa))
print('Tenha um Bom Dia e Dirija com Segurança!')"""

"""from random import randint
from time import sleep  # faz o computador "esperar"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
C = randint(0, 5)  # Faz o computador "pensar"
J = int(input('Em que número eu pensei? '))  # O jogador tenta advinhar o número
print('PROCESSANDO...')
sleep(3)
if J == C:
    print('PARABÉNS, você acertou o número que eu estava pensando')
else:
    print('GANHEI! eu pensei no número {} e não no {}'.format(C, J))"""

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2) / 2
# print('A sua média foi {:.1f}'.format(m))
# print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')
# if m >=6.0:
#   print('Sua média foi boa! PARABÉNS!')
# else:
#    print('Sua média foi ruim! ESTUDE MAIS!')

# nome = str(input('Qual seu nome ? ')).strip()
# if nome == 'Cauê':
#    print('que nome lindo você tem')  # se para aqui é simples
# else:
#    print('Seu nome é tão normal')  # se parar aqui é composta
# print('Bom dia {}'.format(nome))

# tempo = int(input('quantos ano o seu carro tem ?'))
# if tempo <= 3:
#    print('Teu carro ta novinho')
# else:
#    print('ta na hora de trocar né filho ?')
# print('carro novo' if tempo <= 3 else 'carro velho')
