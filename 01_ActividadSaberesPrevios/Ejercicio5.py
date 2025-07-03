# 5. Lea la distancia (en kilómetros) recorrida por un auto, el tiempo (en horas) en que la recorrió y calcule la velocidad a la cual se desplazaba el auto (V=D/T).

while True:
    try:
        distancia = float(input("Ingresa la distancia (Kilometros), recorridas por un auto: "))
        tiempo = float(input("Ingresa el tiempo (horas), en que la recorrio: "))
        if distancia <= 0 or tiempo <= 0:
            raise Exception("Porfavor, Verifica que el dato sea mayor a 0...") 
    except ValueError:
        print("Error, Verifica haber llenado Correctamente los datos...")
    except Exception as a:
        print(a)
    else:
        velocidad = distancia / tiempo
        print(f"La velocidad que recorrio fue: {velocidad}")
        break