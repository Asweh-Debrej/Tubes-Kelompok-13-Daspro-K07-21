import C01_fungsiDasar as fd

def askID(_usersData):
    """Meminta ID pengguna.

    Mengembalikan ID yang sudah valid."""
    Type = "id"
    Input = fd.strip(input("""Masukkan id pengguna. Ketik "uname" untuk menggunakan username pengguna
    
        ID : """))
    if not Input:
        print("ID tidak bisa kosong!")
        Input, Type = askID(_usersData)
    elif Input.lower() == "uname":
        Input, Type = askUName(_usersData)
    elif fd.mtrxFind(_usersData, Input, 0) == -1:
        print("ID tersebut tidak ditemukan.")
        Input, Type = askID(_usersData)

    return Input, Type
    

def askUName(_usersData):
    """Meminta username pengguna.
    
    Mengembalikan username yang sudah valid."""
    Type = "uname"
    Input = fd.strip(input("""Masukkan username pengguna. Ketik "id" untuk menggunakan ID pengguna

        Username : """))
    if not Input:
        print("Username tidak bisa kosong!")
        Input, Type = askUName(_usersData)
    elif Input.lower() == "id":
        Input, Type = askID(_usersData)
    elif fd.mtrxFind(_usersData, Input, 1) == -1:
        print("Username tersebut tidak ditemukan.")
        Input, Type = askUName(_usersData)

    return Input, Type
            

def askAmount(_usersData, person, Type):
    """Meminta jumlah penambahan saldo.
    
    Mengembalikan nilai yang sudah valid"""
    amount = fd.strip(input("Jumlah penambahan saldo : "))
    if amount == "batal":
        return
    try:
        amount = int(amount)
    except:
        if not amount:
            amount = 0
        else:
            print("Masukan hanya boleh berbentuk bilangan bulat!")
            amount = askAmount(_usersData, person, Type)
    else:
        if Type == "id":
            idx = 0
        else:
            idx = 1

        if _usersData[fd.mtrxFind(_usersData, person, idx)][5] + amount < 0:
            print("Jumlah yang dikurangi melebihi saldo yang dimiliki!")
            amount = askAmount(_usersData, person, Type)

        return amount


def topup(_usersData):
    """Menambahkan saldo pengguna.

    Mengembalikan matriks _usersData yang telah diubah."""
    Input, Type = askUName(_usersData)
    
    if Type == "id":
        idxType = 0
    else:
        idxType = 1

    idxPerson = fd.mtrxFind(_usersData, Input, idxType)

    print("\nSaldo = " + str(_usersData[idxPerson][5]))

    amount = askAmount(_usersData, Input, Type)
    
    _usersData[idxPerson][5] += amount
            
    if amount > 0:
        print("Saldo telah ditambah sebesar " + str(amount) + ".")
    elif amount == 0:
        print("Saldo tidak berubah.")
    else:
        print("Saldo telah dikurangi sebesar " + str(-amount) + ".")

    return _usersData


if __name__ == "__main__":
    pass
