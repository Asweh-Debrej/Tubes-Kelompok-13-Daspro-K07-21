toe = [['#' for j in range(3)]for i in range(3)]
truth = [['0' for j in range(3)]for i in range(3)]

print("Selamat Datang di Game TicTacToe ini")
print("Silakan dibacakan petunjuk permainan ini")

print("Di dalam permainan ini X akan jalan duluan baru O")
print("Pertama - tama tentukan siapa yang akan jalan duluan")
print("untuk memilih petak, hanya masukan angka di input baris dan kolom pada matrix")
print("Ketahuilah apa itu baris dan kolom jika belum tau")
print("untuk memilih baris teratas masukan indeks 0, baris tengah masukan indeks 1, dan baris bawah masukan indeks 2")
print("untuk memilih kolom terkiri masukan indeks 0, kolom tengah masukan indeks 1, dan kolom terkanan masukan indeks 2")

def check():
     if(toe[0][0]=='X'and toe[0][1]=='X'and toe[0][2]=="X" or toe[1][0]=='X'and toe[1][1]=='X'and toe[1][2]=="X" or toe[2][0]=='X'and toe[2][1]=='X'and toe[2][2]=="X"):
        for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()

        print("X menang secara horizontal")
        exit()
     elif(toe[0][0]=='X'and toe[1][0]=='X'and toe[2][0]=="X" or toe[0][1]=='X'and toe[1][1]=='X'and toe[2][1]=="X" or toe[0][2]=='X'and toe[1][2]=='X'and toe[2][2]=="X"):
         for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
         print("X menang secara Vertikal")
         exit()
     elif(toe[0][0]=='X'and toe[1][1]=='X'and toe[2][2]=="X" or toe[0][2]=='X'and toe[1][1]=='X'and toe[2][0]=="X" ):
         for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
         print("X menang secara horizontal")
         exit()
     if(toe[0][0]=='O'and toe[0][1]=='O'and toe[0][2]=='O' or toe[1][0]=='O'and toe[1][1]=='O'and toe[1][2]=="O" or toe[2][0]=='O'and toe[2][1]=='O'and toe[2][2]=="O"):
         for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
         print("O menang secara horizontal")
         exit()
     elif(toe[0][0]=='O'and toe[1][0]=='O'and toe[2][0]=="O" or toe[0][1]=='O'and toe[1][1]=='O'and toe[2][1]=="O" or toe[0][2]=='O'and toe[1][2]=='O'and toe[2][2]=="O"):
        for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
        print("O menang secara Vertikal")
        exit()
     elif(toe[0][0]=='O'and toe[1][1]=='O'and toe[2][2]=="O" or toe[0][2]=='O'and toe[1][1]=='O'and toe[2][0]=="O" ):
         for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
         print("O menang secara horizontal")
         exit()


n=9


while(n>0):
    if(n%2==1):
        print("Giliran X untuk jalan, Sekarang Silakan lihat petak tictactoe ini terlebih dahulu")
        m=1
        for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
        while(m==1):

            baris = int(input("Masukan indeks baris: "))
            kolom = int (input("Masukan indeks kolom: "))
            if(truth[baris][kolom]=='0'):
                toe[baris][kolom]='X'
                truth[baris][kolom]='1'
                m=0
                n-=1
                check()
            else :
                print("Masukan sudah diisi sehingga langkah anda tidak valid, Ulangi masukan dengan benar!!!")
                print("Dengan cara mengisi yang kosong pada petak diatas")
    else :
        
        print("Giliran O  untuk jalan, Sekarang Silakan lihat petak tictactoe ini terlebih dahulu")
        m=1
        for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
        while(m==1):

            baris = int(input("Masukan indeks baris: "))
            kolom = int (input("Masukan indeks kolom: "))
            if(truth[baris][kolom]=='0'):
                toe[baris][kolom]='O'
                truth[baris][kolom]='1'
                m=0
                n-=1
                check()
            else :
                print("Masukan sudah diisi sehingga langkah anda tidak valid, Ulangi masukan dengan benar!!!")
                print("Dengan cara mengisi yang kosong pada petak diatas")

if(n==0):
        for i in range(3):
            for j in range(3):
                print (toe[i][j],end="")
            print()
        print("Seri. Tidak ada yang menang")
        print("Terima Kasih Sudah memainkan game ini, Ulangi jika ingin memainkannya lagi")
        exit()



