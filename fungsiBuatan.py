import fungsiDasar as fd

def maxLengths(matrix):
    """Mengembalikan panjang terpanjang setiap kolom dari matriks berukuran minimal 1x1.
    """
    if not matrix:
        return 0

    lengths = [0 for i in range(len(matrix[0]))]
    for i in range(fd.len(matrix[0])):
        lengths[i] = fd.len(matrix[0][i])

    for i in range(1, fd.len(matrix)):
        for j in range(fd.len(matrix[i])):
            if fd.len(matrix[i][j]) > lengths[j]:
                lengths[j] = fd.len(matrix[i][j])

    return lengths


def merge(arr1, arr2):
    """Mengembalikan array yang telah digabung dengan setiap elemennya berbeda.
    """
    for val in arr2:
        if fd.find(arr1, val) == -1:
            arr1 = fd.append(arr1, val)

    return arr1


def ubahStringData(data):
    """Mengubah data bilangan menjadi bilangan (misal: saldo, harga, dll).
    """
    listToInt = ["saldo", "harga", "tahun_beli", "tahun_rilis", "stok"]       # Nama kolom yang akan diubah menjadi integer
    for i in range(fd.len(data)):
        for j in range(1, fd.len(data[i])):
            for k in range(fd.len(data[i][j])):
                if fd.find(listToInt, data[i][0][k]) != -1:                 # Header kolom sesuai
                    data[i][j][k] = int(data[i][j][k])
    
    return data

def printWelcome():
    """Menyambut pengguna.
    """
    print("""
           .----------------.  .----------------.  .----------------.  .----------------.  
          | .--------------. || .--------------. || .--------------. || .--------------. |
          | |              | || |              | || |              | || |              | |
          | |   ██████╗    | || |  ███╗   ██╗  | || |  ███╗   ███╗ | || |    ██████╗   | |
          | |   ██╔══██╗   | || |  ████╗  ██║  | || |  ████╗ ████║ | || |   ██╔═══██╗  | |
          | |   ██████╔╝   | || |  ██╔██╗ ██║  | || |  ██╔████╔██║ | || |   ██║   ██║  | |
          | |   ██╔══██╗   | || |  ██║╚██╗██║  | || |  ██║╚██╔╝██║ | || |   ██║   ██║  | |
          | |   ██████╔╝   | || |  ██║ ╚████║  | || |  ██║ ╚═╝ ██║ | || |   ╚██████╔╝  | |
          | |   ╚═════╝    | || |  ╚═╝  ╚═══╝  | || |  ╚═╝     ╚═╝ | || |    ╚═════╝   | |
          | |              | || |              | || |              | || |              | |
          | '--------------' || '--------------' || '--------------' || '--------------' |
           '----------------'  '----------------'  '----------------'  '----------------' """)


if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    pass