"""
program perulangan membaca buku  sampai paham
"""
# perulangan dengan while dengan penanda henti
book_count = 10
read_count = 0
understood_count = 0
print(f'jumlah buku adalah {book_count}')
print(f'jumlah buku yang sudah dibaca adalah {understood_count}')
while read_count < book_count + 3:
    read_count = read_count + 1
    if understood_count == 8:
        print(f'buku ke {understood_count + 1} belum paham')
    else:
        understood_count = understood_count + 1
        print(f'buku ke {understood_count} sudah dibaca dan dipahami')

print(f'jumlah buku yang sudah dibaca dan dipahami adalah {understood_count}')
if understood_count == book_count:
    print('semua buku sudah saya baca dan pahami bu,,,')
else:
    print(f'tidak semua buku saya pahami, saya hanya paham {understood_count} buku')
print('selesai,,,,')
