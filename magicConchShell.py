def kerangAjaib():

    import time
    a = 2
    m = 6
    rn = time.time()
    c = 3

    arr = ["Ya","Tidak","Bisa Jadi","Mungkin","Tentunya","Tidak Mungkin"]
    k = input("Apa pertanyaanmu ? ")

    jawab = round(((a)*(rn) + (c))) % m

    print(arr[jawab])
