#3) Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado^2).

#Valores esperados:
#área_quadrado(4) == 16
#área_quadrado(9) == 81


def areaQuadrado(lado):
    print(f"A área do quadrado com o lado {lado} é: {lado**2}")


ladoQuadrado = float(input("Informe o lado do quadrado: "))
areaQuadrado(ladoQuadrado)