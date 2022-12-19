"""expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errado!')"""

"""num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')"""

"""valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')"""

"""lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
                pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')"""

"""números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')"""

"""listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas Posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')"""

# a=[2,3,4,7]
# b=a[:] cópia
# b=a não cópia
# b[2]=8
# print(f'Lista A:{a}')
# print(f'Lista B:{b}')


# valores = []
# for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')))

# valores.append(5)
# valores.append(9)
# valores.append(4)
# for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

# for v in valores:
#   print(f'{v}...',end='')


# num = [2, 5, 9, 1]
# num[2]=3
# num.append(7)
# num.sort()
# num.sort(reverse=True)
# num.insert(2,2)
# if 4 in num:
#    num.remove(4)
# else:
#    print('Não achei o número 5')
# num.remove(2)
# num.pop()
# num.pop(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')


# ,,,.append('')adiciona elemento na lista
# ,,,.insert(0,'') adiciona um elemento na lista em determinada posição
# del ,,,[3] elimina algo na lista em determinada posição
# ,,,.pop[3] mesma coisa, mas geralmente é usado pra deletar o último elemento
# ,,,.remove('')remove o conteúdo da lista
