def metade(num=0, formato=False):
    """

    :param num: O valor a ser recebido
    :param formato: Para formatar o texto(TRUE)
    :return: Retorna o valor, formatado ou não
    """
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    """

    :param num: O valor a ser recebido
    :param formato: Para formatar o texto(TRUE)
    :return: Retorna o valor, formatado ou não
    """
    res = num * 2
    return res if formato is False else moeda(res)


def aumento(num=0, taxa=0, formato=False):
    """

    :param num: O valor a ser recebido
    :param taxa: A taxa de reajuste a ser declarada
    :param formato: Para formatar o texto(TRUE)
    :return: Retorna o valor, formatado ou não
    """
    res = num + ((taxa / 100) * num)
    return res if not formato else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    """

    :param num: O valor a ser recebido
    :param taxa: A taxa de reajuste a ser declarada
    :param formato: Para formatar o texto(TRUE)
    :return: Retorna o valor, formatado ou não
    """
    res = num - ((taxa / 100) * num)
    return res if formato is False else moeda(res)


def moeda(preco, moeda='R$'):
    """

    :param preco: O valor para formatar
    :param moeda: A formatação
    :return: O texto formatado
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(num=0, taxaa=10, taxar=5):
    """

    :param num: Valor a ser recebido
    :param taxaa: Valor de acrescímo
    :param taxar: Valor de redução
    :return: O texto formatado
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisando: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num,True)}')
    print(f'{taxaa}% de aumento: \t{aumento(num,taxaa,True)}')
    print(f'{taxar}% de redução; \t{diminuir(num,taxar,True)}')
    print('-' * 30)
