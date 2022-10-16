"""
program perulangan membaca buku  sampai paham
"""
# perulangan dengan while dengan penanda henti
jumlah_buku = 10
jumlah_baca = 0
jumlah_paham = 0
print(f'jumlah buku adalah {jumlah_buku}')
print(f'jumlah buku yang sudah dibaca adalah {jumlah_paham}')
while jumlah_baca < jumlah_buku + 3:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 8:
        print(f'buku ke {jumlah_paham + 1} belum paham')
    else:
        jumlah_paham = jumlah_paham + 1
        print(f'buku ke {jumlah_paham} sudah dibaca dan dipahami')

print(f'jumlah buku yang sudah dibaca dan dipahami adalah {jumlah_paham}')
if jumlah_paham == jumlah_buku:
    print('semua buku sudah saya baca dan pahami bu,,,')
else:
    print(f'tidak semua buku saya pahami, saya hanya paham {jumlah_paham} buku')
print('selesai,,,,')
