# type data list

daftar_buku = ['matematika', 'fisika', 'biologi', 'kimia']
print('>>>tampilkan daftar buku')
print(daftar_buku)

print('\n>>>proses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\n>>>atau bisa juga dengan seperti ini')
for i in daftar_buku:
    print(i)
print('hasilnya sama khan')

print('\n>>>tampilkan isi daftar buku pada index tertentu')
print(daftar_buku[0])  # index pertama dimulai dari 0
print(daftar_buku[-1])  # index terakhir (pertama dari belakang) adalah -1

print('\n>>>tampilkan dengan for in range')
daftar_buku = ['matematika', 'fisika', 'biologi', 'kimia']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nbisa juga tampilkan hanya range tertentu')
for i in range(0, 2):
    print(daftar_buku[i])

print('\n>>>tambahkan satu buku baru')
daftar_buku.append('cadcam')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n>>>clear : menghapus semua isi list')
daftar_buku = ['matematika', 'fisika', 'biologi', 'kimia']
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n>>>mengganti elemen pertama')
daftar_buku = ['matematika', 'fisika', 'biologi', 'kimia']
daftar_buku[0] = 'ilmu logam'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n>>>ambil elemen ke n dan simpan ke variabel tertentu')
daftar_buku = ['matematika', 'fisika', 'biologi', 'kimia']
buku = daftar_buku.pop(0)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print(f' ini elemen yg diambil: {buku} ')






