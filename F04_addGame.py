import C01_fungsiDasar as fd

def askGName(_gameData):
    """Meminta nama game.
    
    Mengembalikan nama game yang sudah valid."""
    gName = fd.strip(input("Nama game : "))
    if gName == '':
        print("Nama game tidak boleh kosong!")
        gName = askGName(_gameData)
    elif fd.mtrxFind(_gameData, gName, 1) != -1:
        print("Game tersebut sudah ada!")
        gName = askGName(_gameData)

    return gName


def askCategory():
    """Meminta nama kategori.
    
    Mengembalikan nama kategori yang sudah valid."""
    category = fd.strip(input("Kategori : "))
    if category == '':
        print("Kategori tidak boleh kosong!")
        category = askCategory()

    return category


def askRelease():
    """Meminta tahun rilis game.
    
    Mengembalikan tahun yang sudah valid."""
    releaseYear = fd.strip(input("Tahun rilis : "))
    try:
        releaseYear = int(releaseYear)
    except:
        if releaseYear == '':
            releaseYear = 2022
            print("Tahun diatur menjadi {}.".format(releaseYear))
        else:
            print("Tahun rilis harus berupa bilangan bulat!")   # Tahun rilis mungkin saja sebelum masehi
            releaseYear = askRelease()
    else:
        if releaseYear > 2022:
            print("Game yang dijual harus sudah dirilis!")
            releaseYear = askRelease()

    return releaseYear


def askPrice():
    """Meminta harga game.
    
    Mengembalikan harga yang sudah valid."""
    price = fd.strip(input("Harga game : "))
    try:
        price = int(price)
    except:
        if price == '' or price.lower == "gratis" or price.lower == "free":
            price = 0
            print("Harga diatur menjadi {} (gratis).".format(price))
        else:
            print("Harga harus berupa bilangan bulat tak negatif!")
            price = askPrice()
    else:
        if price < 0:
            print("Harga harus berupa bilangan bulat tak negatif!")
            price = askPrice()

    return price


def askStock():
    """Meminta jumlah stok game.

    Mengembalikan jumlah stok yang sudah valid."""
    stock = fd.strip(input("Jumlah stok : "))
    try:
        stock = int(stock)
    except:
        if stock == '':
            stock = 0
            print("Stok diatur menjadi {}.".format(stock))
        else:
            print("Stok harus berupa bilangan bulat tak negatif!")
            stock = askStock()
    else:
        if stock < 0:
            print("Stok harus berupa bilangan bulat tak negatif!")
            stock = askStock()

    return stock


def addGame(_gameData):
    """Menambahkan game.

    Mengembalikan matriks _gameData yang sudah diubah"""
    id = "G" + '0'*(3 - fd.len(str(fd.len(_gameData)))) + str(fd.len(_gameData))
    gName = askGName(_gameData)
    category = askCategory()
    releaseYear = askRelease()
    price = askPrice()
    stock = askStock()

    _gameData = fd.append(_gameData, [id, gName, category, releaseYear, price, stock])
    print("\nGame {} berhasil ditambahkan dengan id = {}.".format(gName, id))

    return _gameData


if __name__=="__main__":
    pass
