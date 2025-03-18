import random

def gerar_dados(tamanho, nome_arquivo):
    """
    Gera um conjunto de números aleatórios e os salva em um arquivo.

    Parâmetros:
        tamanho (int): Quantidade de números a serem gerados.
        nome_arquivo (str): Nome do arquivo onde os dados serão salvos.
    """
    dados = [random.randint(1, 100000) for _ in range(tamanho)]
    with open(nome_arquivo, 'w') as f:
        for numero in dados:
            f.write(f"{numero}\n")

# Exemplo de uso
if __name__ == "__main__":
    # Gerar conjuntos de dados de diferentes tamanhos
    gerar_dados(1000, 'dados/dados_1000.txt')
    gerar_dados(10000, 'dados/dados_10000.txt')
    gerar_dados(100000, 'dados/dados_100000.txt')
    print("Dados gerados com sucesso!")