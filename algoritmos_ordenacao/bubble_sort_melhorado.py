class BubbleSortMelhorado:
    def ordenar(self, dados):
        n = len(dados)
        comparacoes = 0
        trocas = 0
        for i in range(n):
            trocou = False
            for j in range(0, n-i-1):
                comparacoes += 1
                if dados[j] > dados[j+1]:
                    dados[j], dados[j+1] = dados[j+1], dados[j]
                    trocas += 1
                    trocou = True
            if not trocou:
                break
        return dados, comparacoes, trocas