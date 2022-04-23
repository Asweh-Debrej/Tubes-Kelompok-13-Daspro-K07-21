import C01_fungsiDasar as fd

def search_game_at_store(_gamedata):

    k= fd.len(_gamedata)
    str1=input("Masukkan ID Game: ")
    str2=input("Masukkan Nama Game: ")
    str3= input("Masukkan Harga Game: ")
    str4=input("Masukkan Kategori Game: ")
    str5= input("Masukkan Tahun Rilis Game: ")


    print("Daftar game pada toko yang memenuhi kriteria: ")
     
    t=0
    if(str1!=''):
                    
         for j in range (k):
             if(str1.lower() ==_gamedata[j][0].lower()):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")
    elif(str2!=''):
                    
         for j in range (k):
             if(str2.lower() ==_gamedata[j][1].lower()):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")
    
    elif(str3!='' and str4!='' and str5!=''):



         for j in range (k):
             if(str3 == str(_gamedata[j][4]) and str4.lower() ==_gamedata[j][2].lower() and str5 == str(_gamedata[j][3])):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(str3!='' and str4!=''):

         for j in range (k):
             if(str3 == str(_gamedata[j][4]) and str4.lower() ==_gamedata[j][2].lower()):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(str4!='' and str5!=''):

         for j in range (k):
             if(str4.lower() ==_gamedata[j][2].lower() and str5 == str(_gamedata[j][3])):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(str3!='' and str5!=''):

         for j in range (k):
             if(str3 == str(_gamedata[j][4])) and str5 == str(_gamedata[j][3]):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(str3!=''):
         for j in range (k):
             if(str3 == str(_gamedata[j][4])):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(str4!=''):
                    
         for j in range (k):
             if(str4.lower() == _gamedata[j][2].lower()):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    elif(str5!=''):
         for j in range (k):
             if(str5 ==str(_gamedata[j][4])):
                 print()
                 t+=1
                 print(t,end=". ")
                 print(_gamedata[j][0],end=" | ")
                 print(_gamedata[j][1],end=" | ")
                 print(_gamedata[j][2],end=" | ")
                 print(_gamedata[j][3],end=" | ")
                 print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()

             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")

    else :
         for j in range (k):
            print()
            t+=1
            print(t,end=". ")
            print(_gamedata[j][0],end=" | ")
            print(_gamedata[j][1],end=" | ")
            print(_gamedata[j][2],end=" | ")
            print(_gamedata[j][3],end=" | ")
            print(_gamedata[j][4],end="")
                    
         if(t==0):
             print()
             print("Tidak ada game pada toko yang memenuhi kriteria.",end="")
            
      


            
      

