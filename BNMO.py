import fungsiDasar as fd
import fungsiBuatan as fb
import register as reg
import addGame as ag
import topup
import history
import exit
import cipher as cp

_role = "user"
_loggedIn = False
_valCommand = ["register", "login", ""]

_userData = ["1", "2", "3", "4", "5", 0]
"""
1 : id
2 : username
3 : nama
4 : password
5 : role (admin/user)
6 : saldo
"""

_gameData = [["1", "2", "3", 2000, 0, 0]]
"""
1 : id
2 : nama
3 : kategori
4 : tahun rilis
5 : harga
6 : stok
"""

_history = [["1", "2", 0, "4", 2000]]
"""
1 : id game
2 : nama game
3 : harga game
4 : id pembeli
5 : tahun pembelian
"""

_possession = [["1", "2"]]
"""
1 : id game
2 : id pemilik
"""

def mintaCommand():
    global _role, _loggedIn, _userData, _gameData, _history, _possession, running
    command = input(">>> ").lower()
    if _loggedIn:
        if command == "register":
            if _role != "admin":
                print("""Hanya admin yang memiliki akses command terebut!
                
                Untuk melihat command user, ketik \"help\"""")
                reg.register()
        elif command == "exit":
            running = exit.exit()
        else:
            print("""Perintah tersebut tidak ada
            
            Untuk melihat command, ketik \"help\"""")
    else:
        if command == "login":
            pass                                # login
        elif command == "help":
            pass                                # help
        elif command

    return command


running = True


if __name__ == "__main__":                          # Inti program
    while running:
        command = mintaCommand()

    print("Selamat menikmati hari anda :(")