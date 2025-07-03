class Persona:
    def __init__(self, nombre, telefono, email, identificacion):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._identificacion = identificacion
    #Get y Set de Nombre
    # def get_nombre(self):
    #     print(self._nombre)
    # def set_nombre(self, nombre):
    #     self.__nombre = nombre

    #Get y Set de Telefono
    # def get_telefono(self):
    #     print(self._telefono)
    # def set_telefono(self, telefono):
    #     self.__telefono = telefono

    #Get y Set de Email
    # def get_email(self):
    #     print(self._email)
    # def set_email(self, email):
    #     self.__email = email

    #Get y Set de Identificacion
    # def get_identificacion(self):
    #     print(self._identificacion)
    # def set_identificacion(self, identificacion):
    #     self.__identificacion = identificacion

    #Mostrar Informacion del Usuario
    def mostrar_info(self):
        print(f'''INFORMACION USUARIO\nNombre: {self._nombre}\nTelefono: {self._telefono}\nEmail: {self._email}\nIdentificacion: {self._identificacion}''')

#Objeto Persona Uno
per_uno = Persona("Adrian", 3195939437, "adriandaguirrej@gmail.com", 1017281748)

#Informacion de la Persona
per_uno.mostrar_info()