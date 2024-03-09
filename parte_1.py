# Recebe duas matrizes de tamanho nx1
# passo 1 - ordenar a matriz
# passo 2 - verificar se é impar ou par

# posicao = len(m)/2
# posicao, posicao - 1

def fusao_ordenacao_matrizes(matriz_1: list, matriz_2: list) -> list:

    matriz_resultante = matriz_1 + matriz_2
    matriz_resultante.sort()
    return matriz_resultante

def encontra_mediana(matriz_1: list, matriz_2: list) -> float:

    matriz_resultante = fusao_ordenacao_matrizes(matriz_1 , matriz_2)

    if len(matriz_resultante) % 2 == 0: #verifica se a matriz é par
        posicao_ultimo_elemento_direta = int(len(matriz_resultante)/2)
        posicao_ultimo_elemento_esquerda = posicao_ultimo_elemento_direta - 1

        mediana = (matriz_resultante[posicao_ultimo_elemento_esquerda] + matriz_resultante[posicao_ultimo_elemento_direta])/2

    else:
        posicao_mediana = int((len(matriz_resultante)/2) - 0.5)
        mediana = matriz_resultante[posicao_mediana]

    return mediana

if __name__ == "__main__":

    print(encontra_mediana([4, 7, 2, 9, 1, 2], [0.9, 2.3, 5.6]))