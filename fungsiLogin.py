from fungsiDasar import len
from fungsiBacacsv import matriks

def admin(x):
    # perintah yang valid untuk admin
    cek = True
    if x == "register" or x == "login" or x == "tambah_game" or x == "ubah_game" or x == "ubah_stok" or x == "list_game_toko" or x == "search_game_at_store" or x == "topup" or x == "help" or x == "save" or x == "exit":
        cek = True
    else:
        cek = False
    return cek

def user(x):
    # perintah yang valid untuk user
    cek = True
    if x == "login" or x == "list_game_toko" or x == "buy_game" or x == "list_game" or x == "search_my_game" or x == "search_game_at_store" or x == "riwayat" or x == "help" or x == "save" or x == "exit":
        cek = True
    else:
        cek = False
    return cek

data1 = matriks("user.csv")
perintah = input()
while perintah != "login" and perintah != "help":
    # validasi perintah, tidak boleh melakukan apa-apa sebelum login KECUALI HELP
    if admin(perintah) or user(perintah):
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login"')
        perintah = input()
    else:
        print("Perintah tidak valid")
        perintah = input()

#validasi username dan password
in_username = input("Masukan username: ")
in_password = input("Masukan password: ")
a = 0
for i in range(len(data1)):
    if in_username in data1[i][1]:
        if in_password == data1[i][3]:
            a = 1
            nama = data1[i][2]
            print('Halo', nama, '! Selamat data1ng di "Binomo".') #ke validasi perintah admin user
            role = data1[i][4]
        else:
            pass
    else:
        pass

if a == 0:
    print("Password atau username salah atau tidak ditemukan.")
    perintah = input()

#validasi perintah admin user
perintah = input("Masukkan perintah: ")
while perintah != "login" and perintah != "registrasi": #sudah login dan registrasi
    for j in range(len(data1)):
        if role == "admin":
            if not admin(perintah):
                print("Maaf, anda harus menjadi user untuk melakukan hal tersebut")
                perintah = input()
            else:
                pass
        else :
            if not user(perintah):
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                perintah = input()
            else:
                pass
