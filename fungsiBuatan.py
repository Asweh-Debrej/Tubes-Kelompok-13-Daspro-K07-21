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


def blit(loggedUser):
    maxLen = 0
    title = [
        "██████╗  ███╗   ██╗ ███╗   ███╗  ██████╗ ",
        "██╔══██╗ ████╗  ██║ ████╗ ████║ ██╔═══██╗",
        "██████╔╝ ██╔██╗ ██║ ██╔████╔██║ ██║   ██║",
        "██╔══██╗ ██║╚██╗██║ ██║╚██╔╝██║ ██║   ██║",
        "██████╔╝ ██║ ╚████║ ██║ ╚═╝ ██║ ╚██████╔╝",
        "╚═════╝  ╚═╝  ╚═══╝ ╚═╝     ╚═╝  ╚═════╝ "                              
    ]
    for line in title + [loggedUser[0] + loggedUser[1] + ' '*5, loggedUser[2] + ' '*5, "saldo" + ' '*5, "Logged as admin      " + str(loggedUser[5])]:
        if fd.len(line) > maxLen:
            maxLen = fd.len(line)

    maxLen += 8
    print("|{}|".format((maxLen+2)*'‾'))
    for line in title:
        print("| {0:^{1}} |".format(line, maxLen))
    print("|{}|".format((maxLen+2)*'-'))
    print("| {0:<{1}}".format(loggedUser[0], 5) + "{0:>{1}} |".format(loggedUser[1], maxLen - 5))
    print("| {0:<{1}} |".format(loggedUser[2], maxLen))
    print("| {0:>{1}} |".format("saldo", maxLen))
    print("| {0:<{1}}".format("Logged as {}".format(loggedUser[4]), 15)  + "{0:>{1}} |".format(str(loggedUser[5]), maxLen - 15))
    for i in range(4):
        print("| {0:^{1}} |".format('', maxLen))
    print("|{}|".format((maxLen+2)*'_'))
                  

if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    _loggedUser = ["1", "2", "3", "4", "5", 0]
    blit(_loggedUser)