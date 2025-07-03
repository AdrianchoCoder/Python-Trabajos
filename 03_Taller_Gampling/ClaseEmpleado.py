from ClasePersona import Persona

class Empleado(Persona):
    def __init__(self, nombre, telefono, email, identificacion, cargo, salario, fecha_ingreso):
        super().__init__(nombre, telefono, email, identificacion)
        self._fecha_ingreso = fecha_ingreso
        self._cargo = cargo
        self._salario = salario
        
        #Calcular Antiguedad Empleado
    def calcular_antiguedad(self):
        antiguedad = 2025 - self._fecha_ingreso
        return antiguedad
    
    def mostrar_info(self):
        # Calcular la edad y mostrarla en el print
        antiguedad = self.calcular_antiguedad()
        print(f'''\t\n---INFORMACION EMPLEADO---
    Nombre: {self._nombre}
    Telefono: {self._telefono}
    Email: {self._email}
    Identificacion: {self._identificacion}
    Identificacion: {self._cargo}
    Identificacion: {self._salario}
    Fecha de Ingreso: {self._fecha_ingreso}
    Antiguedad del empleado: {antiguedad}
    ''')
        
emmpleado_uno = Empleado("Quiros", 3042565874, "juanmanuelquirosa@gmail.com", 1020429818, "Empleado", 1400000, 2020)
emmpleado_uno.mostrar_info()