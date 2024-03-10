
def verifica_rainha(n: int, tabuleiro: list, linha_rainha: int, coluna_rainha: int) -> bool:
    """Realiza os ataques da rainha para verificar se há uma rainha nessas posições"""
    for linha_atual in range(linha_rainha):
        if tabuleiro[linha_atual][coluna_rainha] == 1:
            return False
    
    for linha_atual, coluna_atual in zip(range(linha_rainha, -1, -1), range(coluna_rainha, -1, -1)):
        if tabuleiro[linha_atual][coluna_atual] == 1:
            return False
    
    for linha_atual, coluna_atual in zip(range(linha_rainha, -1, -1), range(coluna_rainha, n)):
        if tabuleiro[linha_atual][coluna_atual] == 1:
            return False
    
    return True
            
def encontra_solucoes(n: int, tabuleiro: list, linha_rainha: int, solucoes: list):
    """Posiciona as rainhas no tabuleiro, e ao colocar uma rainha pula para a proxima linha.
    Realiza esse processo de forma recurssiva para encontrar todas as soluções possíveis"""
    if linha_rainha == n:
        solucoes.append([linha[:] for linha in tabuleiro]) 
        return  

    for coluna_atual in range(n):
        if verifica_rainha(n, tabuleiro, linha_rainha, coluna_atual):

            tabuleiro[linha_rainha][coluna_atual] = 1
            encontra_solucoes(n, tabuleiro, linha_rainha + 1, solucoes)

            tabuleiro[linha_rainha][coluna_atual] = 0

if __name__ == "__main__":

    n = 8  
    solucoes = []
    tabuleiro = [[0] * n for _ in range(n)]
    encontra_solucoes(n, tabuleiro, 0, solucoes)
    print(f"O número de soluções quando N é igual a {n} é {len(solucoes)}")