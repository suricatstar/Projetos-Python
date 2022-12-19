#from random import randint
#from time import sleep


#def sorteia(lista):
#    print('Sorteando 5 valores da lista: ', end='')
#    for cont in range(0, 5):
#        n = randint(1, 10)
#        lista.append(n)
#        print(f'{n} ', end='', flush=True)
#        sleep(0.3)
#    print('PRONTO!')


#def somapar(lista):
#    soma = 0
#    for valor in lista:
#        if valor % 2 == 0:
#            soma += valor
#    print(f'Somando os valores pares de {lista}, temos {soma}')


#numeros = list()
#sorteia(numeros)
#somapar(numeros)

# from time import sleep


# def maior(*num):
#    cont = maior = 0
#    print('-=' * 30)
#    print('ANALISANDO OS VALORES PASSADOS... ')
#    for valor in num:
#        print(f'{valor} ', end='', flush=True)
#        sleep(0.3)
#        if cont == 0:
#            maior = valor
#        else:
#            if valor > maior:
#                maior = valor
#        cont += 1
#    print(f'Foram informados {cont} valores ao todo.')
#    print(f'O maior valor informado foi {maior}')


# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1,2)
# maior(6)
# maior()

# from time import sleep


# def contador(i, f, p):
#    if p < 0:
#        p *= -1
#    if p == 0:
#        p = 1
#    print('-=' * 20)
#    print(f'Contagem de {i} até {f} de {p} em {p}')
#    sleep(2.5)

#    if i < f:
#        cont = 1
#        while cont <= f:
#            print(f'{cont} ', end='', flush=True)
#            sleep(0.5)
#            cont += p
#        print('FIM!')
#    else:
#        cont = i
#        while cont >= f:
#            print(f'{cont} ', end='', flush=True)
#            sleep(0.5)
#            cont -= p
#        print('FIM')


# contador(1, 10, 1)
# contador(10, 0, 2)
# print('-=' * 20)
# print('Agora é sua vez de personalizar a contagem')
# ini = int(input('Início: '))
# fim = int(input('Fim: '))
# pas = int(input('Passo: '))
# contador(ini, fim, pas)

# def escreva(msg):
#   tam = len(msg) + 4
#    print('˜' * tam)
#    print(f'   {msg}')
#    print('˜' * tam)


# escreva('Vai estudar seu vagabundo')
# escreva('Oi')

# def area(l, c):
#   a = l * c
#    print(f'A área de um terreno {l}M X {c}M é de {a}m quadrados')


# print(' Controle de Terrenos')
# print('-' * 20)
# l = float(input('LARGURA (m): '))
# c = float(input('COMPRIMENTO (m): '))
# area(l, c)

# def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

# def contador(*num):
#    tam=len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} números')
# print(num)
# for valor in num:
#    print(f'{valor} ',end='')
# print('FIM')
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma A + B = {s}')
# soma(b=4, a=5)
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

# def titulo(txt):
#    print('_'*30)
#    print(txt)
#   print('-'*30)
# def lin():
#    print('-' * 30)
# programa principal
# lin()
# titulo('   Python é bom ó  ')
# print('      loucuras   ')
# lin()
