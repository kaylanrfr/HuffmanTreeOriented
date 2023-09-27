from Node import Node

frase = 'testando como funciona'

arvore_huffman = Node.montarNodes(frase)

codigos = Node.gerarCodigos(arvore_huffman[0])

frase_codificada = ""
for caractere in frase:
    frase_codificada += codigos[caractere]

with open("codificada.txt", "wb") as arquivo:
    # arquivo.write(bytes(frase_codificada, encoding="utf-8"))
    arquivo.write(frase_codificada.encode("utf-8"))

print("Frase codificada:", frase_codificada)
