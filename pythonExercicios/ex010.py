"""resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e a menor foi {}'.format(maior, menor))"""

"""núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))"""

"""print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('˜' * 30)
print('{} ➝ {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ➝ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➝ Fim')
print('˜' * 30)"""

"""print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➝ '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))"""

"""print('Gerador de PA')
print('-='*10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão da PA: '))
termo=primeiro
cont=1
while cont<=10:
    print(' {} ➝ '.format(termo),end='')
    termo+=razão
    cont+=1
print('FIM')"""

"""fator = int(input('Digite um número para calcular seu fatorial: '))
c = fator
f = 1
print('Calculando {}! = '.format(fator), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))"""

"""from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = 0
while option != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    option = int(input('>>>>> Qual é a sua opção? '))
    if option == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif option == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif option == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif option == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')"""

# from time import sleep
# from random import randint
# print('Sou seu computador...')
# computador = randint(0, 10)
# sleep(2)
# print('acabei de pensar em um número entre 0 e 10')
# jogador = int(input('Qual número eu pensei? '))
# tentativa = 0
# tentativa=false
# while not acertou:
# tentativa=True se acertou
# while jogador != computador:
#  if jogador < computador:
#      print('mais...Tente novamente')
#   else:
#     print('menos...Tente novamente')
#  tentativa += 1
#  jogador = int(input('Qual número eu pensei? '))
# tentativa+=1
# print('Acertou com {} tentativas. Parabéns'.format(tentativa))

"""sexo = str(input('Informe seu Sexo: [M/F] ')).upper()[0].strip()
while sexo not in 'MmFf':
    print('Essa não é a resposta correta, tente novamente')
    sexo = str(input('Informe seu Sexo: [M/F] ')).upper()[0].strip()
print('Sexo {} registrado com sucesso'.format(sexo))"""

"""n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))"""

"""r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')"""

"""n=1
while n!=0:
    n=int(input('Digite um valor: '))
print('FIM')"""

"""c = 1
while c < 10:
    print(c)
    c += 1
print('fim')"""
