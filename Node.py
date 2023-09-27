class Node:
    def __init__(self, frequencia, caractere, esquerda=None, direita=None):
        self.frequencia = frequencia
        self.caractere = caractere
        self.esquerda = esquerda
        self.direita = direita
        self.codigo = ''

    @staticmethod
    def gerarCodigos(node, codigo=''):
        codigoConcatenado = codigo + node.codigo
        caracteresECodigos = {}  
        if node.esquerda:
            caracteresECodigos.update(Node.gerarCodigos(node.esquerda, codigoConcatenado))
        if node.direita:
            caracteresECodigos.update(Node.gerarCodigos(node.direita, codigoConcatenado))
        if not node.esquerda and not node.direita:
            caracteresECodigos[node.caractere] = codigoConcatenado
        return caracteresECodigos
    
    @staticmethod
    def montarNodes(frase):
        frequenciaCaracteres = {}
        arrayNode = []

        for caractere in frase:
            if caractere not in frequenciaCaracteres:
                frequenciaCaracteres[caractere] = 1
            else:
                frequenciaCaracteres[caractere] += 1

        frequenciaCaracteres = {k: v for k, v in sorted(frequenciaCaracteres.items(), key=lambda item: item[1])}

        for i in range(0, len(frequenciaCaracteres)):
            arrayNode.append(Node(frequenciaCaracteres[list(frequenciaCaracteres.keys())[i]], list(frequenciaCaracteres.keys())[i]))

        while len(arrayNode) > 1:
            node = Node(arrayNode[0].frequencia + arrayNode[1].frequencia,
                        arrayNode[0].caractere + arrayNode[1].caractere,
                        arrayNode[0], arrayNode[1])
            arrayNode[0].codigo = '0'
            arrayNode[1].codigo = '1'
            for i in range(len(arrayNode) - 1, 0, -1):
                if node.frequencia >= arrayNode[i].frequencia:
                    arrayNode.insert(i + 1, node)
                    break
            arrayNode.pop(0)
            arrayNode.pop(0)

        return arrayNode


