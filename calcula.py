class Calcula:
    def multiplicar_numero(self,numero: int):
        try:
            if not isinstance(numero, int) or numero < 1 or numero > 12:
                raise ValueError("Por favor ingrese un número entero del 1 al 12.")

            print(f"Tabla de multiplicar del {numero}:")
            for i in range(1, 13):
                print(f"{numero} x {i} = {numero * i}")

        except ValueError as e:
            print(e)

    def calcular_secuencia(self, inicio, fin, incremento):
        try:
            if not isinstance(inicio, int) or not isinstance(fin, int) or not isinstance(incremento, int):
                raise ValueError("Todos los parámetros deben ser enteros")

            secuencia = []
            valor = inicio

            while valor <= fin:
                secuencia.append(valor)
                valor += incremento
                incremento += 1

            return secuencia
        except Exception as e:
            print(f"Ocurrió un error al calcular la secuencia: {e}")
            return None