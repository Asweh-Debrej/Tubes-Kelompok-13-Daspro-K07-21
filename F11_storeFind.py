import C01_fungsiDasar as fd

def search_game_at_store(_gamedata):

    _panjangGame= fd.len(_gamedata)
    _idGame=input("Masukkan ID Game: ")
    _nama=input("Masukkan Nama Game: ")
    _harga= input("Masukkan Harga Game: ")
    _kategori=input("Masukkan Kategori Game: ")
    _tahunRilis= input("Masukkan Tahun Rilis Game: ")


    print("Daftar game pada toko yang memenuhi kriteria: ")

    _count=0
    if(_idGame!=''):

         for j in range (_panjangGame):
             if(_idGame.lower() ==_gamedata[j][0].lower()):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")
    elif(_nama!=''):

         for j in range (_panjangGame):
             if(_nama.lower() ==_gamedata[j][1].lower()):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_harga!='' and _kategori!='' and _tahunRilis!=''):



         for j in range (_panjangGame):
             if(_harga == str(_gamedata[j][4]) and _kategori.lower() ==_gamedata[j][2].lower() and _tahunRilis == str(_gamedata[j][3])):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_harga!='' and _kategori!=''):

         for j in range (_panjangGame):
             if(_harga == str(_gamedata[j][4]) and _kategori.lower() ==_gamedata[j][2].lower()):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_kategori!='' and _tahunRilis!=''):

         for j in range (_panjangGame):
             if(_kategori.lower() ==_gamedata[j][2].lower() and _tahunRilis == str(_gamedata[j][3])):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_harga!='' and _tahunRilis!=''):

         for j in range (_panjangGame):
             if(_harga == str(_gamedata[j][4])) and _tahunRilis == str(_gamedata[j][3]):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_harga!=''):
         for j in range (_panjangGame):
             if(_harga == str(_gamedata[j][4])):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_kategori!=''):

         for j in range (_panjangGame):
             if(_kategori.lower() == _gamedata[j][2].lower()):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(_tahunRilis!=''):
         for j in range (_panjangGame):
             if(_tahunRilis ==str(_gamedata[j][3])):
                 print()
                 _count+=1
                 print(_count,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")

         if(_count==0):
             print()

             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    else :
         for j in range (_panjangGame):
            print()
            _count+=1
            print(_count,end=". ")
            print(_gamedata[j][0],end=" | ")
            print(_gamedata[j][1],end=" | ")
            print(_gamedata[j][2],end=" | ")
            print(_gamedata[j][3],end=" | ")
            print(_gamedata[j][4],end="")

         if(_count==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")
