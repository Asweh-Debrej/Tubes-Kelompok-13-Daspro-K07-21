import fungsiDasar as fd
import os

def _ubahJadiString(arr):

    _panjang = fd.len(arr)
    _lebar = fd.len(arr[0])
    _data = ''

    for x in range(_panjang):
        for y in range(_lebar):
            _data += str(arr[x][y]) +","
        _data += "\n"

    return _data


def simpan(_arrData, tipe,cari):

    directory = os.getcwd()
    _daftarFolder = []
    for root, dirs, files, in os.walk(directory):
        _daftarFolder += dirs



    if(fd.find(_daftarFolder,cari) != -1):
        # Jika ada folder
        pass

    else:
        # Jika tidak ada folder
        _path = os.path.join(directory,cari)
        os.makedirs(cari)

    if(tipe == "game"):
        buka = os.path.join(os.getcwd(), cari, "game.csv")
    elif(tipe == "kepemilikan"):
        buka = os.path.join(os.getcwd(), cari, "kepemilikan.csv")
    elif(tipe == "user"):
        buka = os.path.join(os.getcwd(), cari, "user.csv")
    else:
        buka = os.path.join(os.getcwd(), cari, "riwayat.csv")
    a = open(buka,"w")
    a.writelines(_ubahJadiString(_arrData))





