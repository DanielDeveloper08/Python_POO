class Validaciones:
    def convertir_mayuscula(self,texto:str):
        if not isinstance(texto, str):
            raise ValueError("Por favor ingrese un texto")
        texto_convertido = texto.upper()
        return texto_convertido

    def validar_numeros(self,numero, minimo=None, maximo=None):
        es_valido = True
        mensaje_error = ""

        if not isinstance(numero, (int, float)):
            es_valido = False
            mensaje_error = "Por favor ingrese un número."

        elif numero <= 0:
            es_valido = False
            mensaje_error = "Por favor ingrese un número positivo."

        elif minimo is not None and numero < minimo:
            es_valido = False
            mensaje_error = f"Por favor ingrese un número mayor o igual a {minimo}."

        elif maximo is not None and numero > maximo:
            es_valido = False
            mensaje_error = f"Por favor ingrese un número menor o igual a {maximo}."

        if es_valido:
            return numero
        else:
            return mensaje_error