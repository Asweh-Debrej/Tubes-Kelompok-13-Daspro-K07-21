import fungsiDasar as fd

def selection_sort(_skemaSorting,_arrData):
    # Melakukan selection sort dan mengprint hasilnya
    _banyakData = fd.len(_arrData)

    for x in range(_banyakData-1):
        _indeksMaks = x

        for y in range(x+1,_banyakData):
            if(_skemaSorting == "tahun+"):
                if(_arrData[_indeksMaks][3] > _arrData[y][3]):
                    _indeksMaks = y
            elif(_skemaSorting == "tahun-"):
                if (_arrData[_indeksMaks][3] < _arrData[y][3]):
                    _indeksMaks = y
            elif(_skemaSorting == "harga+"):
                if (_arrData[_indeksMaks][4] > _arrData[y][4]):
                    _indeksMaks = y
            elif(_skemaSorting == "harga-"):
                if (_arrData[_indeksMaks][4] < _arrData[y][4]):
                    _indeksMaks = y
            else:
                if(int(_arrData[_indeksMaks][0][1:]) > int(_arrData[y][0][1:])):
                    _indeksMaks = y

        # Lakukan penukaran
        _temp0  = _arrData[_indeksMaks][0]
        _temp1  = _arrData[_indeksMaks][1]
        _temp2  = _arrData[_indeksMaks][2]
        _temp3  = _arrData[_indeksMaks][3]
        _temp4  = _arrData[_indeksMaks][4]

        _arrData[_indeksMaks][0]    = _arrData[x][0]
        _arrData[_indeksMaks][1]    = _arrData[x][1]
        _arrData[_indeksMaks][2]    = _arrData[x][2]
        _arrData[_indeksMaks][3]    = _arrData[x][3]
        _arrData[_indeksMaks][4]    = _arrData[x][4]

        _arrData[x][0]  = _temp0
        _arrData[x][1]  = _temp1
        _arrData[x][2]  = _temp2
        _arrData[x][3]  = _temp3
        _arrData[x][4]  = _temp4

    for x in range(_banyakData):
        print(str(x+1) +'. ' + str(_arrData[x][0]) +"\t | " + str(_arrData[x][1]) + "\t | " + str(_arrData[x][4]) +"\t | " + str(_arrData[x][2]) + "\t | " + str(_arrData[x][3]) + "\t | " + str(_arrData[x][5]))



def listing_game(game):
    # Fungsi utama
    _banyakData = fd.len(game)
    _arrData= [[0 for x in range(6)] for x in range(_banyakData)]


    for x in range(_banyakData):
        _arrData[x][0]  = game[x][0]
        _arrData[x][1]  = game[x][1]
        _arrData[x][2]  = game[x][2]
        _arrData[x][3]  = game[x][3]
        _arrData[x][4]  = game[x][4]
        _arrData[x][5]  = game[x][5]

    _skemaSorting = input("Skema sorting : ")

    if (_skemaSorting == "tahun+" or _skemaSorting == "tahun-" or _skemaSorting == "harga+" or _skemaSorting == "harga-" or _skemaSorting == ""):
        selection_sort(_skemaSorting,_arrData)
    else:
        print("Skema sorting tidak valid")
