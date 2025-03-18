class InsertionSort:
    def ordenar(self, dados):
        comparacoes = 0
        trocas = 0
        for i in range(1, len(dados)):
            chave = dados[i]
            j = i - 1
            while j >= 0 and chave < dados[j]:
                comparacoes += 1
                dados[j + 1] = dados[j]
                trocas += 1
                j -= 1
            dados[j + 1] = chave
        return dados, comparacoes, trocas