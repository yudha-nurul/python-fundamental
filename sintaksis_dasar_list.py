# materi List
print('materi list')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']

print('\n>>>1. tampilkan value list daftar_buku')
print(daftar_buku)

# proses semua dengan for in
print('\n>>>2. proses semua dengan for in. ini akan menampilkan value satu persatu')
for buku in daftar_buku:
    print(buku)  # ini akan menampilkan value list daftar_buku satu persatu

# tampilkan isi daftar_buku pada index tertentu
print('\n>>>3. tampilkan isi daftar_buku pada index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

# tampilkan dengan for in range
print('\n>>>4. tampilkan dengan for in range')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# append = tambahkan 1 buku baru di index terakhir
print('\n5. append = tambahkan 1 buku baru di index terakhir')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']
print(daftar_buku)
daftar_buku.append('CADCAM')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# clear list (menghapus semua isi daftar buku)
print('\n6. clear list (menghapus semua isi daftar buku')
print(daftar_buku)
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# ganti index pertama
print('\n7. ganti index pertama')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']
print(daftar_buku)
daftar_buku[0] = 'geografi'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# pop = ambil index ke n dan simpan pada variabel tertentu
print('\n8. pop = ambil index ke n dan simpan pada variabel tertentu')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']
print(daftar_buku)
buku = daftar_buku.pop(0)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print(f'ini hasil dari elemen yang diambil: {buku}')

# pop =  menghapus elemen terakhir
print('\n9. pop =  menghapus elemen terakhir')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']
print(daftar_buku)
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# pop = menghapus /  mengambil index tertentu
print('\n10. pop = menghapus /  mengambil index tertentu')
daftar_buku = ['fisika', 'biologi', 'matamatika', 'kimia']
print(daftar_buku)
daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])