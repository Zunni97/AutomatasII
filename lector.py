def find_sustantivo(palabra):
    fid = open('diccionario/diccionario.txt')
    for line in fid:
        data = line.split('-')
        token = data[0]
        palabras = data[1].split(',')
        for diccionario_palabras in palabras:
            if palabra == diccionario_palabras.strip():
                print(f"\t Si lo encontre y su token es {token}\n")
                fid.close()

                return token
    print("\t Palabra invalida, token 666")
    return 666
    #fid.close()




def leer_gramatica():
    archivo_gramatica = open('diccionario/gramatica.txt')
    contenido = archivo_gramatica.read()
    archivo_gramatica.close()
    return contenido