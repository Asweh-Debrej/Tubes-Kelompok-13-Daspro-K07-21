import fungsiDasar as fd

def cekGame(_idGame):
     _panjangArray = fd.len(_gameData)
     _found = False
     for x in range(_panjangArray):
          if(_idGame == _gameData[x][0]):
               _found = True
     return _found

def cekKepemilikanGame(_idGame):
     # Mencari apakah kita sudah memiliki game tersebut
     _panjangArray = fd.len(_possession)
     _ketemu = False
     for x in range(_panjangArray):
          if(_possession[x][0] == _idGame and _possession[x][1] == _loggedUser[0]):
               _ketemu = True
     return _ketemu


def cekHarga(_idGame):
     # Mencari harga dari game tersebut
     _panjangArray = fd.len(_gameData)
     for x in range(_panjangArray):
          if(_gameData[x][0] == _idGame):
               return _gameData[x][4]

def cekStok(_idGame):
     # Mencari stok dari game tersebut
     _panjangArray = fd.len(_gameData)
     for x in range(_panjangArray):
          if(_gameData[x][0] == _idGame):
               return _gameData[x][5]

def gameIndex(_idGame):
     # mencari indeks game tersebut
     _panjangArray = fd.len(_gameData)
     for x in range(_panjangArray):
          if(_idGame == _gameData[x][0]):
               return x

def userIndex():
    _panjangArray = fd.len(_usersData)
    for x in range(_panjangArray):
        if(_usersData[x][0] == _loggedUser[0]):
            return x


def beli():
     global _loggedUser,_possession,_gameData,_usersData,_history
     # Fungsi Utama
     _wanted = input("Masukkan ID Game : ")
     _gameIndex = gameIndex(_wanted)
     _userIndex = userIndex()

     # Cek apakah input Valid
     if(cekGame(_wanted)):

          # Cek _possession game
          if not((cekKepemilikanGame(_wanted))):

               #Cek Saldo
               _price = cekHarga(_wanted)
               if(_price <= (_usersData[_userIndex][5])):

                    #Cek stok
                    _stok = cekStok(_wanted)
                    if(_stok >0):

                         # Kurangi saldo
                         _usersData[_userIndex][5] -= _price
                         # Kurangi stok
                         _gameData[_gameIndex][5] -=1
                         # Tambah riwayat
                         _tambahRiwayat = [[_wanted,_gameData[_gameIndex][1],_gameData[_gameIndex][4],_loggedUser[0],2022]]
                         _history += _tambahRiwayat
                         # Tambah _possession
                         _tambahKepemilikan = [[_wanted,_loggedUser[0]]]
                         _possession += _tambahKepemilikan

                         print("Game " + str(_gameData[_gameIndex][1] + " berhasil dibeli!"))

                    else:
                         print("Stok Game tersebut sedang habis")
               else:
                    print("Saldo anda tidak cukup untuk membeli Game tersebut! ")

          else:
               print("Anda sudah memiliki Game tersebut! ")

     else:
          print("Input anda salah!")





#---------------------------------------

#






