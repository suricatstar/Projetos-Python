D = int(input('Por quantos dias o carro foi alugado: '))
K = float(input('Quantos quilometros ele percorreu: '))
dia = 60 * D
kil = 0.15 * K
Total = (60 * D) + (0.15 * K)
print('A diária ficou por R${:.2f} e o percurso ficou por R${:.2f},logo o total a pagar é R${}'.format(dia, kil, Total))
print('-' * 12)
C = float(input('Informe a temperatura em ˚C: '))
F = 1.8 * C + 32
# F = ((9*C)/5)+32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(C, F))
# carro = ('Fiat Uno')
# cor = ('azul')
# km = ('720´)
# print(f'O veículo era um {carro}, de cor {cor} e com {km} quilômetros rodados.')
print('-' * 12)
s = float(input('Qual é o salário do funcionário ? R$'))
reajuste = float(input('Qual é o seu reajuste ?'))
SA = s + (s * reajuste / 100)
print('um funcionário que recebia R${}, com {}% de reajuste, passa a receber R${}'.format(s, reajuste, SA))
print('-' * 12)
larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m quadrados.'.format(larg, altu, area))
print('Para pintar essa parede, você irá precisar de {}L de tinta.'.format(tinta))
print('-' * 12)
p = float(input('Qual é o preço do produto ? R$'))
desconto = int(input('Quanto tem de desconto ? '))
pr = p * desconto / 100
pf = p - pr
# p - (p * desconto / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de {} vai custar R${:.2f}'.format(p, desconto, pf))
print('-' * 12)
n1 = float(input('um valor: '))
print('Seu sucessor é {}'.format(n1 + 1), 'e seu antecessor é {} '.format(n1 - 1))  # format(n1,(n1+1),(n1-1))
print('A medida de {} metros equivale a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(n1, n1 / 1000, n1 / 100,
                                                                                           n1 / 10,
                                                                                           n1 * 10, n1 * 100,
                                                                                           n1 * 1000))
print('Isso em Dólar equivale à {} dólares'.format(n1 / 5.43))
print('E equivale à {} Éuros'.format(n1 / 6.10))
print('------------')
n2 = float(input('outro valor: '))
print('sua tabuada é:')
print('{} x {:2} = {}'.format(n2, 1, n2 * 1))
print('{} x {:2} = {}'.format(n2, 2, n2 * 2))
print('{} x {:2} = {}'.format(n2, 3, n2 * 3))
print('{} x {:2} = {}'.format(n2, 4, n2 * 4))
print('{} x {:2} = {}'.format(n2, 5, n2 * 5))
print('{} x {:2} = {}'.format(n2, 6, n2 * 6))
print('{} x {:2} = {}'.format(n2, 7, n2 * 7))
print('{} x {:2} = {}'.format(n2, 8, n2 * 8))
print('{} x {:2} = {}'.format(n2, 9, n2 * 9))
print('{} x {:2} = {}'.format(n2, 10, n2 * 10))
print('-' * 12)
print('Seu dobro é {} seu triplo é {} e sua raiz quadrada é {}'.format((n2 * 2), (n2 * 3), n2 ** (1 / 2)))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2  # pow(n1,(n2))/pow(n1,(1/2))
r = n1 % n2
# \n quebra linha ,end='' não quebrar linha (usar no depois do format ou no final do codigo )
print(
    "A soma entre eles vale {}, o produto entre eles vale {}, a divisão entre eles vale {},\na divisão inteira entre "
    "eles vale {},\no resto de divisão entre eles é {} e a exponenciação entre eles vale {}".format(
        s, m, d, di, r, e))
print('a média entre eles é {}'.format((n1 + n2) / 2))
