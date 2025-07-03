# Clase Alojamiento (tu versión)
class Alojamiento:
    def __init__(self, numero, tipo, capacidad_maxima, precio_base_noche, amenidades=None):
        self.__numero = numero
        self.__tipo = tipo
        self.__capacidad_maxima = capacidad_maxima
        self.__precio_base_noche = precio_base_noche
        self.__amenidades = amenidades if amenidades else []
        self.__disponible = True

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
        print(f"Precio base por noche: ${self.__precio_base_noche}")
        print(f"Amenidades: {', '.join(self.__amenidades)}")
        print(f"Estado: {estado}")

# Clase Glamping
class Glamping:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alojamientos = []

    def registrar_alojamiento(self, alojamiento):
        self.alojamientos.append(alojamiento)

    def mostrar_alojamientos(self):
        print(f"\nListado de alojamientos en {self.nombre}:")
        if not self.alojamientos:
            print("No hay alojamientos registrados.")
        for alojamiento in self.alojamientos:
            alojamiento.mostrar_info()
            print("-" * 40)

# Prueba del sistema
if __name__ == "__main__":
    # Crear glamping
    mi_glamping = Glamping("EcoParadise Glamping")

    # Crear alojamientos
    cabaña = Alojamiento(1, "Cabaña", 4, 120, ["WiFi", "Chimenea", "Baño privado"])
    domo = Alojamiento(2, "Domo", 2, 150, ["Vista panorámica", "Jacuzzi"])
    tienda_lujo = Alojamiento(3, "Tienda de lujo", 3, 100, ["Cama queen", "Mini bar"])

    # Registrar alojamientos
    mi_glamping.registrar_alojamiento(cabaña)
    mi_glamping.registrar_alojamiento(domo)
    mi_glamping.registrar_alojamiento(tienda_lujo)

    # Mostrar alojamientos
    mi_glamping.mostrar_alojamientos()
