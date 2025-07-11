##### EP - GIT ###
# Ao implementar uma função, dê commit no github usando os comandos vistos no workshop!
# Implemente uma função de cada vez, e dê commit em uma função por vez.
# NOME:


def minimo(arr):
    menor = arr[0]

    for elemento in arr[1:]:
        if elemento < menor:
            menor = elemento





    return menor 

def maximo(arr):

    maior = arr[0]

    for elemento in arr[1:]:
        if elemento > maior:
            maior = elemento

    return maior

    

def meio(arr):
    
    return arr[len(arr) // 2]

def media(arr):
    
    soma = 0

    for x in range(0, len(arr)):
        soma = soma + arr[x]

    return soma / len(arr)

def moda(arr):
    # retorna o valor que mais se repete no array
    return

def soma(arr, n = 1):
    # soma n a todos os valores do array e retorna o novo array
    # exemplo
    # entrada: arr = [1, 1, 1], n = 5
    # saida: arr = [6, 6, 6]
    return 

def subtracao(arr, n):
    # subtrai n em todos os valores do array e retorna o novo array
    # exemplo
    # entrada: arr = [1, 1, 1], n = 5
    # saida: arr = [-4, -4, -4]
    return

def soma_arr(arr1, arr2):
    # soma de dois arrays elemento-a-elemento e retorna
    return

def produto_interno(arr1, arr2):
    # retorna o produto interno entre dois vetores
    return
