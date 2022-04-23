import C01_fungsiDasar as fd
import C02_fungsiBuatan as fb 

def selection_sort(_skemaSorting,_arrData):
    # Melakukan selection sort dan mengprint hasilnya
    _banyakData = fd.len(_arrData)

    for x in range(1, _banyakData):
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

      #print matriks
    _lengths = fb.maxLengths(_arrData)
    line1 = "| {0[0]:^{1[0]}} | {0[1]:^{1[1]}} | {0[4]:^{1[4]}} | {0[2]:^{1[2]}} | {0[3]:^{1[3]}} | {0[5]:^{1[5]}} |".format(_arrData[0],_lengths)
    print('_'*fd.len(line1))
    print(line1)
    print("| {} | {} | {} | {} | {} | {} |".format(_lengths[0]*'-',_lengths[1]*'-',_lengths[4]*'-',_lengths[2]*'-',_lengths[3]*'-',_lengths[5]*'-'))
    for i in range(1, fd.len(_arrData)):
        print("| {0[0]:<{1[0]}} | {0[1]:<{1[1]}} | {0[4]:<{1[4]}} | {0[2]:<{1[2]}} | {0[3]:<{1[3]}} | {0[5]:<{1[5]}} |".format(_arrData[i], _lengths))
    print('‾'*fd.len(line1))


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

    print("Daftar skema sorting : ")
    print("     - harga+    : mensortir berdasarkan harga termurah -> termahal ")
    print("     - harga-    : mensortir berdasarkan harga termahal -> termurah ")
    print("     - tahun+    : mensortir berdasarkan tahun rilis terlama -> terbaru ")
    print("     - tahun+    : mensortir berdasarkan tahun rilis terlama -> terbaru ")
    print('')
    _skemaSorting = input("Skema sorting : ")
    
    if(fd.len(_skemaSorting) == 6):
        for x in range(6):
            _skemaSorting[x] = _skemaSorting[x].lower()
            
        if (_skemaSorting == "tahun+" or _skemaSorting == "tahun-" or _skemaSorting == "harga+" or _skemaSorting == "harga-" or _skemaSorting == ""):
            selection_sort(_skemaSorting,_arrData)
        else:
            print("Skema sorting tidak valid")

    else:
        print("Skema sorting tidak valid")

