import fungsiDasar as fd

def printf(string, width= 48, fence= '|', style= '2', indent= 2):
    """Mencetak string pada layar dengan pemosisian string masukan

    fence   : pagar/pinggiran yang menjadi pembatas string

    style   : posisi string akan dicetak
              1/left    = kiri,
              2/center  = tengah,
              3/right   = kanan

    indent  : penambahan spasi sebelum pagar
    """
    print(indent * ' ')
    if (str(style) == '1') or (str(style).lower() == "left"):
        print(fence + string + (width - fd.len(string)) * ' ' + fence)
    elif (str(style) == '2') or (str(style).lower() == "center"):
        print(fence + ((width - fd.len(string) + 1)//2) * ' ' + string + ((width - fd.len(string))//2) * ' ' + fence)
    elif (str(style) == '3') or (str(style).lower() == "right"):
        print(fence + (width - fd.len(string)) * ' ' + string + '|')

if __name__ == "__main__":                  # Kalau mau tes kode silahkan ubah isi ini dan run codenya
    pass