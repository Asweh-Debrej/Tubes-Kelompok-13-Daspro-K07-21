import os.path
import sys
import argparse

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=argparse.folder('r'))
    args = parser.parse_args()

    

    if len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
             with open(sys.argv[1]) as folder:
                 print("Selamat datang di antarmuka 'Binomo' ")
        elif(os.path.isfile(sys.argv[1])):
            print("Ini adalah fila bukan folder sehingga masukan salah harus folder")
        else:
            print('Folder',args.folder,'tidak ditemukan.')
    elif len(sys.argv) == 1:
        print('Tidak ada nama folder yang diberikan')
    
