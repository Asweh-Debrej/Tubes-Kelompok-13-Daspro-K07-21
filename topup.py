import fungsiDasar as fd

def askID(usersData):
    """Meminta ID pengguna.

    Mengembalikan ID yang sudah valid."""
    print("-"*100)
    Type = "id"
    Input = fd.strip(input("""Masukkan "uname" untuk menggunakan user pengguna
    
        ID : """))
    if not Input:
        print("ID tidak bisa kosong!")
        Input, Type = askID(usersData)
    elif Input.lower() == "uname":
        Input, Type = askUName(usersData)
    elif fd.mtrxFind(usersData, Input, 0) == -1:
        print("ID tersebut tidak ditemukan.")
        Input, Type = askID(usersData)

    return Input, Type
    

def askUName(usersData):
    """Meminta username pengguna.
    
    Mengembalikan username yang sudah valid."""
    print("-"*100)
    Type = "uname"
    Input = fd.strip(input("""Masukkan "id" untuk menggunakan ID pengguna

        Username : """))
    if not Input:
        print("Username tidak bisa kosong!")
        Input, Type = askUName(usersData)
    elif Input.lower() == "id":
        Input, Type = askID(usersData)
    elif fd.mtrxFind(usersData, Input, 1) == -1:
        print("Username tersebut tidak ditemukan.")
        Input, Type = askUName(usersData)

    return Input, Type
            

def askAmount(usersData, person, Type):
    """Meminta jumlah penambahan saldo.
    
    Mengembalikan nilai yang sudah valid"""
    print("-"*100)
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
            amount = askAmount(usersData, person, Type)
    else:
        if Type == "id":
            idx = 0
        else:
            idx = 1

        if usersData[fd.mtrxFind(usersData, person, idx)][5] + amount < 0:
            print("Jumlah yang dikurangi melebihi saldo yang dimiliki!")
            amount = askAmount(usersData, person, Type)

        return amount


def topup(usersData):
    """Menambahkan saldo pengguna.

    Mengembalikan matriks usersData yang telah diubah."""
    Input, Type = askUName(usersData)
    
    if Type == "id":
        idxType = 0
    else:
        idxType = 1

    idxPerson = fd.mtrxFind(usersData, Input, idxType)

    print("\nSaldo = " + str(usersData[idxPerson][5]))

    amount = askAmount(usersData, Input, Type)
    
    usersData[idxPerson][5] += amount
            
    if amount > 0:
        print("Saldo telah ditambah sebesar " + str(amount) + ".")
    elif amount == 0:
        print("Saldo tidak berubah.")
    else:
        print("Saldo telah dikurangi sebesar " + str(-amount) + ".")

    return usersData


if __name__ == "__main__":
    import tes
    print(topup(tes.usersData))