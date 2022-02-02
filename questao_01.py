#1) Escreva uma função que retorne o maior de dois números. Valores esperados:

#máximo(5,6) == 6
#máximo(2,1) == 2
#máximo(7,7) == 7

def maiorValor(numero1, numero2):
    print(f"O maior número é: {max(numero1,numero2)}" )

numero1 = int(input('Informe o primeiro número:'))
numero2 = int(input('Informe o segundo número: '))

maiorValor(numero1,numero2)


