from random import randint, shuffle


def gerar_participantes_e_jogadas(quantidade_participante, numeros_a_serem_sorteados):
    pessoas = ['Miguel', 'Davi', 'Arthur', 'Pedro', 'Gabriel', 'Bernardo', 'Lucas', 'Matheus', 'Rafael', 'Heitor',
               'Sophia', 'Alice', 'Julia', 'Isabella', 'Manuela', 'Luiza', 'Valentina', 'Giovanna', 'Maria', 'Eduarda']
    shuffle(pessoas)
    participantes = {}
    for jogador in range(quantidade_participante):
        if jogador < len(pessoas):
            participantes[pessoas[jogador]] = gerar_lista_numeros_aleatorios(numeros_a_serem_sorteados)
        else:
            print(f'Máximo de {jogador} pessoas atingido!')
            break
    if quantidade_participante <= 0:
        print('Impossível continuar sem participantes!')
        exit()
    return participantes


def gerar_lista_numeros_aleatorios(tamanho_lista):
    minimo = 1
    maximo = 20
    numeros = []

    while len(numeros) - 1 < tamanho_lista:
        n_aleatorio = randint(minimo, maximo)
        if n_aleatorio not in numeros:
            numeros.append(n_aleatorio)
        if len(numeros) - 1 == (maximo - minimo):
            break
    return numeros


def gerar_resultado(quantidade_de_numeros):
    return gerar_lista_numeros_aleatorios(quantidade_de_numeros)


def gerar_premiacao(participantes, resultado_final, premiacao):
    acertos = gerar_quantidade_acertos(participantes, resultado_final)
    grupo_de_acertos = gerar_grupo_vencedores(acertos)

    premiados = {}

    acertos_12 = grupo_de_acertos['12 Acertos']
    acertos_11 = grupo_de_acertos['11 Acertos']
    acertos_10 = grupo_de_acertos['10 Acertos']

    if len(acertos_12) > 0:
        premio = premiacao / len(acertos_12)
        for acertou_12 in acertos_12:
            premiados[acertou_12] = premio
            premiacao -= premio

    elif len(acertos_11) > 0:
        premiacao *= 0.90
        premio = premiacao / len(acertos_11)
        for acertou_11 in acertos_11:
            premiados[acertou_11] = premio
            premiacao -= premio

    elif len(acertos_10) > 0:
        premiacao *= 0.80
        premio = premiacao / len(acertos_10)
        for acertou_10 in acertos_10:
            premiados[acertou_10] = premio
            premiacao -= premio

    return premiados


def gerar_quantidade_acertos(participantes, resultado_final):
    resultados_contados = {}
    for nome, aposta in participantes.items():
        acertos = 0
        for numero in resultado_final:
            if aposta.count(numero) != 0:
                acertos += 1
        resultados_contados[nome] = acertos
    return resultados_contados


def gerar_grupo_vencedores(partipantes):
    vencedores = {
        '12 Acertos': [],
        '11 Acertos': [],
        '10 Acertos': []
    }
    for pessoa, qtd_acerto in partipantes.items():
        if qtd_acerto == 12:
            vencedores['12 Acertos'].append(pessoa)
        elif qtd_acerto == 11:
            vencedores['11 Acertos'].append(pessoa)
        elif qtd_acerto == 10:
            vencedores['10 Acertos'].append(pessoa)

    return vencedores


if __name__ == '__main__':
    premio = 100000
    integrantes_do_grupo = ['Pedro Henrique Nunes', 'Luiz Fernando Rodrigues Lemos', 'Gabriel Yago Barbosa']
    print('Desenvolvedores: ', integrantes_do_grupo[0], ',', integrantes_do_grupo[1], ',', integrantes_do_grupo[2])

    jogadores = int(input('Quantidade de Pessoas: '))
    QTD_NUMEROS_SORTEADOS = 12
    todos_os_participantes = gerar_participantes_e_jogadas(jogadores, QTD_NUMEROS_SORTEADOS)
    resultado = gerar_resultado(QTD_NUMEROS_SORTEADOS)
    vencedores = gerar_premiacao(todos_os_participantes, resultado, premio)
    if len(vencedores.values()) > 0:
        print('Parabens para os seguintes participantes!')
        for n, p in vencedores.items():
            print(f'Sr(a) {n} pelo prémio de R$ {p:.2f} reais!')
    else:
        print('Infelizmente ninguém ganhou.')

    """
    Complemento de recursos exigidos pelo professor que não tiveram funcionalidades no codio principal.
    """
    todos_participantes = list(todos_os_participantes.keys())
    vencedorees = list(vencedores.keys())
    for v in vencedorees:
        try:
            todos_participantes.pop(todos_participantes.index(v))
        except:
            pass
    todos_participantes.sort()
    todos_participantes.insert(0, integrantes_do_grupo)
    todos_participantes.pop(0)

    for nome in todos_participantes:
        print('Parabens pela tentativa Sr(a)', nome, ', mais sorte na proxima vez!')

    todos_participantes.extend(['\nObrigado por participarem!'])
    print(todos_participantes[todos_participantes.index('\nObrigado por participarem!')])
    print('Curiosidade, existem', todos_participantes.count('Maria'), 'Maria participando')
    todos_participantes_2 = todos_participantes.copy()
    todos_participantes_2.reverse()
    todos_participantes_2.remove(todos_participantes[0])
    todos_participantes_2.clear()