def find_sustantivo(palabra):
    fid = open('diccionario/sustantivos.txt')
    for line in fid:
        data = line.split('-')
        token = data[0]
        palabras = data[1].split(',')
        for diccionario_palabras in palabras:
            if palabra == diccionario_palabras.strip():
                print(f"\t Si lo encontre y su token es {token}\n")
                fid.close()

                return token
    #print(f"\t No se encontro la palabra '{palabra}'")
    return 666
    fid.close()




def leer_gramatica():
    archivo_gramatica = open('diccionario/gramatica.txt')
    contenido = archivo_gramatica.read()
    archivo_gramatica.close()
    return contenido