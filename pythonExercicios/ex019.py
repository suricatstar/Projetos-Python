# import uteis.erros
# from uteis import erros
from uteis.erros.arquivo import *
from uteis.erros import *  # * importa tudo
from time import sleep

arq = 'listanomes.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('ERRO! Digite uma opção válida!')
    sleep(1)

'''import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('consegui abrir o site pudim com sucesso!')
    print(site.read())'''

'''def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digíte um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digíte um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O número inteiro digitado foi {n1} e o número real foi {n2}')'''

# try:
#    a = int(input('Numerador: '))
#    b = int(input('Denominador: '))
#    r = a / b
# except:
# print('Infelizmente tivemos um problema :(')
# except Exception as erro:
#   print(f'Problema encontrado foi {erro.__class__}')
# except (ValueError,TypeError):
#    print('Tivemos um problema com os tipos de dados que você digitou.')
# except ZeroDivisionError:
#    print('Não é possível dividir um número por zero!')
# except KeyboardInterrupt:
#    print('O usuário preferiu não infromar os dados!')
# else: #opcional
#    print(f'O resultado é {r:.1f}')
# finally: #opcional
#   print('Volte sempre! Muito obrigado!')
