#4

import random
def shuffleString(x, n):
    hasil = []
    i = 0
    while i < n:
        acak = ''.join(random.sample(x, len(x)))
        if acak not in hasil:
            hasil += [acak]
            i += 1
    print(hasil)

shuffleString('kita', 5)
