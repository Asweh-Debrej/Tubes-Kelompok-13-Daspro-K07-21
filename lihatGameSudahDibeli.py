import fungsiDasar as fd

def lihat(_userId,_gameData,_possession):
    # Cari ada berapa jumlah game yang kita miliki
    _jumlahGame = 0
    _panjangPossession = fd.len(_possession)
    for x in range(_panjangPossession):
        if(_possession[x][1] == _userId):
            _jumlahGame +=1

    if(_jumlahGame == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        # Print game - game tersebut
        _daftarGame = ['' for x in range(_jumlahGame)]
        _count = 0

        for x in range(_panjangPossession):
            if(_possession[x][1] == _userId):
                _daftarGame[_count] = _possession[x][0]
                _count +=1

        for x in range(_count):
            for y in range(_jumlahGame):
                if(_daftarGame[x] == _gameData[y][0]):
                    print(str(x+1) +'. ' + str(_gameData[y][0]) + '\t | ' + str(_gameData[y][1]) + '\t | ' + str(_gameData[y][2]) + "\t | " + str(_gameData[y][3]) + "\t | " + str(_gameData[y][4]))
                    break



















