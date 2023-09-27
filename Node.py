class Node:
    def __init__(self, frequencia, caractere, folhaEsquerda = None, folhaDireita = None):
        self.frequencia = frequencia
        self.caractere = caractere
        self.folhaEsquerda = folhaEsquerda
        self.folhaDireita = folhaDireita
        self.codigo = ''

    @staticmethod
    def printNodes(node, codigo = ''):
        codigoConcatenado = codigo + str(node.codigo)
        if(node.folhaEsquerda):
            Node.printNodes(node.folhaEsquerda, codigoConcatenado)
        if(node.folhaDireita):
            Node.printNodes(node.folhaDireita, codigoConcatenado)
        if(not node.folhaEsquerda and not node.folhaDireita):
            print(f"{node.caractere} -> {codigoConcatenado}")
            
    @staticmethod
    def montarArvore(frase):
        arrayLetras = {}
        arrayNode = []

        for i in frase:
            if i not in arrayLetras:
                arrayLetras[i] = 1
            else:
                arrayLetras[i]+=1
        arrayLetras = {k: v for k, v in sorted(arrayLetras.items(), key=lambda item: item[1])}


        for i in range (0, len(arrayLetras)):
            arrayNode.append(Node(arrayLetras[list(arrayLetras.keys())[i]], list(arrayLetras.keys())[i]))
    
        while (len(arrayNode)>1):
            node = Node(arrayNode[0].frequencia + arrayNode[1].frequencia, arrayNode[0].caractere + arrayNode[1].caractere, arrayNode[0], arrayNode[1])
            arrayNode[0].codigo = 0
            arrayNode[1].codigo = 1
            for i in range(len(arrayNode)-1, 0, -1):
                if(node.frequencia >= arrayNode[i].frequencia):
                    arrayNode.insert(i + 1, node)
                    break
            arrayNode.pop(0)
            arrayNode.pop(0)

        return arrayNode
