# ==========materi list comprehension
print('\n>>>>>Materi List comprehension')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)

# >>perintah del dengan list comprehension
print('\n>>perintah del dengan list comprehension')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
del daftar_buku[0]  # menghapus index ke 1 dalam list
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# menghapus semua elemen dalam index daftar buku
print('\n>>menghapus semua elemen dalam index daftar buku')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
del daftar_buku[:]  # menghapus semua elemen dalam index daftar buku
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# menghapus index ke 1 dan 2 (0 & 1)
print('\n>>menghapus index ke 1 dan 2 (0 & 1)')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
del daftar_buku[0:2]  # menghapus index ke 1 dan 2 (0 & 1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# >>perintah del dengan list comprehension START : END : STEP
print('\n>>perintah del dengan list comprehension START : END : STEP')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
del daftar_buku[0::2]  # perintah del dengan list comprehension START : END : STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# membuat list dari list yang sudah ada

# harus ditambah ini ([:]) untuk benar2 baru

# list lama dihapus, list baru tetep exist

# membuat list comprehension genap

# membuat list comprehension, buang elemen terakhir

# membuat list comprehension ganjil
