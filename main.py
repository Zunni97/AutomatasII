import validador_caracteres
import lector

cadena_usuario = input("Ingrese una cadena de texto: ")

if validador_caracteres.validar_caracter(cadena_usuario):
    for componente in cadena_usuario.split():
        print(f"\n\t Buscando la palabra: {componente}")
        lector.load_sustantivos(componente)
