try:
    capital = float(input("Ingrese el capital a invertir: "))
    meses = int(input("Ingrese el número de meses: "))

    if capital < 0 or meses < 1:
        print("Por favor ingrese valores válidos (capital positivo y al menos 1 mes).")
    else:
        mes = 1

        while mes <= meses:
            ganancia = capital * 0.02
            capital += ganancia
            print(f"Mes {mes}: Ganancia = {ganancia:.2f}, Total = {capital:.2f}")
            mes += 1

except ValueError:
    print("Error: Ingrese solo números válidos (por ejemplo: 1000 o 3).")