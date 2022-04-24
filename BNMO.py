import C01_fungsiDasar as fd
import C02_fungsiBuatan as fb
import F02_register as reg
import F03_login as login
import F04_addGame as ag
import F05_updateGame as ug
import F06_updateStok as us
import F07_gameListing as lg
import F10_libraryFind as F10
import F11_storeFind as F11
import F08_buyGame as bg
import F09_gameLibrary as lgsd
import F12_topup as topup
import F13_history as hs
import F14_help as help
import F17_exit as exit
import F16_save as sv
import F15_load as loading
import B02_magicConch as mcs
import B03_tictactoe as tt



_role = "user"
_loggedIn = False
_adminCmds = ["register", "login", "addgame", "updategame", "updatestock", "store", "storesearch", "topup", "help", "save", "exit","magicconch","tictactoe"]
_userCmds = ["login", "store", "buygame", "listgame", "searchmygame", "storesearch", "history", "help", "save", "exit","magicconch","tictactoe"]
_valCommand = fb.merge(_adminCmds, _userCmds)


_loggedUser = ["0", "1", "2", "3", "4", 0]
"""Data user yang telah login
0 : id
1 : username
2 : nama
3 : password
4 : role (admin/user)
5 : saldo
"""


_usersData = [["0", "1", "2", "3", "4", 0]]
"""Diimport dari user.csv sebagai variabel global
0 : id
1 : username
2 : nama
3 : password
4 : role (admin/user)
5 : saldo
"""

_gameData = [["0", "1", "2", 2000, 0, 0]]
"""Diimport dari game.csv sebagai variabel global
0 : id
1 : nama
2 : kategori
3 : tahun rilis
4 : harga
5 : stok
"""

_history = [["0", "1", 0, "3", 2000]]
"""Diimport dari riwayat.csv sebagai variabel global
0 : id game
1 : nama game
2 : harga game
3 : id pembeli
4 : tahun pembelian
"""

_possession = [["0", "1"]]
"""Diimport dari kepemilikan.csv sebagai variabel global
0 : id game
1 : id pemilik
"""


def roleCmdIsValid(_role, command, _adminCmds, _userCmds):
    """ validasi command sesuai role """
    _cekCommand = False
    if _role == "admin":
        if fd.find(_adminCmds, command) != -1:
            _cekCommand = True
        else:
            print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')
            input("\nTekan enter untuk melanjutkan\n")
    else: #_role == "user"
        if fd.find(_userCmds, command) != -1:
            _cekCommand = True
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            print('Untuk melihat list command, ketik "help"')
            input("\nTekan enter untuk melanjutkan\n")

    return _cekCommand


def mintaCommand():
    global _role, _loggedIn, _adminCmds, _userCmds, _valCommand, _loggedUser, _usersData, _gameData, _history, _possession, running
    if _loggedIn:
        fb.blit(_loggedUser, "Masukkan perintah")
    cmdInput = input("\n>>> ").strip()
    command = fd.replace(fd.replace(fd.replace(cmdInput.lower(), ' ', ''), '_', ''), '-', '')     # Toleransi bagi pengguna yang menggunakan (' '), ('_'), atau ('-') sebagai pengutaraan maksud perintah
    print()
    if fd.find(_valCommand, command) != -1:                 # validasi input command
        if _loggedIn:
            if roleCmdIsValid(_role, command, _adminCmds, _userCmds):              # validasi perintah admin dan user
                if command == "register":
                    fb.blit(_loggedUser, cmdInput)
                    _usersData = reg.register(_usersData)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "login":
                    fb.blit(_loggedUser, cmdInput)
                    print('Anda sudah login! Untuk melihat list command, ketik "help".')
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "addgame":
                    fb.blit(_loggedUser, cmdInput)
                    _gameData = ag.addGame(_gameData)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "updategame":
                    fb.blit(_loggedUser, cmdInput)
                    ug.ubahGame(_gameData)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "updatestock":
                    fb.blit(_loggedUser, cmdInput)
                    us.ubahStok(_gameData)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "store":           # Melihat daftar game yang ada     
                    fb.blit(_loggedUser, cmdInput)
                    lg.listing_game(_gameData)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "buygame":
                    fb.blit(_loggedUser, cmdInput)
                    lg.listing_game(_gameData)
                    _wanted = input("Masukkan ID Game: ")   # Membeli game
                    if(bg.beli(_wanted, _loggedUser, _possession, _gameData, _usersData)):
                        _history     = bg._ubahHistory(_wanted, _loggedUser, _gameData, _history)
                        _gameData    = bg._ubahGameData(_wanted, _gameData)
                        _loggedUser  = bg._ubahLoggedUsers(_wanted, _loggedUser, _gameData)
                        _usersData   = bg._ubahUsersData(_wanted, _loggedUser, _gameData, _usersData)
                        _possession  = bg._ubahPossession(_wanted, _loggedUser, _possession)
                    input("\nTekan enter untuk melanjutkan\n") 
                elif command == "listgame":
                    fb.blit(_loggedUser, cmdInput)
                    lgsd.lihat(_loggedUser[0],_gameData,_possession)            # melihat daftar game yang dimiliki 
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "searchmygame":
                    fb.blit(_loggedUser, cmdInput)
                    F10.search_my_game(_possession,_gameData,_loggedUser)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "storesearch":
                    fb.blit(_loggedUser, cmdInput)
                    F11.search_game_at_store(_gameData)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "history":
                    fb.blit(_loggedUser, cmdInput)
                    hs.history(_history, _loggedUser)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "topup":
                    fb.blit(_loggedUser, cmdInput)
                    _usersData = topup.topup(_usersData)
                    _loggedUser = _usersData[fd.mtrxFind(_usersData, _loggedUser[1], 1)]
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "help":
                    fb.blit(_loggedUser, cmdInput)
                    help.help(_role)
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "exit":
                    fb.blit(_loggedUser, cmdInput)
                    running = exit.exit(_usersData, _gameData, _history, _possession, _loggedIn)
                    if running == 0:
                        print("Selamat menikmati hari anda :D")
                        input("\nTekan enter untuk keluar program\n")
                elif command == "save":
                    fb.blit(_loggedUser, cmdInput)
                    cari = input("Masukkan nama folder penyimpanan : ")
                    if cari == '':
                        print("Nama folder penyimpanan tidak bisa kosong!")         # Melakukan save
                        cari = input("Masukkan nama folder penyimpanan : ")
                    print("")
                    print("Saving")
                    sv.simpan(_possession,"kepemilikan",cari)
                    sv.simpan(_gameData,"game",cari)
                    sv.simpan(_usersData,"user",cari)
                    sv.simpan(_history,"riwayat",cari)
                    print("Data telah disimpan pada folder " + cari +"!")
                    input("\nTekan enter untuk melanjutkan\n")
                    
                elif command == "magicconch":
                    fb.blit(_loggedUser, cmdInput)
                    mcs.kerangAjaib()                       # Kerang Ajaib
                    input("\nTekan enter untuk melanjutkan\n")
                elif command == "tictactoe" :
                    fb.blit(_loggedUser, cmdInput)
                    tt.tictactoe()
                    input("\nTekan enter untuk melanjutkan\n")
            else: # command tidak valid dengan _role
                pass

        else: #_loggedIn = False
            if command == "login":
                _loggedUser = login.login(_usersData)
                if _loggedUser != None: #username dan password sudah tervalidasi
                    _role = _loggedUser[4]
                    _loggedIn = True
            elif command == "help":
                help.help(_role)  
            elif command == "exit":
                running = exit.exit(_usersData, _gameData, _history, _possession, _loggedIn)                       
            else:
                # validasi perintah, tidak boleh melakukan apa-apa sebelum login KECUALI HELP
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
    
    else: #command != _valCommand[i]
        print('Command tidak ada. Untuk melihat list command, ketik "help".')
        if _loggedIn:
            input("\nTekan enter untuk melanjutkan\n")
        
                


running = True



if __name__ == "__main__":   # Inti program
    data = loading.load()
    if data:    # apabila data tidak kosong atau dapat diproses
        _usersData, _gameData, _possession , _history = data
        fb.printWelcome()
        while running:
            mintaCommand()
