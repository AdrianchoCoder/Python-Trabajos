# 21) Realice un algoritmo que permita realizar el cálculo del siguiente enunciado,
# se solicita el año de nacimiento del aprendiz, el nombre, la dirección, 
# se requiere conocer la edad de la persona y la información completa ingresada. 
while True:
    try:
        nacimiento = int(input("Ingresa el Año de Nacimiento: "))
        nombre = str(input("Ingresa el Nombre: "))
        direccion = str(input("Ingresa la Direccion de Residencia: "))
        edad = int(input("Ingresa Tu Edad: "))

        resultado_edad = 2025 - nacimiento
        if edad == resultado_edad:
            print(f"""\t--- ¡Tu Informacion Ha Sido Completada! ---
                Tu Fecha de Nacimiento es: {nacimiento}
                Tu Nombre es: {nombre}
                Direccion de Residencia: {direccion}
                Tu Edad es: {edad}""")
            break
        else:
            print("Error, Verifica que la Edad y la Fecha de nacimiento coincidan...")
    except ValueError:
        print("Porfavor, Verifica Haber llenado todos los Datos...")
