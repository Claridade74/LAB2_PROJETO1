def cumprimento(texto):
    return(f'Olá, {texto}')

nome = "Clarissa Treptow"
resultado = cumprimento(nome)
resultado

import random

def media_numeros_aleatorios():
    numeros = [random.randint(0, 1000) for i in range(3)]
    media = sum(numeros) / len(numeros)
    return media, numeros

media, numeros_sorteados = media_numeros_aleatorios()
media, numeros_sorteados