import fungsiDasar as fd

def askGName(gameData):
    """Meminta nama game.
    
    Mengembalikan nama game yang sudah valid."""
    gName = fd.strip(input("Nama game : "))
    if not gName:
        print("Nama game tidak boleh kosong!")
        gName = askGName(gameData)
    elif fd.mtrxFind(gameData, gName, 1) != -1:
        print("Game tersebut sudah ada!")
        gName = askGName(gameData)

    return gName


def askCategory():
    """Meminta nama kategori.
    
    Mengembalikan nama kategori yang sudah valid."""
    category = fd.strip(input("Kategori : "))
    if not category:
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
        if not releaseYear:
            releaseYear = 2022
            print("Harga diatur menjadi {} (gratis)".format(releaseYear))
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
        if not price or price.lower == "gratis" or price.lower == "free":
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
        if not stock:
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


def addGame(gameData):
    """Menambahkan game.

    Mengembalikan matriks gameData yang sudah diubah"""
    id = "G" + '0'*(3 - fd.len(str(fd.len(gameData)))) + str(fd.len(gameData))
    gName = askGName(gameData)
    category = askCategory()
    releaseYear = askRelease()
    price = askPrice()
    stock = askStock()

    gameData = fd.append(gameData, [id, gName, category, releaseYear, price, stock])
    return gameData


if __name__=="__main__":
    pass
