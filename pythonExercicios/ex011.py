"""print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 50
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')"""

"""total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${menor:.2f}')"""

"""tot18=totH=totM20=0
while True:
    idade=int(input('Idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo=='M':
        totH+=1
    if sexo =='F' and idade<20:
        totM20+=1
    resp=' '
    while resp not in 'SN'
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp=='N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')"""

"""from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER Você venceu {v} vezes.')"""

"""while True:
    n=int(input('quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n<0:
        break
    for c in range(1,11):
        print(f'{n} x {c} ={n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')"""

"""soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')"""

# n = s = 0
# while True:
#   n = int(input('Digite um nümero: '))
#   if n == 999:
#       break
#   s += n
# print('A soma vale {}'.format(s))
# print(f'A soma vale {s}')
