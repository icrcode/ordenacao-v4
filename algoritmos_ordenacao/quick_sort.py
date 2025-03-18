class QuickSort:
    def ordenar(self, dados):
        comparacoes = 0
        trocas = 0

        def _quick_sort(dados):
            nonlocal comparacoes, trocas
            if len(dados) <= 1:
                return dados
            pivot = dados[len(dados) // 2]
            left = [x for x in dados if x < pivot]
            middle = [x for x in dados if x == pivot]
            right = [x for x in dados if x > pivot]
            comparacoes += len(dados) - 1
            return _quick_sort(left) + middle + _quick_sort(right)

        dados = _quick_sort(dados)
        return dados, comparacoes, trocas