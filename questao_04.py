#4) Escreva uma função que receba a base e a altura de um triângulo e retorne sua área 
# (A = (base x altura)/2).

#Valores esperados:
#área_triângulo(6, 9) == 27
#área_triângulo(5, 8) == 20

def areaTriangulo(base, altura):
    print(f"A área do triangulo é: {(base*altura)/2}")


baseTriangulo = float(input("Informe a base do triângulo: "))
alturaTriangulo = float(input("Informe a altura do triângulo: "))

areaTriangulo(baseTriangulo, alturaTriangulo)