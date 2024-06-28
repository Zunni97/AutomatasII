caracteres_validos = {'a','b','c','d','f','g','h','i','j','k','l',
                          'm','n','ñ','o','p','q','r','s','t','u','v','w',
                          'x','y','z','1','2','3','4','5','6','7','8','9',
                          '0','¡','!','¿','?',':','.',','}

def separar_caracteres(cadena):
    cadena = cadena.lower()
    for caracter in cadena:
        if caracter not in caracteres_validos:
            return "Error, caracter invalido"
    return list(cadena)

cadena_usuario = input("Ingrese una cadena de texto: ")

caracteres_separados = separar_caracteres(cadena_usuario)
print("Cadena separada por caracteres: ", caracteres_separados)