import fungsiDasar as fd
import datetime

def cekGame(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # Mengecek apakah game tersebut ada atau tidak
     _panjangArray = fd.len(_gameData)
     _found = False
     for x in range(_panjangArray):
          if(_wanted == _gameData[x][0]):
               _found = True
     return _found

def cekKepemilikanGame(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # Mencari apakah kita sudah memiliki game tersebut
     _panjangArray = fd.len(_possession)
     _ketemu = False
     for x in range(_panjangArray):
          if(_possession[x][0] == _wanted and _possession[x][1] == _loggedUser[0]):
               _ketemu = True
     return _ketemu


def cekHarga(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # Mencari harga dari game tersebut
     _panjangArray = fd.len(_gameData)
     for x in range(_panjangArray):
          if(_gameData[x][0] == _wanted):
               return _gameData[x][4]

def cekStok(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # Mencari stok dari game tersebut
     _panjangArray = fd.len(_gameData)
     for x in range(_panjangArray):
          if(_gameData[x][0] == _wanted):
               return _gameData[x][5]

def gameIndex(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # mencari indeks game tersebut
     _panjangArray = fd.len(_gameData)
     for x in range(_panjangArray):
          if(_wanted == _gameData[x][0]):
               return x

def userIndex(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # Mencari indeks user tersebut
    _panjangArray = fd.len(_usersData)
    for x in range(_panjangArray):
        if(_usersData[x][0] == _loggedUser[0]):
            return x

#-----------------------------
def _ubahPossession(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # Ganti _possession
     _tambahKepemilikan = [[_wanted, _loggedUser[0]]]
     _possession += _tambahKepemilikan

     return _possession

def _ubahGameData(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # ganti _gameData
     _gameIndex = gameIndex(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _gameData[_gameIndex][5] -= 1

     return _gameData


def _ubahUsersData(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # ganti _userData
     _userIndex = userIndex(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _price = cekHarga(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
     _usersData[_userIndex][5] -= _price

     return _usersData


def _ubahLoggedUsers(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # ganti _loggedUser
     _price = cekHarga(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
     _userIndex = userIndex(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)
     _loggedUser[5] -= _price

     return _loggedUser

def _ubahHistory(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):
     # ganti _history
     _sekarang = datetime.datetime.now()
     _sekarang = _sekarang.year
     _gameIndex = gameIndex(_wanted, _loggedUser, _possession, _gameData, _usersData, _history)

     _tambahRiwayat = [[_wanted, _gameData[_gameIndex][1], _gameData[_gameIndex][4], _loggedUser[0], _sekarang]]
     _history += _tambahRiwayat

     return _history









def beli(_wanted,_loggedUser, _possession, _gameData, _usersData, _history):

     # Fungsi Utama

     _gameIndex = gameIndex(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _userIndex = userIndex(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _bisa = False
     _wanted[0] = _wanted[0].upper()

     # Cek apakah input Valid
     if(cekGame(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)):

          # Cek _possession game
          if not((cekKepemilikanGame(_wanted,_loggedUser, _possession, _gameData, _usersData, _history))):

               #Cek Saldo
               _price = cekHarga(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
               if(_price <= (_usersData[_userIndex][5])):

                    #Cek stok
                    _stok = cekStok(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
                    if(_stok >0):

                         _bisa = True

                         """"
                         # Kurangi saldo
                         _usersData[_userIndex][5] -= _price
                         # Kurangi stok
                         _gameData[_gameIndex][5] -=1
                         # Tambah riwayat
                         _sekarang = datetime.datetime.now()
                         _sekarang = _sekarang.year

                         _tambahRiwayat = [[_wanted,_gameData[_gameIndex][1],_gameData[_gameIndex][4],_loggedUser[0],_sekarang]]
                         _history += _tambahRiwayat
                         # Tambah _possession
                         _tambahKepemilikan = [[_wanted,_loggedUser[0]]]
                         _possession += _tambahKepemilikan
                         """

                         print("Game " + str(_gameData[_gameIndex][1] + " berhasil dibeli!"))

                    else:
                         print("Stok Game tersebut sedang habis")
               else:
                    print("Saldo anda tidak cukup untuk membeli Game tersebut! ")

          else:
               print("Anda sudah memiliki Game tersebut! ")

     else:
          print("Input anda salah!")

     return _bisa




#---------------------------------------

"""
_loggedUser = ["U001", "jonathan", "Jonathan Sinaga", "jon123", "user", 100000]
_possession =  [["G001", "U001"],["G002","U002"]]
_gameData =  [["G001", "Call of Duty", "FPS", 2000, 1000, 2],["G002","Age of Empire","Adventure",2020,2000,3],["G003","AC Unity","Adventure",2030,3000,4]]
_usersData =  [["U001", "jonathan", "Jonathan Sinaga", "jon123", "user", 100000]]
_history = [["G001", "Call of Duty", 1000, "U001", 2000]]



print(_loggedUser)
print(_possession)
print(_gameData)
print(_usersData)
print(_history)
print("__________________________________________")

_wanted = input("want = ")

if(beli(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)):
     _ubahHistory(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _ubahGameData(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _ubahLoggedUsers(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _ubahUsersData(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)
     _ubahPossession(_wanted,_loggedUser, _possession, _gameData, _usersData, _history)





print(_loggedUser)
print(_possession)
print(_gameData)
print(_usersData)
print(_history)


"""
