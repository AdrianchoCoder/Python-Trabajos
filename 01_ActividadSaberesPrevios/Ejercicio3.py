# dadas las 3 notas de un aprendiz, calcule la definitiva de la asinatura

while True:
    try:
        n1 = int(input('Ingrese la primera nota: '))
        n2 = int(input('Ingrese la segunda nota: '))
        n3 = int(input('Ingrese la tercera nota: '))
        if n1 <= 0 or n2 <= 0 or n3 <= 0:
            raise Exception("Porfavor, Verifica que el dato ingresado sea mayor a 0...")
    except ValueError:
        print("Error, Verifica haber llenado el dato correctamente...")
    except Exception as a:
        print(a)
    else:
        definitiva = (n1 + n2 + n3) / 3
        print(f'la definitiva de sus notas es: {definitiva}')