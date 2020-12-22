#1

def ubahHuruf(teks, a, b):
    text = list(teks)
    hasil = ' '
    for i in text:
        if i == a:
            i = b
        hasil = ''.join([hasil, i])
    return hasil

print(ubahHuruf('BAYANG', 'B', 'S'))
