def sum(arr):
    """Mengembalikan jumlah bilangan dari seluruh elemen arr.
    """
    result = 0
    for i in arr:
        result += i
    
    return result


def len(arr):       # Penggunaan len(arr) dengan arr bertipe 
    """Mengembalikan banyak isi dari array yang diberikan.
    """
    if type(arr) == int or type(arr) == float:
        arr = str(arr)
    length = 0
    for i in arr:
        length += 1

    return length


def append(arr, X):
    """Mengembalikan array yang sudah ditambah X pada akhir array
    """
    return arr + [X]


def sliced(arr, start = 0, stop = None, step = 1):
    """Mengembalikan array yang sudah dipotong dengan posisi yang diberikan.

    Dimulai dari elemen berindeks start. Tidak termasuk elemen berindeks stop.
    """
    if type(arr) == str:
        result = ""
    else:
        result = []
    if step < 0:
        if start == None or start > len(arr) - 1:
            start = len(arr) - 1
        if stop == None:
            stop = -1
    elif step > 0:
        if start == None:
            start = 0
        if stop == None or stop > len(arr):
            stop = len(arr)
    else:
        return result

    for i in range(start, stop, step):
        if type(arr) == str:
            result += arr[i]
        else:
            result = append(result, arr[i])

    return result

def strip(string: str, chars: str = ' '):
    """Menghapus chars yang berada pada awal atau akhir string
    """
    if not string:
        return ''

    front = True
    while string[0] == chars[0] and front:
        for i in chars:
            if front and len(string) > 0 and string[0] == i:
                string = sliced(string, 1)
            else:
                front = False

    back = True
    while string[-1] == chars[-1] and back:
        for i in sliced(chars, step= -1):
            if back and len(string) > 0 and string[-1] == i:
                string = sliced(string, stop = len(string) - 1)
            else:
                back = False

    return string


def replace(string: str, chars1, chars2):
    """Menggantikan chars1 yang ditemukan pada string menjadi chars2.
    
    Pembacaan dimulai dari kiri.
    """
    result = ""
    while string:
        if sliced(string, 0, len(chars1)) == chars1:
            result += chars2
            string = sliced(string, len(chars1))
        else:
            result += string[0]
            string = sliced(string, 1)

    return result


def find(arr, X):
    """Mengembalikan indeks ditemukannya X pertama pada arr.

    Mengembalikan -1 bila tidak ditemukan X pada arr.
    """
    if type(arr) == list and type(X) != list:
        X = [X]

    for i in range(0, len(arr) - len(X) + 1):
        slicedArr = sliced(arr, i, i + len(X))
        if slicedArr == X:
            return i
    
    return -1


def mtrxFind(matrix, X, idxSlug):
    """Mengembalikan indeks list pada matrix yang ditemukan X merupakan elemen berindex idxSlug dari list tersebut
    
    Mengembalikan -1 jika tidak ditemukan."""
    for i in range(len(matrix)):
        if matrix[i][idxSlug] == X:
            return i

    return -1


def join(arr, infix):
    """Menyisipkan infiks pada arr dan mengembalikannya dalam bentuk string.
    """
    string = ""
    for i in range(len(arr)):
        string += str(arr[i])
        if i + 1 < len(arr):
            string += str(infix)
    
    return string


def split(string, pattern= ' ', arr = [], ignoreNull = False):
    """Mengembalikan string yang sudah dipecah menjadi list of string.
    
    String dipecah berdasarkan pattern."""
    idx = find(string, pattern)
    if idx != -1:
        if not ignoreNull or sliced(string, 0, idx):
            arr = append(arr, sliced(string, 0, idx))

        if len(string) > idx + 1:
            return split(sliced(string, idx + 1), pattern, arr)
        else:
            return arr
    else:
        return append(arr, string)
    
    
def valAll(val, arr):
    """Mengembalikan True apabila semua isi arr adalah val, False jika tidak
    """
    allIn = True
    i = 0
    while allIn and i < len(arr):
        if arr[i] != val:
            allIn = False
        i += 1
    
    return allIn








if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    pass
