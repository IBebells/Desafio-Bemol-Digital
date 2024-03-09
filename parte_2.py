# matriz nxn
# passo 1 - receber n
# passo 2 - montar uma matriz n x n
# posicao_rainha_atual = [x][y]

import numpy as np

def movimento_rainha(n: int, x: int, y: int, tabuleiro: list) -> list:

    soma = x + y

    for i in range(n):
        for j in range (n):

            if  i + j == soma:
                tabuleiro[i][j] = 1

    for i in range(n):
        
        tabuleiro[i][y] = 1
        tabuleiro[x][i] = 1
        
        try:
            
            tabuleiro[x + (i + 1)][y + (i + 1)] = 1 

            if x - (i + 1) >= 0 and y - (i + 1) >= 0:
                tabuleiro[x - (i + 1)][y - (i + 1)] = 1 

        except IndexError:
            pass

    return tabuleiro
            
def verifica_rainha(n):

    solucoes = 0

    for a in range(n):
        for b in range(n):

            rainhas = 1
            tabuleiro = np.zeros((n , n), dtype=np.int64)
            tabuleiro = movimento_rainha(n, a, b, tabuleiro)
            tabuleiro[a][b] = 5

            for x in range(n):
                for y in range(n):

                    if tabuleiro[x][y] == 0:
                        tabuleiro = movimento_rainha(n, x, y, tabuleiro)
                        tabuleiro[x][y] = 5
                        rainhas += 1
                        verifica_rainha(n)
                        tabuleiro[x][y] = 0
                        

                    if rainhas == n:
                        solucoes += 1
                        break
    
    print(solucoes)


if __name__ == "__main__":

    verifica_rainha(8)