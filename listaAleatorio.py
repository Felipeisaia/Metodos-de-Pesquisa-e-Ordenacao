import random
import time

def popular_lista(lista, quantidade_numeros, inicio, fim, aleatorio):
    """
    Função que popula uma lista com números aleatórios ou sequenciais dentro de uma faixa.

    Args:
        lista (list): A lista a ser populada.
        quantidade_numeros (int): A quantidade de números a serem adicionados.
        inicio (int): O valor inicial da faixa.
        fim (int): O valor final da faixa (para números aleatórios).
        aleatorio (bool): Se True, os números devem ser aleatórios.
    """
    if aleatorio:
        for _ in range(quantidade_numeros):

            lista.append(random.randint(inicio, fim))
    else:

        for i in range(inicio, quantidade_numeros):
            lista.append(i)

def exibir_lista(lista, frase):
    """
    Função que exibe o conteúdo de uma lista de inteiros.

    Args:
        lista (list): A lista a ser exibida.
        frase (str): Uma frase para exibir no início.
    """
    print(frase)
    for item in lista:
        print(item)
    print("--------------------------")
    print(f"Total de registros: {len(lista)}")

if __name__ == "__main__":
    lista_aleatoria = []
    lista_sequencial = []

    tempo_inicio = time.time()
    
    popular_lista(lista_aleatoria, 100000, 100, 100000, True)
  
    
    tempo_fim = time.time()
    duracao_ms_1 = (tempo_fim - tempo_inicio) * 1000
    print(f"Tempo (ms) rotina 1: {duracao_ms_1:.2f}")


    tempo_inicio = time.time()


    popular_lista(lista_sequencial, 100000, 1, 100000, False)
    
    tempo_fim = time.time()
    duracao_ms_2 = (tempo_fim - tempo_inicio) * 1000
    print(f"Tempo (ms) rotina 2: {duracao_ms_2:.2f}")