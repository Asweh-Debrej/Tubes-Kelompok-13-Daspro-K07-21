import os.path
import sys
import argparse

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType('r'))
    args = parser.parse_args()

    print(args.filename.readlines())

    if len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
             with open(sys.argv[1]) as file:
                 print("Selamat datang di anatarmuka 'Binomo' ")
            
        else:
            print('Folder','gk tau','tidak ditemukan.')
    elif len(sys.argv) == 0:
        print('Tidak ada nama folder yang diberikan')
    
