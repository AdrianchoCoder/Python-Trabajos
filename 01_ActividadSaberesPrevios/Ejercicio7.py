# 7. Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos equivale.

# hora = 3600
# minutos = 60
# segundos = 1

while True:
    print('''
    1. Horas, minutos a segundos
    ''')
    try:
        opc = int(input('Ingrese la opcion: '))
    except ValueError:
        print("Porfavor, Verifica haber Ingresado Correctamente la Opcion...")
    else:
        match opc:
            case 1:
                try:
                    cantidad_hora = int(input('Ingrese la cantidad de horas: '))
                    cantidad_minutos = int(input('Ingrese la cantidad de minutos: '))
                    segundos = int(input('Ingrese la cantidad de segundos: '))
                except ValueError:
                    print("Porfavor, Verifica haber Ingresado Correctamente los Datos...")
                else:
                    total_horas = print(f"La cantidad de {cantidad_hora} horas en segundos es de: {cantidad_hora * 3600}")
                    total_minutos = print(f"La cantidad de {cantidad_minutos} minutos en segundos es de: {cantidad_minutos * 60}")
                    total_segundos = (cantidad_hora * 3600) + (cantidad_minutos * 60) + segundos 
                    print(f'El registro total es equivalente a: {total_segundos} segundos.')
                    break
            case _:
                print("Ingresa una Opcion Correcta...")