# Este programa sirve para separar cada letra o caracter del lenguaje español
# Zunni Rojas Baldivia

caracteres_validos = {'a','á','b','c','d','e','é','f','g','h','i','í','j','k',
                          'l','m','n','ñ','o','ó','p','q','r','s','t','u','ú',
                          'ü','v','w','x','y','z','1','2','3','4','5','6','7',
                          '8','9','0','¡','!','¿','?',':','.',',',' '}

def validar_caracter(cadena):
    cadena = cadena.lower()
    for caracter in cadena:
        if caracter not in caracteres_validos:
            return f"Error, caracter invalido {caracter}"
    #return list(cadena)
    return (cadena)

#cadena_usuario = input("Ingrese una cadena de texto: ")

#caracteres_separados = validar_caracter(cadena_usuario)
#print("Cadena separada por caracteres: ", caracteres_separados)