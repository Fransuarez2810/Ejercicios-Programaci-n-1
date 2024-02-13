#Diseñar una función que calcule el área y el perímetro de una circunferencia. 
#Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
import math

def calcular_circunferencia(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input("Ingrese el radio de la circunferencia: "))

if radio < 0:
    print("El radio no puede ser un valor negativo.")
else:
    area, perimetro = calcular_circunferencia(radio)
    print("El área de la circunferencia es:", area)
    print("El perímetro de la circunferencia es:", perimetro)