def splitarray(arr):
    list_data = []
    elemen = ""
    for isi in arr:
        if isi == ';':
            list_data += [elemen]
            elemen = ""
        elif isi == '\n':
            list_data += [elemen]
            elemen = ""
        else:
            elemen += isi
    return list_data

def matriks(x):
    data = open(x,"r")
    baris = data.readlines()

    matriks = []
    for line in baris:
        arrawal = splitarray(line)
        matriks += [arrawal]
    return matriks
