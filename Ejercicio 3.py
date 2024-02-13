#Escribir dos funciones que permitan calcular:
#La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, 
#convertir a horas,minutos y segundos o salir del programa.
def tiempo_a_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

def segundos_a_tiempo(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return horas, minutos, segundos

while True:
    print("Menú:")
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        horas = int(input("Ingrese las horas: "))
        minutos = int(input("Ingrese los minutos: "))
        segundos = int(input("Ingrese los segundos: "))
        total_segundos = tiempo_a_segundos(horas, minutos, segundos)
        print("El tiempo ingresado equivale a", total_segundos, "segundos.")
    elif opcion == 2:
        total_segundos = int(input("Ingrese el tiempo en segundos: "))
        horas, minutos, segundos = segundos_a_tiempo(total_segundos)
        print("El tiempo ingresado equivale a", horas, "horas,", minutos, "minutos y", segundos, "segundos.")
    elif opcion == 3:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")