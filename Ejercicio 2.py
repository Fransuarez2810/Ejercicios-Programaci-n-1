#Crear una función recursiva que permita calcular el factorial de un número. 
#Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero: "))

if numero < 0:
    print("El número es negativo, no puesde sacar el factorial.")
else:
    resultado = factorial(numero)
    print("El factorial de", numero, "es:", resultado)