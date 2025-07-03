class MaquinaCafe:
    def __init__(self, volumen_maximo_litros=1000, volumen_actual_litros=0):
        self.volumen_maximo_litros = volumen_maximo_litros
        if volumen_actual_litros > volumen_maximo_litros:
            self.volumen_actual_litros = volumen_maximo_litros
        else:
            self.volumen_actual_litros = volumen_actual_litros

    def llenar_deposito_completo(self):
        self.volumen_actual_litros = self.volumen_maximo_litros
        print("La cafetera se llenó completamente.")

    def dispensar_taza_cafe(self, capacidad_taza_cc):
        if self.volumen_actual_litros >= capacidad_taza_cc:
            self.volumen_actual_litros -= capacidad_taza_cc
            print(f"Taza de {capacidad_taza_cc} c.c. servida completamente.")
        else:
            print(f"No hay suficiente café. Solo se sirvieron {self.volumen_actual_litros} c.c.")
            self.volumen_actual_litros = 0

    def vaciar_deposito_cafe(self):
        self.volumen_actual_litros = 0
        print("La cafetera se ha vaciado.")

    def anadir_cafe_deposito(self, volumen_agregar_cc):
        if volumen_agregar_cc <= 0:
            print("No se puede agregar una cantidad negativa o cero.")
            return

        volumen_total_resultante = self.volumen_actual_litros + volumen_agregar_cc
        if volumen_total_resultante > self.volumen_maximo_litros:
            volumen_desperdiciado = volumen_total_resultante - self.volumen_maximo_litros
            print(f"La cafetera se llenó. Se desperdiciaron {volumen_desperdiciado} c.c.")
            self.volumen_actual_litros = self.volumen_maximo_litros
        else:
            self.volumen_actual_litros += volumen_agregar_cc
            print(f"Se agregaron {volumen_agregar_cc} c.c. de café a la cafetera.")

    def mostrar_estado_actual(self):
        print(f"\nCapacidad máxima: {self.volumen_maximo_litros} c.c.")
        print(f"Cantidad actual: {self.volumen_actual_litros} c.c.\n")


def ejecutar_programa_cafetera():
    print("Inicializando cafetera...")
    maquina_cafe_principal = MaquinaCafe() 

    while True:
        print("""
--- MENÚ DE CAFETERA ---
1. Llenar cafetera
2. Servir taza
3. Vaciar cafetera
4. Agregar café
5. Mostrar estado
6. Salir
""")
        opcion_menu_seleccionada = input("Seleccione una opción: ")

        if opcion_menu_seleccionada == "1":
            maquina_cafe_principal.llenar_deposito_completo()
        elif opcion_menu_seleccionada == "2":
            tamano_taza_solicitada = int(input("Tamaño de la taza en c.c.: "))
            maquina_cafe_principal.dispensar_taza_cafe(tamano_taza_solicitada)
        elif opcion_menu_seleccionada == "3":
            maquina_cafe_principal.vaciar_deposito_cafe()
        elif opcion_menu_seleccionada == "4":
            cantidad_cafe_agregar = int(input("Cantidad de café a agregar: "))
            maquina_cafe_principal.anadir_cafe_deposito(cantidad_cafe_agregar)
        elif opcion_menu_seleccionada == "5":
            maquina_cafe_principal.mostrar_estado_actual()
        elif opcion_menu_seleccionada == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_programa_cafetera()