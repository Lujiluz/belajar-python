# python offers a "trick" where, operators like * and + have a different meaning depending on
# what kind of thing they're applied to. (The technical term for this is operator overloading)

spam_amount = 4
viking_song = "Spam " * spam_amount
print(viking_song)

# Question: Kenapa gua bisa campur operasi aritmatik antara string dan int hanya jika dikali, kalo ditambah gabisa?
# Answer: karena python tidak tahu cara mengubah angka menjadi string meggunakan operator +. Kalo operator * kan cuma 
# mengalikan string berdasarkan angka. Jadi tidak ada perubahan tipe data
