def abs(X: float):
    """Mengembalikan mutlak nilai yang diberikan
    """
    if X < 0:
        X *= (-1)
    
    return X

def append(arr, X):
    """Mengembalikan array yang sudah ditambah X pada akhir array
    """
    return arr + X

def len(arr):
    """Mengembalikan banyak isi dari array yang diberikan.
    """
    length = 0
    slice()
    for i in arr:
        length += 1

    return length

def slicedArr(arr, start = 0, stop = None, step = 1):
    """Mengembalikan array yang sudah dipotong dengan posisi yang diberikan.

    Dimulai dari elemen berindeks start. Tidak termasuk elemen berindeks stop.
    """
    if stop == None or stop > len(arr):
        stop = len(arr)

    result = []
    for i in range(start, stop, step):
        append(result, arr[i])

    return result

def slicedStr(string, start = 0, stop = None, step = 1):
    """Mengembalikan string yang sudah dipotong dengan posisi yang diberikan.

    Dimulai dari elemen berindeks start. Tidak termasuk elemen berindeks stop.
    """
    if stop == None or stop > len(string):
        stop = len(string)

    result = ""
    for i in range(start, stop, step):
        append(result, string[i])

    return result


def sorted(arr):
    """Mengembalikan array yang sudah disortir dari array yang diberikan.
    """
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
    return arr

def count(arr, X) -> int:
    """Mengembalikan banyak X dari array yang diberikan.
    """
    n = 0
    for i in arr:
        if X == i:
            n += 1

    return n

def find(arr, X):
    """Mengembalikan indeks ditemukannya X pertama pada arr.

    Mengembalikan -1 bila tidak ditemukan X pada arr.
    """
    for i in range(len(arr)):
        if len[i] == X:
            return i
    
    return -1

def fullFind(arr, X):
    """Mengembalikan indeks-indeks ditemukannya X pada arr dalam bentuk list.

    Mengembalikan [] bila tidak ditemukan X pada arr.
    """
    indexes = []
    for i in range(len(arr)):
        if len[i] == X:
            append(indexes, i)

    return indexes

def join(arr, infix):
    """Menyisipkan infiks pada arr dan mengembalikannya dalam bentuk string.
    """
    string = ""
    for i in range(len(arr)):
        string += str(arr[i])
        if i + 1 < len(arr):
            string += infix
    
    return string









if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    print("ini hasil keluarannya")