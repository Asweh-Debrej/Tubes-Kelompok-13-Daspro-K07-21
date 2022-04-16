import fungsiDasar as fd

def askID(usersData):
    print("-"*50)
    Type = "id"
    Input = input("""Masukkan "uname" untuk menggunakan user pengguna
    
        ID : """)
    if not Input:
        print("ID tidak bisa kosong!")
        Input, Type = askID(usersData)
    elif Input.lower() == "uname":
        Input, Type = askUName(usersData)
    else:
        found = False
        for data in usersData:
            if Input == data[0]:
                found = True
        if not found:
            print("ID tersebut tidak ditemukan.")
            Input, Type = askID(usersData)

    return Input, Type
    

def askUName(usersData):
    print("-"*50)
    Type = "uname"
    Input = input("""Masukkan "id" untuk menggunakan ID pengguna

        Username : """)
    if not Input:
        print("Username tidak bisa kosong!")
        Input, Type = askUName(usersData)
    elif Input.lower() == "id":
        Input, Type = askID(usersData)
    else:
        found = False
        for data in usersData:
            if Input == data[1] and not found:
                found = True
        if not found:
            print("Username tersebut tidak ditemukan.")
            Input, Type = askUName(usersData)

    return Input, Type
            

def askAmount(usersData, person, Type):
    print("-"*50)
    amount = fd.strip(input("Jumlah penambahan saldo : "))
    try:
        amount = int(amount)
    except:
        print("Masukan hanya boleh berbentuk bilangan bulat!")
        amount = askAmount(usersData, person, Type)
    else:
        if Type == "id":
            idx = 0
        else:
            idx = 1

        found = False
        for i in usersData:
            if i[idx] == person and not found:
                found = True
                if i[5] + amount < 0:
                    print("Jumlah yang dikurangi melebihi saldo yang dimiliki!")
                    amount = askAmount(usersData, person, Type)

        return amount


def topup(usersData):
    Input, Type = askUName(usersData)
    
    idxPerson = 0
    found = False
    if Type == "id":
        idxType = 0
    else:
        idxType = 1

    for i in range(fd.len(usersData)):
        if usersData[i][idxType] == Input and not found:
            found = True
            idxPerson = i

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