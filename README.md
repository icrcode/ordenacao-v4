# Projeto de Comparação de Algoritmos de Ordenação

Este projeto tem como objetivo implementar, comparar e analisar a performance de diferentes algoritmos de ordenação, utilizando o padrão de projeto **Strategy** para modularidade e **OpenTelemetry** para coleta de métricas e logs.

---

## Algoritmos Implementados

- **Básicos**:
  - Bubble Sort
  - Bubble Sort Melhorado
  - Insertion Sort
  - Selection Sort

- **Avançados (Dividir para Conquistar)**:
  - Quick Sort
  - Merge Sort
  - Tim Sort

---

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado:
- Python 3.8 ou superior.
- Gerenciador de pacotes `pip`.

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/comparacao-algoritmos-ordenacao.git
   cd comparacao-algoritmos-ordenacao
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
##  Como Executar o Projeto
1. Gerar Dados Aleatórios

Execute o script gerador_dados.py para gerar conjuntos de números aleatórios:

    python gerador_dados.py

2. Executar os Algoritmos de Ordenação

Execute o script main.py para rodar todos os algoritmos de ordenação e coletar métricas de desempenho:

    python main.py

O que acontece:

- Os algoritmos são executados para cada conjunto de dados.

- Métricas como tempo de execução, comparações e trocas são coletadas.

- Logs são registrados usando o OpenTelemetry.
3. Visualizar Logs e Métricas

Os logs são registrados no console e podem ser enviados para o Jaeger para visualização.
Configuração do Jaeger:

### Inicie o Jaeger usando Docker:
    docker run -d --name jaeger \
      -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \
      -p 5775:5775/udp \
      -p 6831:6831/udp \
      -p 6832:6832/udp \
      -p 5778:5778 \
      -p 16686:16686 \
      -p 14268:14268 \
      -p 9411:9411 \
      jaegertracing/all-in-one:1.21
#### Acesse o Jaeger no navegador:
    http://localhost:16686
Procure pelos traces gerados pelo projeto.

## Resultados

Após a execução, os resultados serão exibidos no console e registrados no Jaeger. Eles incluem:

- Tempo de execução (em milissegundos).

- Número de comparações realizadas.

- Número de trocas/movimentações realizadas.