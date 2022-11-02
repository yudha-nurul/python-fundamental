# ==========materi list comprehension
print('\n>>>>>Materi List comprehension')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)

# >>1. perintah del dengan list comprehension
print('\n>>1. perintah del dengan list comprehension')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)
del daftar_buku[0]  # menghapus index ke 1 dalam list
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# 2. menghapus semua elemen dalam index daftar buku
print('\n>>2. menghapus semua elemen dalam index daftar buku')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)
del daftar_buku[:]  # menghapus semua elemen dalam index daftar buku
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# 3. menghapus index ke 1 dan 2 (0 & 1)
print('\n>>3. menghapus index ke 1 dan 2 (0 & 1)')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)
del daftar_buku[0:2]  # menghapus index ke 1 dan 2 (0 & 1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# >>4. perintah del dengan list comprehension START : END : STEP
print('\n>>4. perintah del dengan list comprehension START : END : STEP')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)
del daftar_buku[0::2]  # perintah del dengan list comprehension START : END : STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# 5. membuat list dari list yang sudah ada
print('\n5. membuat list dari list yang sudah ada')
daftar_buku = ['fisika', 'biologi', 'matematika', 'kimia']
print(daftar_buku)
daftar_buku_baru = daftar_buku[:]  # 6. harus ditambah ini ([:]) untuk benar2 baru
print(daftar_buku_baru)

# 7. list lama dihapus, list baru tetep exist
print('\n7. list lama dihapus, list baru tetep exist')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# 8. membuat list comprehension genap
print('\n8. membuat list comprehension genap')
daftar_buku = [1, 2, 3, 4, 5, 6]
print(daftar_buku)
daftar_buku_baru = daftar_buku[1::2]
print(daftar_buku_baru)

# 9. membuat list comprehension, buang elemen terakhir
print('\n9. membuat list comprehension, buang elemen terakhir')
daftar_buku = [1, 2, 3, 4, 5, 6]
print(daftar_buku)
daftar_buku_baru = daftar_buku[0:-1:]
print(daftar_buku_baru)

# 10. membuat list comprehension ganjil
print('\n10. membuat list comprehension ganjil')
daftar_buku = [1, 2, 3, 4, 5, 6]
print(daftar_buku)
daftar_buku_baru = daftar_buku[0::2]
print(daftar_buku_baru)
