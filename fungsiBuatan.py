import fungsiDasar as fd

_seed = 16
_cipherModifier = 6
_maxOrd = 1114112


def cipher(string, seed= _seed, modifier= _cipherModifier):
    """Menyandi string masukan. Hasil akan bergantung pada seed yang diberikan.
    
    Seed harus berupa faktor dari 1114112.

    Modifier berupa angka bebas
    """
    if 1114112 % seed != 0:
        print("""
        Peringatan : Seed yang dimasukkan bukan salah satu faktor 1114112.
        Seed akan diubah menjadi 16.
        """)
        seed = _seed

    strArr = list(string)
    for i in range(fd.len(strArr)):
        ordinate = ord(strArr[i])
        ciphOrd = (ordinate//seed + 1) * seed - ordinate % seed - 1 + modifier
        strArr[i] = chr(ciphOrd % _maxOrd)

    string = fd.join(strArr, '')
    return string

def decipher(string, seed= _seed, modifier= _cipherModifier):
    """Menguraikan string masukan. Hasil akan bergantung pada seed yang diberikan.
    
    Seed harus berupa faktor dari 1114112.

    Modifier berupa angka bebas
    """
    if 1114112 % seed != 0:
        print("""
        Peringatan : Seed yang dimasukkan bukan salah satu faktor 1114112.
        Seed akan diubah menjadi 16.
        """)
        seed = _seed

    strArr = list(string)
    for i in range(fd.len(strArr)):
        ordinate = ord(strArr[i]) - modifier
        ciphOrd = (ordinate//seed + 1) * seed - ordinate % seed - 1
        strArr[i] = chr(ciphOrd % _maxOrd)

    string = fd.join(strArr, '')
    return string

if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    print(decipher(cipher("abcdefg")))