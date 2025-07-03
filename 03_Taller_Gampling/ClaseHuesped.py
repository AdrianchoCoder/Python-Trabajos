from ClasePersona import Persona

class Huesped(Persona):
    def __init__(self, nombre, telefono, email, identificacion, fecha_nacimiento, pais_origen, preferencias_alimentarias):
        super().__init__(nombre, telefono, email, identificacion)
    
        self._fecha_nacimiento = fecha_nacimiento
        self._pais_origen = pais_origen
        self._preferencias_alimentarias = preferencias_alimentarias
        
    # def get_fecha_nacimiento(self):
    #     return self._fecha_nacimiento
        
    # def get_pais_origen(self):
    #     return self._pais_origen
        
    # def get_preferencias_alimentarias(self):
    #     return self._preferencias_alimentarias

    def calcular_edad(self):
        # Calcular la edad sin modificar fecha_nacimiento
        edad_actual = 2025 - self._fecha_nacimiento
        return edad_actual
    
    def mostrar_info(self):
        # Calcular la edad y mostrarla en el print
        edad = self.calcular_edad()
        print(f'''\n---INFORMACION HUESPED---
            Nombre: {self._nombre}
            Telefono: {self._telefono}
            Email: {self._email}
            Identificacion: {self._identificacion}
            Fecha de Nacimiento: {self._fecha_nacimiento}
            Edad Actual: {edad} años
            Pais de Origen: {self._pais_origen}
            Preferencias Alimentarias: {self._preferencias_alimentarias}''')
        
huesped_uno = Huesped("Adrian", 3195939437, "adriandaguirrej@gmail.com", 1017281748, 1999, "Venezuela", "Arepa venezolana")
huesped_uno.mostrar_info()

