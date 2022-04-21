import os.path
import sys
import argparse

def load():
    parser = argparse.ArgumentParser(usage= "Mohon masukkan nama folder!")
    parser.add_argument('folder', type= str, help= "Nama folder harus berisi data program ini.")
    args = parser.parse_args()

    

    if len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            path = sys.argv[1]
            for file in ["user.csv", "game.csv", "kepemilikan.csv", "riwayat.csv"]:
                with open(path + '/' + file, 'r') as f:
                    print(f.readlines())
            print("Selamat datang di antarmuka 'Binomo' ")
        elif(os.path.isfile(sys.argv[1])):
            print("Ini adalah file bukan folder. Mohon masukan nama folder!")
        else:
            print('Folder',args._get_args,'tidak ditemukan.')
    elif len(sys.argv) == 1:
        print('Tidak ada nama folder yang diberikan.')
    
