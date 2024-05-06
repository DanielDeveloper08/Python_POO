from calcula import Calcula
from validaciones import Validaciones

def main():
        calculadora = Calcula()
        validador = Validaciones()

        print("Tabla de multiplicar del 3:")
        calculadora.multiplicar_numero(3)
        print("\nSecuencia del 1 al 18 con incremento de 2:")
        secuencia = calculadora.calcular_secuencia(1, 18, 2)
        print(secuencia)

        print("\nTexto convertido a mayúsculas:")
        texto_convertido = validador.convertir_mayuscula("Hola Mundo!")
        print(texto_convertido)

        print("\nValidación de números:")
        numero_valido = validador.validar_numeros(15, minimo=10, maximo=20)
        print(numero_valido)

        numero_invalido = validador.validar_numeros(-5)
        print(numero_invalido)

if __name__ == "__main__":
    main()