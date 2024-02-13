#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
#Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))


if EsMultiplo(numero1, numero2):
    print("¡Al menos uno de los números es múltiplo del otro!")
else:
    print("Ninguno de los números es múltiplo del otro.")