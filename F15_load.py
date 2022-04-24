import os.path
import sys
import argparse
import C01_fungsiDasar as fd
import C02_fungsiBuatan as fb

def load():
    parser = argparse.ArgumentParser(usage= "Mohon masukkan nama folder!")
    
    if fd.len(sys.argv) == 2:
        parser.add_argument('folder', type= str, help= "Nama folder harus berisi data program ini.")
        args = parser.parse_args()
        if os.path.isdir(sys.argv[1]):
            path = sys.argv[1]
            toLoad = ["user.csv", "game.csv", "kepemilikan.csv", "riwayat.csv"]
            data = [[] for i in toLoad]
            for i in range(fd.len(toLoad)):
                with open(path + '/' + toLoad[i], 'r', encoding='utf-8') as f:  # encoding= utf-8 agar dapat menggunakan tabel ASCII yang lebih luas hingga 1114112 karakter
                    arg = fd.split(f.read(), "\n")
                    data[i] = [[] for i in arg]
                    for j in range(fd.len(arg)):
                        data[i][j] = fd.split(arg[j], ';')

            if fd.len(data[0]) <= 1:    # apabila data user hanya berisi header atau tidak berisi
                print("Tidak ada akun yang dapat diproses.")
                return 0

            return fb.ubahStringData(data)

        elif(os.path.isfile(sys.argv[1])):
            print("Ini adalah file bukan folder. Mohon masukan nama folder!")

        else:
            print('Folder', sys.argv[1],'tidak ditemukan.')

    elif fd.len(sys.argv) == 1:
        print('Tidak ada nama folder yang diberikan. \"python BNMO.py <nama folder>\"')

    else:   # argumen lebih dari 2
        print("Mohon masukkan perintah sesuai format! \"python BNMO.py <nama folder>\"")
    return 0

    
    
