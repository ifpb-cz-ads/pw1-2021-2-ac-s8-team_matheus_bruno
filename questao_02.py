#   2) Escreva uma função que receba dois números e retorne True se o primeiro 
# número for múltiplo do segundo.

#   Valores esperados:
#   múltiplo(8,4) == True
#   múltiplo(7,3) == False
#   múltiplo(5,5) == True

def multiplos(numero1, numero2):
    if numero1%numero2 == 0:
        print(f"O número {numero1} é múltiplo de {numero2}")
    else:
        print(f"O número {numero1} não é múltiplo de {numero2}")

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

multiplos(numero1, numero2)
