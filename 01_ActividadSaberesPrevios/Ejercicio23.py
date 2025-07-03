# 23) Una persona tarda 5 horas en subir una montaña de 7 metros, 
# si un escalador desea subir más o menos de la montaña, cuanto tiempo tarda en subir. 
# Debe de resolver el ejercicio. 
tasa_subida = 7 / 5 

print(f"La tasa de Subida es de: {tasa_subida}Metros/Horas")
altura = float(input("Ingrese la altura que desea subir (en metros): "))

tiempo = altura / tasa_subida

print(f"El escalador tardará aproximadamente {tiempo:.2f} horas en subir {altura} metros.")
