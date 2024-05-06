class Calcula:
    def tabla_multiplicar(numero: int):
        try:
            if not isinstance(numero, int) or numero < 1 or numero > 12:
                raise ValueError("Por favor ingrese un número entero del 1 al 12.")

            print(f"Tabla de multiplicar del {numero}:")
            for i in range(1, 13):
                print(f"{numero} x {i} = {numero * i}")

        except ValueError as e:
            print(e)