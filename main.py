from executar_algoritmo import comparar_algoritmos
from registrar_logs import registrar_logs

# Arquivo de dados
nome_arquivo = "dados/dados_1000.txt"

# Comparar algoritmos
resultados = comparar_algoritmos(nome_arquivo, repeticoes=5)

# Registrar logs e exibir resultados
for nome, metricas in resultados.items():
    registrar_logs(
        nome_algoritmo=nome,
        tamanho_dados=1000,
        tempo_execucao=metricas["tempo_medio"],
        comparacoes=metricas["comparacoes_media"],
        trocas=metricas["trocas_media"],
    )