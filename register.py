import fungsiDasar as fd

_valChars = []

# Pengisian karakter yang valid
for i in range(97, 123):
    _valChars = fd.append(_valChars, chr(i))
for i in range(65, 91):
    _valChars = fd.append(_valChars, chr(i))
_valChars = fd.append(_valChars, chr(45))
_valChars = fd.append(_valChars, chr(95))

def register():
    name = input("Masukkan nama : ")
    valid = True
    for i in name:
        if i not in _valChars:
            valid = False
    while not valid:
        print("Hanya alfabet(a-z), minus(-), dan underscore(_) yang diperbolehkan!")
        name = input("Masukkan nama : ")
        valid = True
        for i in name:
            if i not in _valChars:
                valid = False

    uName = input("Masukkan username : ")
    