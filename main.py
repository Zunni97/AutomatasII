import validador_caracteres
import lector

""""
if __name__ == '__main__':
    archivo_gramatica = open('diccionario/gramatica.txt')
    #input("Ingrese una cadena de texto: ")

    if validador_caracteres.validar_caracter(archivo_gramatica):
        for linea in archivo_gramatica:
            for palabra in linea.split():
                print(f"\n\t Buscando la palabra: {palabra}")
                lector.load_sustantivos(palabra)
"""

if __name__ == '__main__':
    cadena_usuario = lector.leer_gramatica()
    resultado_validacion = validador_caracteres.validar_caracter(cadena_usuario)
    
    if isinstance(resultado_validacion, str):
        print(resultado_validacion)  # Imprimir el error si hay caracteres inválidos
    else:
        #print("Cadena separada por caracteres: ", resultado_validacion)
        lineas_gramatica = cadena_usuario.split('\n')
        for linea in lineas_gramatica:
            for palabra in linea.split():
                print(f"\n\t Buscando la palabra: {palabra}")
                lector.load_sustantivos(palabra)
