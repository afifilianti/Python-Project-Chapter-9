#6

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('================================================================')
print('NIM \t NAMA \t\t N.MID \t N.UAS \t N.AKHIR \t STATUS')
print('----------------------------------------------------------------')
for i in range (len(nilai)):
    nilaiAkhir = int(((nilai[i]['mid']) + (2*(nilai[i]['uas'])))/3)
    if nilaiAkhir >=60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print((nilai[i]['nim']), '\t', (nilai[i]['nama'].ljust(10)), '\t', (nilai[i]['mid']), '\t', (nilai[i]['uas']), '\t', nilaiAkhir, '\t\t', status)
print('----------------------------------------------------------------')
