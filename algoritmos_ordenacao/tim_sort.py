class TimSort:
    def ordenar(self, dados):
        # Tamanho mínimo de uma "run" (subsequência ordenada)
        MIN_MERGE = 32

        # Função para calcular o tamanho mínimo da run
        def _calcular_min_run(n):
            r = 0
            while n >= MIN_MERGE:
                r |= n & 1
                n >>= 1
            return n + r

        # Função para ordenar uma "run" usando Insertion Sort
        def _insertion_sort(dados, esquerda, direita):
            nonlocal comparacoes, trocas
            for i in range(esquerda + 1, direita + 1):
                chave = dados[i]
                j = i - 1
                while j >= esquerda and dados[j] > chave:
                    comparacoes += 1
                    dados[j + 1] = dados[j]
                    trocas += 1
                    j -= 1
                dados[j + 1] = chave
                if j >= esquerda:
                    comparacoes += 1

        # Função para mesclar duas "runs" adjacentes
        def _merge(dados, esquerda, meio, direita):
            nonlocal comparacoes, trocas
            len1, len2 = meio - esquerda + 1, direita - meio
            esquerda_run = [0] * len1
            direita_run = [0] * len2

            # Copiar dados para as runs temporárias
            for i in range(len1):
                esquerda_run[i] = dados[esquerda + i]
            for i in range(len2):
                direita_run[i] = dados[meio + 1 + i]

            # Mesclar as runs
            i, j, k = 0, 0, esquerda
            while i < len1 and j < len2:
                comparacoes += 1
                if esquerda_run[i] <= direita_run[j]:
                    dados[k] = esquerda_run[i]
                    i += 1
                else:
                    dados[k] = direita_run[j]
                    j += 1
                trocas += 1
                k += 1

            # Copiar elementos restantes da esquerda_run, se houver
            while i < len1:
                dados[k] = esquerda_run[i]
                i += 1
                k += 1
                trocas += 1

            # Copiar elementos restantes da direita_run, se houver
            while j < len2:
                dados[k] = direita_run[j]
                j += 1
                k += 1
                trocas += 1

        # Função principal do Tim Sort
        def _tim_sort(dados):
            nonlocal comparacoes, trocas
            n = len(dados)
            min_run = _calcular_min_run(n)

            # Ordenar runs individuais de tamanho min_run usando Insertion Sort
            for esquerda in range(0, n, min_run):
                direita = min(esquerda + min_run - 1, n - 1)
                _insertion_sort(dados, esquerda, direita)

            # Mesclar as runs
            tamanho = min_run
            while tamanho < n:
                for esquerda in range(0, n, 2 * tamanho):
                    meio = min(n - 1, esquerda + tamanho - 1)
                    direita = min(n - 1, esquerda + 2 * tamanho - 1)
                    if meio < direita:
                        _merge(dados, esquerda, meio, direita)
                tamanho *= 2

        # Inicializar contadores de comparações e trocas
        comparacoes = 0
        trocas = 0

        # Executar o Tim Sort
        _tim_sort(dados)
        return dados, comparacoes, trocas