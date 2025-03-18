class MergeSort:
    def ordenar(self, dados):
        comparacoes = 0
        trocas = 0

        def _merge_sort(dados):
            nonlocal comparacoes, trocas
            if len(dados) <= 1:
                return dados
            meio = len(dados) // 2
            esquerda = _merge_sort(dados[:meio])
            direita = _merge_sort(dados[meio:])
            return _merge(esquerda, direita)

        def _merge(esquerda, direita):
            nonlocal comparacoes, trocas
            resultado = []
            i = j = 0
            while i < len(esquerda) and j < len(direita):
                comparacoes += 1
                if esquerda[i] < direita[j]:
                    resultado.append(esquerda[i])
                    i += 1
                else:
                    resultado.append(direita[j])
                    j += 1
                trocas += 1
            resultado.extend(esquerda[i:])
            resultado.extend(direita[j:])
            return resultado

        dados = _merge_sort(dados)
        return dados, comparacoes, trocas