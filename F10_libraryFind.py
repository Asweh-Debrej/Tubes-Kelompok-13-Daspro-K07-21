import C01_fungsiDasar as fd

def search_my_game(_possession,_gamedata,_loggedUser):
     
     username = _loggedUser[0]
     x =fd.len(_possession) 
     k= fd.len(_gamedata)
     str1=input("Masukkan ID Game: ")
     str2=input("Masukkan Tahun Rilis Game: ")
     print("Daftar game pada inventory yang memenuhi kriteria: ")
     
     t=0
     if(str1=='' and str2 ==''):
          
          for m in range (x):
               
               if(_possession[m][1]==username):
                    
                    for j in range (k):
                         if(_possession[m][0]==_gamedata[j][0]):
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
                    print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")
     elif(str1!='' and str2!=''):

          for m in range (x):
               if(_possession[m][1]==username):
                 
                 for j in range (k):
                    if(_possession[m][0]==_gamedata[j][0] and str1.lower() == _gamedata[j][0].lower() and str2 ==_gamedata[j][4] ):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")

     elif(str1!='' and str2==''):

          for m in range (x):
               if(_possession[m][1]==username):
                 
                 for j in range (k):
                    if(_possession[m][0]==_gamedata[j][0] and str1.lower() == _gamedata[j][0].lower()):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")

     elif(str1=='' and str2!=''):

          for m in range (x):
               if(_possession[m][1]==username):
                 
                 for j in range (k):
                    if(_possession[m][0]==_gamedata[j][0] and  int(str2) ==_gamedata[j][4] ):
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
               print("Tidak ada game pada inventory-mu yang memenuhi kriteria.",end="")
                    
