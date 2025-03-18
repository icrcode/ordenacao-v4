import time
from algoritmos_ordenacao import estrategias

def carregar_dados(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return [int(linha) for linha in f]

def executar_algoritmo(estrategia, dados):
    inicio = time.time()
    dados_ordenados, comparacoes, trocas = estrategia.ordenar(dados.copy())
    fim = time.time()
    tempo_execucao = (fim - inicio) * 1000  # Convertendo para milissegundos
    return tempo_execucao, comparacoes, trocas

def comparar_algoritmos(nome_arquivo, repeticoes=5):
    dados = carregar_dados(nome_arquivo)
    resultados = {}

    for nome, estrategia in estrategias.items():
        tempos = []
        comparacoes_total = 0
        trocas_total = 0

        for _ in range(repeticoes):
            tempo, comparacoes, trocas = executar_algoritmo(estrategia, dados)
            tempos.append(tempo)
            comparacoes_total += comparacoes
            trocas_total += trocas

        # Calcular médias
        tempo_medio = sum(tempos) / repeticoes
        comparacoes_media = comparacoes_total / repeticoes
        trocas_media = trocas_total / repeticoes

        resultados[nome] = {
            "tempo_medio": tempo_medio,
            "comparacoes_media": comparacoes_media,
            "trocas_media": trocas_media,
        }

    return resultados