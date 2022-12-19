print('\033[36;107mFala meu lindo\033[m')
nome = input('\033[97;40mQual é o teu nome meu cria ?\033[m ')
print('É uma honra te conhcer meu querido colega, {}{}{}'.format('\033[36m',nome,'\033[m'))  # {:=20}
print('É alpha ?\033[1;33m',nome.isalpha())

# \033[0;33;44m]
# style: 0(none),1(bold),4(underline),7(negative)
# text: 30-37(branco,vermelho,verde,amarelo,azul,roxo,azul claro,cinza)97-branco,30-preto
# back: 40-47(branco,vermelho,verde,amarelo,azul,roxo,azul claro,cinza)107-branco,40-preto
