import C01_fungsiDasar as fd
import B01_cipher as cp

_uNameChars = []

# Pengisian karakter yang valid
for i in range(97, 123):
    _uNameChars = fd.append(_uNameChars, chr(i))
for i in range(65, 91):
    _uNameChars = fd.append(_uNameChars, chr(i))
_uNameChars = fd.append(_uNameChars, chr(45))
_uNameChars = fd.append(_uNameChars, chr(95))

def askName():
    """Menanyakan nama pengguna
    
    Mengembalikan nama yang sudah valid"""
    name = fd.strip(input("Masukkan nama : "))
    if name == '':
        print("Nama tidak boleh kosong!")
        askName()

    return name

def askUName(usedUName):
    """Menanyakan username kepada pengguna.
    
    Mengembalikan username yang sudah valid."""
    uName = input("Masukkan username : ")
    valid = True
    for i in uName:
        if fd.find(_uNameChars, i) == -1:
            valid = False
    if uName == '':
        print("Username tidak boleh kosong!")
        uName = askUName(usedUName)
    elif not valid:
        print("Hanya alfabet(a-z), minus(-), dan underscore(_) yang diperbolehkan!")
        uName = askUName(usedUName)
    elif fd.len(uName) < 6:
        print("Username harus memiliki minimal 6 karakter!")
        uName = askUName(usedUName)
    elif fd.find(usedUName, uName) != -1:
        print("Username tersebut telah digunakan")
        uName = askUName(usedUName)
    
    return uName

def askPass(name: str, uName: str):
    """Menanyakan password kepada pengguna.
    
    Mengembalikan password yang sudah valid."""
    password = cp.cipher(input("Masukkan password : "))             # Disandikan langsung untuk mencegah kebocoran password ketika terjadi kebocoran memori
    if len(password) < 6:
        print("Panjang password tidak boleh kurang dari 6 karakter!")
        password = askPass(name, uName)
    elif fd.find(name.lower(), cp.decipher(password).lower()) != -1  or fd.find(uName.lower(), cp.decipher(password).lower()) != -1:
        print("Password tidak boleh merupakan bagian dari nama atau username!")
        password = askPass(name, uName)
    elif fd.valAll(cp.decipher(password)[0], cp.decipher(password)):
        print("Password harus memiliki karakter yang berbeda!")

    return password

def register(_usersData):
    """Mendaftarkan pengguna baru.

    Mengembalikan matriks _usersData yang sudah diubah."""
    usedUName = []
    for i in fd.sliced(_usersData, 1):
        usedUName = fd.append(usedUName, i[1])
    name = askName()
    userName = askUName(usedUName)
    password = askPass(name, userName)
    id = "U" + '0'*(3 - fd.len(str(fd.len(_usersData)))) + str(fd.len(_usersData))
    _usersData = fd.append(_usersData, [id, userName, name, password, "user", 0])
    print("\nAkun {} berhasil dibuat.".format(userName))

    return _usersData

    
if __name__ == "__main__":
    pass
