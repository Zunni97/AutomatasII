def load_sustantivos(palabra):
    fid = open('diccionario/sustantivos.txt')
    for line in fid:
        data = line.split('-')
        token = data[0]
        palabras = data[1].strip().split(',')
        for diccionario_palabras in palabras:
            if palabra == diccionario_palabras:
                print(f"\t Si lo encontre y su token es {token}\n")
                fid.close()
                return token
    print(f"\t No se encontro la palabra '{palabra}'")
    fid.close()