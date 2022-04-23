import C01_fungsiDasar as fd
import C02_fungsiBuatan as fb


def lihat(_userId,_gameData,_possession):
    # Cari ada berapa jumlah game yang kita miliki
    
    _jumlahGame = 0
    _panjangPossession = fd.len(_possession)
    for x in range(_panjangPossession):
        if(_possession[x][1] == _userId):
            _jumlahGame +=1

    _jumlahGameTotal = fd.len(_gameData)

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


        _length = fb.maxLengths(_gameData)
        line1 = "| {0[0]:^{1[0]}} | {0[1]:^{1[1]}} | {0[2]:^{1[2]}} | {0[3]:^{1[3]}} | {0[4]:^{1[4]}} | ".format(_gameData[0],_length)
        print("_"*fd.len(line1))
        print(line1)
        print("| {} | {} | {} | {} | {} |".format(_length[0]*'-',_length[1]*'-',_length[2]*'-',_length[3]*'-',_length[4]*'-'))
        for x in range(_count):
            for y in range(_jumlahGameTotal):
                if(_daftarGame[x] == _gameData[y][0]):
                    print("| {0[0]:<{1[0]}} | {0[1]:<{1[1]}} | {0[2]:<{1[2]}} | {0[3]:<{1[3]}} | {0[4]:<{1[4]}} |".format(_gameData[y],_length))
                    break
        print('‾' * fd.len(line1))




















