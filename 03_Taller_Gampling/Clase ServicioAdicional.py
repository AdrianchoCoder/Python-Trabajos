class ServicioAdicional:
    def __init__(self, nombre, descripcion, precio, duracion_horas):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._duracion_horas = duracion_horas
    
    # def get_nombre(self):
    #     return self._nombre
        
    # def get_descripcion(self):
    #     return self._descripcion
        
    # def get_precio(self):
    #     return self._precio
        
    # def get_duracion_horas(self):
    #     return self._duracion_horas

    def mostrar_info(self):
        print(f'''\n---INFORMACION SERVICIO ADICIONAL---
            Nombre: {self._nombre}
            Descripcion: {self._descripcion}
            Precio: ${self._precio:,.2f}
            Duracion: {self._duracion_horas} horas''')
# Ejemplo de uso
servicio_uno = ServicioAdicional("Spa y Relajación", "Tratamiento completo de spa con masajes y terapias de relajación", 150000, 3)
servicio_uno.mostrar_info()