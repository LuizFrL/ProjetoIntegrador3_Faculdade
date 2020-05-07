from random import randint, shuffle


def gerar_participantes_e_jogadas(quantidade_participante, numeros_a_serem_sorteados):
    pessoas = ['Miguel', 'Davi', 'Arthur', 'Pedro', 'Gabriel', 'Bernardo', 'Lucas', 'Matheus', 'Rafael', 'Heitor',
               'Sophia', 'Alice', 'Julia', 'Isabella', 'Manuela', 'Luiza', 'Valentina', 'Giovanna', 'Maria', 'Eduarda']
    shuffle(pessoas)
    participantes = {}
    for pessoa in range(quantidade_participante):
        if pessoa < len(pessoas):
            participantes[pessoas[pessoa]] = gerar_lista_numeros_aleatorios(numeros_a_serem_sorteados)
        else:
            print(f'Máximo de {pessoa} pessoas atingido!')
            break
    if quantidade_participante <= 0:
        print('Impossível continuar sem participantes!')
        exit()
    return participantes


def gerar_lista_numeros_aleatorios(tamanho_lista):
    minimo = 0
    maximo = 60
    numeros = []

    while len(numeros) < tamanho_lista:
        n_aleatorio = randint(minimo, maximo)
        if n_aleatorio not in numeros:
            numeros.append(n_aleatorio)
        if len(numeros) == (maximo - minimo):
            break
    return numeros


def gerar_resultado(quantidade_de_numeros):
    return gerar_lista_numeros_aleatorios(quantidade_de_numeros)


def gerar_premiacao(participantes, resultado_final, premiacao):
    acertos = gerar_quantidade_acertos(participantes, resultado_final)
    return acertos


def gerar_quantidade_acertos(participantes, resultado_final):
    resultados_contados = {}
    for nome, aposta in participantes.items():
        acertos = 0
        for numero in resultado_final:
            if numero in aposta:
                acertos += 1
        resultados_contados[nome] = round(acertos / len(resultado_final), 2) * 100

    return resultados_contados


if __name__ == '__main__':
    premio = 100000
    jogadores = int(input('Quantidade de Pessoas: '))
    qtd_numeros_sorteados = 12
    todos_os_participantes = gerar_participantes_e_jogadas(jogadores, qtd_numeros_sorteados)
    resultado = gerar_resultado(qtd_numeros_sorteados)
    vencedores = gerar_premiacao(todos_os_participantes, resultado, premio)

    for n, p in vencedores.items():
        print(n, p)
