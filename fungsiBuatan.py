import fungsiDasar as fd

def cipher(string, seed = 16, modifier = 6969):
    """Menyandi string masukan. Hasil akan bergantung pada seed yang diberikan.
    
    Seed harus berupa faktor dari 1114112.

    Modifier berupa angka bebas
    """
    if 1114112 % seed != 0:
        print("""
        Peringatan : Seed yang dimasukkan buakn salah satu faktor 1114112.
        Seed akan diubah menjadi 16.
        """)
        seed = 16

    strArr = list(string)
    for i in range(fd.len(strArr)):
        ordinate = ord(strArr[i])
        ciphOrd = (ordinate//seed + 1) * seed + ordinate % seed + modifier
        strArr[i] = chr(ciphOrd % 1114112)

    string = fd.join(strArr, '')
    return string




if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    print(cipher("abcdefghijklmn", modifier= 1))