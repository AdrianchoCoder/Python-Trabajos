class Reserva:
    def __init__(self, huesped, alojamiento, temporada, precio_total):
        self.huesped = huesped
        self.alojamiento = alojamiento
        self.temporada = temporada
        self.precio_total = precio_total

reservas = []

def calcular_precio(temporada):
    base = 100000
    if temporada == "alta":
        return base * 1.5
    elif temporada == "media":
        return base * 1.2
    elif temporada == "baja":
        return base * 0.8
    return base
