class CuentaBancaria:
    numero_cuenta_siguiente = 100001  

    def __init__(self, documento_identidad="", saldo_inicial=0.0, tasa_interes_anual=0.0):
        self._numero_cuenta_bancaria = CuentaBancaria.numero_cuenta_siguiente
        CuentaBancaria.numero_cuenta_siguiente += 1

        self._documento_identidad = documento_identidad
        self._saldo_actual = saldo_inicial
        self._tasa_interes_anual = tasa_interes_anual

    def actualizar_saldo_con_interes(self):
        tasa_interes_diario = self._tasa_interes_anual / 365
        interes_ganado = self._saldo_actual * (tasa_interes_diario / 100)
        self._saldo_actual += interes_ganado

    def depositar_dinero(self, monto_deposito):
        if monto_deposito > 0:
            self._saldo_actual += monto_deposito
            print(f"Se ingresaron ${monto_deposito:.2f} correctamente.")
        else:
            print("La cantidad debe ser positiva.")

    def retirar_dinero(self, monto_retiro):
        if monto_retiro <= self._saldo_actual:
            self._saldo_actual -= monto_retiro
            print(f"Se retiraron ${monto_retiro:.2f} correctamente.")
        else:
            print("Saldo insuficiente.")

    def mostrar_informacion_cuenta(self):
        print("\nDATOS DE LA CUENTA ")
        print(f"Número de cuenta: {self._numero_cuenta_bancaria}")
        print(f"DNI del cliente: {self._documento_identidad}")
        print(f"Saldo actual: ${self._saldo_actual:.2f}")
        print(f"Interés anual: {self._tasa_interes_anual:.2f}%")


def crear_nueva_cuenta():
    documento_cliente = input("Ingrese el documento de identidad (DNI): ")
    saldo_inicial_cuenta = float(input("Ingrese el saldo inicial: "))
    porcentaje_interes = float(input("Ingrese el interés anual (%): "))
    cuenta_nueva = CuentaBancaria(documento_cliente, saldo_inicial_cuenta, porcentaje_interes)
    print("\nCuenta creada correctamente.")
    return cuenta_nueva


def mostrar_menu_principal():
    cuenta_cliente = crear_nueva_cuenta()

    while True:
        print("""
 MENÚ DE CUENTA BANCARIA 
1. Mostrar datos de la cuenta
2. Ingresar dinero
3. Retirar dinero
4. Actualizar saldo con interés diario
5. Salir
""")
        opcion_seleccionada = input("Seleccione una opción: ")

        if opcion_seleccionada == "1":
            cuenta_cliente.mostrar_informacion_cuenta()
        elif opcion_seleccionada == "2":
            cantidad_deposito = float(input("Ingrese la cantidad a ingresar: "))
            cuenta_cliente.depositar_dinero(cantidad_deposito)
        elif opcion_seleccionada == "3":
            cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
            cuenta_cliente.retirar_dinero(cantidad_retiro)
        elif opcion_seleccionada == "4":
            cuenta_cliente.actualizar_saldo_con_interes()
            print("Saldo actualizado con interés diario.")
        elif opcion_seleccionada == "5":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    mostrar_menu_principal()