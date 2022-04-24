import C01_fungsiDasar as fd

def search_my_game(_possession,_gamedata,_loggedUser):

     _username = _loggedUser[0]
     _panjangPossession =fd.len(_possession) 
     _panjangGame= fd.len(_gamedata)
     _idGame=input("Masukkan ID Game: ")
     _tahunRilis=input("Masukkan Tahun Rilis Game: ")
     print("Daftar game pada inventory yang memenuhi kriteria: ")

     _count=0
     if(_idGame=='' and _tahunRilis ==''):
          for m in range (_panjangPossession):
               if(_possession[m][1]==_username):
                    for j in range (_panjangGame):
                         if(_possession[m][0]==_gamedata[j][0]):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")
     elif(_idGame!='' and _tahunRilis!=''):
          for m in range (_panjangPossession):
               if(_possession[m][1]==_username):
                 for j in range (_panjangGame):
                    if(_possession[m][0]==_gamedata[j][0] and _idGame.lower() == _gamedata[j][0].lower() and int(_tahunRilis) ==_gamedata[j][3] ):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")
     elif(_idGame!='' and _tahunRilis==''):
          for m in range (_panjangPossession):
               if(_possession[m][1]==_username):
                 for j in range (_panjangGame):
                    if(_possession[m][0]==_gamedata[j][0] and _idGame.lower() == _gamedata[j][0].lower()):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")
     elif(_idGame=='' and _tahunRilis!=''):
          for m in range (_panjangPossession):
               if(_possession[m][1]==_username):
                 for j in range (_panjangGame):
                    if(_possession[m][0]==_gamedata[j][0] and  int(_tahunRilis) ==_gamedata[j][3]):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")
