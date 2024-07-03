def load_sustantivos(palabra):
    fid = open('diccionario/sustantivos.txt')
    for line in fid:
        data = line.split('-') # 0 -> token / 1 -> lista de palabras
        #print(f"Encontrado {data[0]}") if palabra in data[1] else print("\tNEL")
        for diccionario_palabras in data[1].strip().split(","):
            if palabra == diccionario_palabras:
                print(f"\n\t Si lo encontre y su token es {data[0]}\n")
                fid.close()
                return data[0]

    fid.close()

load_sustantivos("amor")