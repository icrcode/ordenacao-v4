class SelectionSort:
    def ordenar(self, dados):
        comparacoes = 0
        trocas = 0
        for i in range(len(dados)):
            indice_minimo = i
            for j in range(i+1, len(dados)):
                comparacoes += 1
                if dados[j] < dados[indice_minimo]:
                    indice_minimo = j
            if indice_minimo != i:
                dados[i], dados[indice_minimo] = dados[indice_minimo], dados[i]
                trocas += 1
        return dados, comparacoes, trocas