import fungsiDasar as fd

def maxLengths(matrix):
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
    for val in arr2:
        if fd.find(arr1, val) == -1:
            arr1 = fd.append(arr1, val)

    return arr1


if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    import tes
    print(maxLengths(tes.gameData))