
"""from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')"""

"""preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))
if option == 1:
    desconto = preco - (preco * 10 / 100)
elif option == 2:
    desconto = preco - (preco * 5 / 100)
elif option == 3:
    desconto = preco
    parcela = desconto / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif option == 4:
    desconto = preco + (preco * 20 / 100)
    parce = int(input('Quantas parcelas? '))
    parcela = desconto / parce
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parce, parcela))
else:
   print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, desconto))"""

"""peso=float(input('Qual é seu peso? (Kg)'))
altura=float(input('Qual é sua altura? (M) '))
imc=peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5<=imc<25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25<= imc <30:
    print('Você está em SOBREPESO')
elif 30<=imc<40:
    print('Você está em OBESIDADE!')
elif imc>=40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')"""

"""r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')"""

"""from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade > 25:
    print('CLASSIFICAÇÃO: MASTER')
elif 19 < idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
elif 14 < idade <= 19:
    print('CLASSIFICAÇÃO: JÚNIOR')
elif 9 < idade <= 14:
    print('CLASSIFCAÇÃO: INFANTIL')
else:
    print('CLASSIFICAÇÃO: MIRIM')"""

"""n1 = float(input('Primeiro nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'azulc': '\033[36m',
       'amarelo': '\033[33m'}
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, média))
if média >= 7:
    print('{}PARABÉNS VOCÊ FOI APROVADO{}'.format(cor['amarelo'], cor['limpa']))
elif 5 <= média <= 6.9:
    print('{}VOCÊ ESTA DE RECUPERAÇÃO{}'.format(cor['azulc'], cor['limpa']))
else:
    print('Sinto em te informar, mas você foi {}reprovado{}'.format(cor['vermelho'], cor['limpa']))
"""

"""from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = -ano + atual
print('Quem nasceu em {} tem {} anos em 2022'.format(ano, idade))
if idade == 18:
    print('Você já pode se alistar')
elif idade > 18:
    Alis = idade - 18
    print('VOCÊ DEVERIA TER SE ALISTADO HÁ {} ANO, VÁ LOGO!'.format(Alis))
    saldo=atual-Alis
    print('Seu alistamento foi em {}'.format(saldo))
else:
    Alis = -idade + 18
    print('Falta {} anos para você se alistar'.format(Alis))
    saldo = atual + Alis
    print('seu alistamento será em {}'.format(saldo))"""

"""P = int(input('Primeiro número: '))
S = int(input('Segundo número: '))
if P == S:
    print('Os dois números são iguais')
elif P > S:
    print('O primeiro é o valor maior')
else:
    print('O segundo é o valor maior')"""

# num = int(input('Digite um número Inteiro: '))
# print('''Escolha uma das bases para conversão:
# {}[ 1 ]{} converter para BINÁRIO
# {}[ 2 ]{} converter para OCTAL
# {}[ 3 ]{} converter para HEXADECIMAL'''.format('\033[31m', '\033[m', '\033[34m', '\033[m', '\033[35m', '\033[m'))
# option = int(input('Sua opção: '))
# if option == 1:
#    print('{} convertido para BINÁRIO é igual a {}{}'.format(num, '\033[31m', bin(num)[2:]))
# elif option == 2:
#    print('{} convertido para OCTAL é igual a {}{}'.format(num, '\033[34m', oct(num)[2:]))
# elif option == 3:
#    print('{} convertido para HEXADECIMAL é igual a {}{}'.format(num, '\033[35m', hex(num)[2:]))
# else:
#   print('\033[33mOpção inválida. Tente novamente ')

"""C = float(input('Valor da casa: R$'))
S = float(input('Salário do comprador: R$'))
F = int(input('Quantos ano de financiamento? '))
prestação = C / (F * 12)
M = S * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} a'.format(C, S), end=' ')
print('prestação será de {:.2f}'.format(prestação))
if prestação <= M:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')"""

# nome = str(input('Qual é seu nome? '))
# if nome == 'Cauê':
#    print('Que nome bonito!')
# elif nome == 'Danilo' or nome == 'Alexandre':
#    print('Seu nome é de alguém que é gente boa')
# elif nome in 'Fialho' or 'Tamiarana':
#    print('Você é da família')
# else:
#    print('Seu nome é bem normal.')
# print('Tenha um Bom Dia sr.{}{}{}'.format('\033[31;40m', nome, '\033[m'))
