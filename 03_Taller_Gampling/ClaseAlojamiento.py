class Alojamiento:
    def __init__(self, numero, tipo, capacidad_maxima, precio_base_noche, amenidades=None):
        self.__numero = numero
        self.__tipo = tipo
        self.__capacidad_maxima = capacidad_maxima
        self.__precio_base_noche = precio_base_noche
        self.__amenidades = amenidades if amenidades else []
        self.__disponible = True


    # Métodos de negocio
    def calcular_precio_temporada(self, temporada):
        if temporada == "alta":
            return self.__precio_base_noche * 1.5
        elif temporada == "media":
            return self.__precio_base_noche * 1.2
        elif temporada == "baja":
            return self.__precio_base_noche * 0.8
        else:
            return self.__precio_base_noche

    def reservar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def liberar(self):
        if not self.__disponible:
            self.__disponible = True
            return True
        return False

    def mostrar_info(self):
        estado = "Disponible" if self.__disponible else "Reservado"
        print(f"Alojamiento #{self.__numero}")
        print(f"Tipo: {self.__tipo}")
        print(f"Capacidad: {self.__capacidad_maxima} personas")
        print(f"Precio base: ${self.__precio_base_noche}")
        print(f"Amenidades: {', '.join(self.__amenidades)}")
        print(f"Estado: {estado}")


# Ejemplo de uso
cabana = Alojamiento(101, "cabaña", 4, 150000, ["wifi", "jacuzzi", "chimenea"])
cabana.mostrar_info()
print(f"Precio temporada alta: ${cabana.calcular_precio_temporada('alta')}")
