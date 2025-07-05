from reserva import reservas

def calcular_ingresos():
    return sum([r.precio_total for r in reservas])
