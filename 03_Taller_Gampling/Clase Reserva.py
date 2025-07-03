class Reserva:
    def __init__(self, codigo_reserva, huesped, alojamiento, fecha_checkin, fecha_checkout):
        self._codigo_reserva = codigo_reserva
        self._huesped = huesped
        self._alojamiento = alojamiento
        self._fecha_checkin = fecha_checkin
        self._fecha_checkout = fecha_checkout
        self._servicios_adicionales = []
        self._precio_total = 0.0
        self._estado = "confirmada"
    
    def calcular_noches(self):
        noches = self._fecha_checkout - self._fecha_checkin
        return noches
    
    def agregar_servicio(self, servicio):
        self._servicios_adicionales.append(servicio)
    
    def calcular_precio_total(self, temporada):
        # Calcular precio del alojamiento por noche según temporada
        noches = self.calcular_noches()
        
        if temporada.lower() == "alta":
            precio_alojamiento = self._alojamiento._precio_por_noche * 1.5 * noches
        elif temporada.lower() == "media":
            precio_alojamiento = self._alojamiento._precio_por_noche * 1.2 * noches
        else:  # temporada baja
            precio_alojamiento = self._alojamiento._precio_por_noche * noches
        
        # Calcular precio de servicios adicionales
        precio_servicios = 0
        for servicio in self._servicios_adicionales:
            precio_servicios += servicio._precio
        
        # Calcular precio total
        self._precio_total = precio_alojamiento + precio_servicios
        return self._precio_total
    
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["confirmada", "en_curso", "finalizada", "cancelada"]
        if nuevo_estado in estados_validos:
            self._estado = nuevo_estado
        else:
            print(f"Estado '{nuevo_estado}' no válido. Estados válidos: {estados_validos}")
    
    def mostrar_info(self):
        print(f'''\n---INFORMACION RESERVA---
            Codigo de Reserva: {self._codigo_reserva}
            Estado: {self._estado}
            Fecha Check-in: {self._fecha_checkin}
            Fecha Check-out: {self._fecha_checkout}
            Numero de Noches: {self.calcular_noches()}
            Precio Total: ${self._precio_total:,.2f}''')
        
        print("\n--- DATOS DEL HUESPED ---")
        self._huesped.mostrar_info()
        
        print("\n--- DATOS DEL ALOJAMIENTO ---")
        self._alojamiento.mostrar_info()
        
        if self._servicios_adicionales:
            print("\n--- SERVICIOS ADICIONALES ---")
            for i, servicio in enumerate(self._servicios_adicionales, 1):
                print(f"\nServicio {i}:")
                servicio.mostrar_info()
        else:
            print("\n--- SERVICIOS ADICIONALES ---")
            print("No hay servicios adicionales contratados")