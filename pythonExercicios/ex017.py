from time import sleep

c = ('\033[m',         # 0- sem cores
     '\033[0;30;41m',  # 1-vermelho
     '\033[0;30;42m',  # 2-verde
     '\033[0,30;43m',  # 3-amarelo
     '\033[0;30;44m',  # 4-azul
     '\033[0;30;45m',  # 5-roxo
     '\033[7;30m'      # 6-branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)
    print(c[6], end='')


# programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA pyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)

'''def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional,indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit in 'Ss':
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(2.3,4.5,6.7,sit=True)
print(resp)
help(notas)'''

'''def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digíte um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''

'''def ficha(jog='<desconhecido>', gol=0):

    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


print('-' * 30)
jog = str(input('Nome do jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jog.strip() == '':
    ficha(gol)
else:
    ficha(jog, gol)'''

'''def fatorial(n, show=''):  # show=False
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show in 'Ss':
            print(c, end='')
            if c > 1:
                print(f' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# fatorial(4)
# print(fatorial(4))
n = int(input('Digite um número para obter seu fatorial: '))
show = str(input('Deseja mostrar como o calculo foi feito? [S/N] '))
print(fatorial(n, show))'''

'''def voto(ano):
    from datetime import date  # reduz o uso de memória no dispositivo
    idade = date.today().year - ano
    if idade < 16:
        v = 'Não vota'
        return f'Com {idade} anos: {v}'
    elif 18 <= idade < 65:
        v = 'Voto obrigatório'
        return f'Com {idade} anos: {v}'
    elif 16 <= idade < 18 or idade > 65:
        v = 'Voto opcional'
        return f'Com {idade} anos: {v}'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))'''

'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')'''

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


print(somar(3, 2, 5))
r1 = somar(3, 4)
r2 = somar(6)
print(f'As somas valem {r1} e {r2}')'''

'''def teste():
    x = 8 #Local V
    print(f'Na função, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2 #Global V
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')'''

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 4)'''

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIm!')


contador(2, 10, 2)
help(contador)'''

# help(print)
# para buscar ajuda use esses dois
# print(input.__doc__)
# def soma(a=0,b=0,c=0)parâmetro opcional
# global=a para usar o a variavel a global nas funções
# return para retornar algo da função
