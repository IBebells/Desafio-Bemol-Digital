def fusao_ordenacao_matrizes(matriz_1: list, matriz_2: list) -> list:
    """Une e ordena as matrizes"""
    matriz_resultante = matriz_1 + matriz_2
    matriz_resultante.sort()
    return matriz_resultante

def encontra_mediana(matriz_1: list, matriz_2: list) -> float:
    """Verifica se o tamanho da matriz é impar ou par e encontra a mediana"""
    matriz_resultante = fusao_ordenacao_matrizes(matriz_1 , matriz_2)

    if len(matriz_resultante) % 2 == 0:
        posicao_ultimo_elemento_direta = int(len(matriz_resultante)/2)
        posicao_ultimo_elemento_esquerda = posicao_ultimo_elemento_direta - 1

        mediana = (matriz_resultante[posicao_ultimo_elemento_esquerda] + matriz_resultante[posicao_ultimo_elemento_direta])/2

    else:
        posicao_mediana = int((len(matriz_resultante)/2) - 0.5)
        mediana = matriz_resultante[posicao_mediana]

    return mediana

if __name__ == "__main__":
    """Exemplo encontrando a mediana de uma matriz com número impar de elementos"""
    matriz_1 = [4, 7, 2, 9, 1, 2]
    matriz_2 = [0.9, 2.3, 5.6]

    matriz = encontra_mediana(matriz_1, matriz_2)

    print(f"A mediana é igual a: {matriz}")

    """Exemplo encontrando a mediana de uma matriz com número par de elementos"""
    matriz_1 = [4, 7, 2, 9, 1, 2]
    matriz_2 = [0.9, 2.3, 5.6, 7.8]
    
    matriz = encontra_mediana(matriz_1, matriz_2)

    print(f"A mediana é igual a: {matriz}")