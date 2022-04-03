## Fungsi buatan oleh M Farhan Syakir 16521105



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

def slice(arr, start = 0, stop = None, step = 1):
    """Mengembalikan array yang sudah dipotong dengan posisi yang diberikan.

    Dimulai dari elemen berindeks start. Tidak termasuk elemen berindeks stop.
    """
    if stop == None or stop > len(arr) - 1:
        stop = len(arr) - 1

    result = []


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

def fullFind(arr, X):
    indexes = []
    for i in range(len(arr)):
        if len[i] == X:
            append(indexes, i)
    return indexes