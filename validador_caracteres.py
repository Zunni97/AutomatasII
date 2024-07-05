# Este programa sirve para separar cada letra o caracter del lenguaje español
# Zunni Rojas Baldivia

caracteres_validos = {'a','á','b','c','d','e','é','f','g','h','i','í','j','k',
                          'l','m','n','ñ','o','ó','p','q','r','s','t','u','ú',
                          'ü','v','w','x','y','z','1','2','3','4','5','6','7',
                          '8','9','0','¡','!','¿','?',':','.',',',' '}

archivo_gramatica = open('diccionario/gramatica.txt')

def validar_caracter(cadena):

    cadena = cadena.lower()
    for caracter in cadena:
        if caracter not in caracteres_validos:
            return f"Error, caracter invalido {caracter}"
    return list(cadena)
    #return (cadena)

""""
archivo_gramatica = open('diccionario/gramatica.txt')
cadena_usuario = archivo_gramatica.read()
caracteres_separados = validar_caracter(cadena_usuario)
print("Cadena separada por caracteres: ", caracteres_separados)
archivo_gramatica.close()
"""
