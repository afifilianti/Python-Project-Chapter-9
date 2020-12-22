#7

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('================================================================')
print('NIM'.ljust(8), 'NAMA MAHASISWA'.ljust(23), 'TGL LAHIR'.ljust(15), 'TEMPAT LAHIR'.ljust(15))
print('----------------------------------------------------------------')
for i in range (len(mhs)):
    data = mhs[i]
    a, b, c, d = data.split(':')
    thn, bln, tgl = c.split('-')
    formatTgl = '/'.join([tgl, bln, thn])
    print(a.ljust(8), b.ljust(23), formatTgl.ljust(15), d.ljust(15))
print('----------------------------------------------------------------')
