"""palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáãàeéêiou':
            print(letra, end=' ')"""

"""listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_' * 40)"""

"""num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')"""

"""from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('OS valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')"""

"""times = (
'Corinthias', 'Palmeiras', 'Santos', 'grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
'Atlético-GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os primeiros são {times[0:5]}')
print('-='*15)
print(f'Os últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')"""

"""cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'cartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')"""

# lanche = ('Hambúrguer', 'suco', 'Pizza', 'Pudim')
# Tuplas são IMUTÁVEIS
# print(lanche)
# for c in range(0,len(lanche)):
# print(f'Eu vou comer {lanche[c]}')
# for c in lanche:
#  print(f'eu vou comer {c}')
# for pos,c in enumerate(lanche):
#   print(f'Eu vou comer {c} na posição {pos}')
# print('comi pra caramba')
# print(sorted(lanche))
# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c=a+b
# print(c)
# print(c.index(8))
# pessoa = ('Cauê', 18, 'M', 99.88)
# del pessoa
# print(pessoa)
