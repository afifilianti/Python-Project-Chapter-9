#3

def bintang():
    for i in range(5):
        print(('*' * (1+2*i)).center(1+2*5))
    for i in reversed(range(4)):
        print(('*' * (1+2*i)).center(1+2*5))

bintang()
