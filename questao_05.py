#5) Reescreva a função abaixo de forma a utilizar os métodos de 
# pesquisa em lista, vistos na aula passada. A função ‘enumerate’ recebe uma 
# lista como parâmetro e retorna uma lista de tuplas, estas formada por pares 
# (índice, valor). O valor ‘None’ é o valor nulo da linguagem Python, similar ao 
# ‘null’ de Java e JavaScript.

# def pesquise(lista, valor):
#    for x,e in enumerate(lista):
#           if e == valor:
#                  return x
# return None


def pesquisa(lista,valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None

lista = ['PW1', 'Banco de dados 2', 'Banco de dados 1']

valorPesquisa = str(input("Informe um nome a ser pesquisado: "))

valorEncontrado = pesquisa(lista,valorPesquisa)

if valorEncontrado != None:
    print(f"Lista: {lista}\nValor de busca: {valorPesquisa}\nÍndice encontrado: {valorEncontrado}")
else:
    print(f"O valor de busca não está dentro dessa lista!")
