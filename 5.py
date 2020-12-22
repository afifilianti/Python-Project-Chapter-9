#5

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('==========================================')
print('NIM \t NAMA \t\t N.MID \t N.UAS')
print('------------------------------------------')
for i in range (len(nilai)):
    print((nilai[i]['nim']), '\t', (nilai[i]['nama'].ljust(10)), '\t', (nilai[i]['mid']), '\t', (nilai[i]['uas']))
print('------------------------------------------')
