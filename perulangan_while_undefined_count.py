"""
bissmillah
program perulangan membaca buku sampai paham
"""
jumlah_buku = 10
jumlah_paham = 0
jumlah_dibaca = 0

print(f'jumlah buku adalah {jumlah_buku}')
print('ibu berkata "budi,, ayo baca buku dan pahami"')

while jumlah_dibaca < jumlah_buku + 3:
    jumlah_dibaca = jumlah_dibaca + 1
    if jumlah_paham == 10:
        print(f'buku ke {jumlah_paham} belum dipahami')
    else:
        print(f'buku ke {jumlah_paham} sudah dibaca dan dipahami')
        jumlah_paham = jumlah_paham + 1
if jumlah_paham == jumlah_buku:
    print('semua buku sudah dibaca dan dipahami')
else:
    print('tidak semua buku bisa dipahami')
print('selesai,,,,,')
