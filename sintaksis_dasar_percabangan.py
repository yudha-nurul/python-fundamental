# Sequential
print('Ibu berkata, "belikan ibu sebotol susu"')
print('Budi menjawab, "Baik bu,, apa yang harus saya lakukan ditoko?"')
print('Ibu menjawab, "Beli satu botol susu"')
print('maka Budi Berangkat ke Toko')
print('dan mulai berbelanja')

# Percabangan, contoh 1
jumlah_botol_susu_ditoko = 0
print(f'Budi melihat bahwa ada {jumlah_botol_susu_ditoko} botol susu di toko')
if jumlah_botol_susu_ditoko > 0:
    print('maka Budi membeli 1 botol susu')
else:
    print('maka Budi tidak jadi membeli susu')
print('dan kembali pulang ke rumah')
print('=' * 50)
print('=' * 50)

# Percabangan, contoh 2, dari joke programmer
"""
-ibu berkata: tolong pergi ketoko dan beli 1 botol susu, jika disana ada telur, bawa 6.
-lalu saya kembali membawa 6 botol susu.
-ibu berkata: kenapa kamu bawa 6 botol susu?
-karena ditoko ada telur. :-)
tugas: dari dialog diatas, buat flowchart yg benar dan tulis programnya 
"""

print("ibu berkata: tolong pergi ketoko dan beli 1 botol susu")
print("jika disana ada telur, bawa 6")
print('baik bu, lalu saya pun pergi ketoko')
jumlah_botol_susu = 5
jumlah_telur = 1
print(f'ketika sampai ditoko, saya melihat ada {jumlah_botol_susu} botol susu dan {jumlah_telur} butir telur')
if jumlah_botol_susu > 0:
    if jumlah_telur > 0:
        print('>>>lalu saya pulang dengan membawa 6 botol susu')
    else:
        print('>>>lalu saya pulang dengan membawa 1 botol susu')
else:
    print(">>>lalu saya pulang tidak membawa apa-apa")
print('selesai')



