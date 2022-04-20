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

        # Cari terpanjang
        _terpanjang = 0
        for x in range(_count):
            for y in range(_jumlahGame):
                if(_daftarGame[x] == _gameData[y][0]):
                    for z in range(6):
                        if(len(str(_gameData[y][z])) > _terpanjang):
                            _terpanjang = len(str(_gameData[y][z]))

        s = '{: ^' + str(_terpanjang) + '}'     # Format penulisan

        for x in range(_count):
            for y in range(_jumlahGame):
                if(_daftarGame[x] == _gameData[y][0]):
                    print(str(x+1) +'. ' + s.format(_gameData[y][0]) +' | ' + s.format(_gameData[y][1]) + ' | ' +  s.format(_gameData[y][2]) + ' | ' + s.format(_gameData[y][3]) + ' | ' + s.format(_gameData[y][4]))
                    break



















