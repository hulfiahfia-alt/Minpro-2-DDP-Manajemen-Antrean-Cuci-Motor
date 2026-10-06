# Minpro-2-DDP-Manajemen-Antrean-Cuci-Motor
NAMA: FIA HULFIAH

NIM: 2609116078


# Deskripsi Program
Program ini merupakan aplikasi manajemen antrean cuci motor berbasis terminal yang dibuat menggunakan bahasa pemrograman Python. Program ini adalah pengembangan dari Mini Project 1. Sebelum dapat menggunakan program, pengguna harus melakukan login terlebih dahulu. Setelah login berhasil, menu yang ditampilkan akan disesuaikan dengan status akun pengguna, yaitu:

a. Admin dapat menambah, melihat, mengubah, dan menghapus data antrean.

b. User hanya dapat melihat daftar antrean.

Data akun disimpan pada dictionary User, sedangkan data antrean disimpan pada dictionary Antrean dengan plat motor sebagai key.


Akun yang dapat digunakan untuk mencoba program adalah sebagai berikut.


| Username | Password | Status |
|----------|----------|--------|
| admin    | admin123 | admin  |
| user1    | user123  | user   |



# Cara menjalankan program:


pip install pwinput prettytable
python minpro2.py


# Flowchart
<img width="1290" height="1172" alt="fllowchart minpro2 (1)" src="https://github.com/user-attachments/assets/072dd1ea-3d78-43e7-8935-6c5934f1fdae" />


# Penjelasan Alur Flowchart


1. Program dimulai, kemudian memanggil fungsi login()
   
2. Program memeriksa apakah login berhasil. Namun apabila tidak berhasil, program kembali ke login() dan proses ini berulang hingga login berhasil.

3. Apabila login berhasil, program akan memeriksa status akun.

4. Apabila status akun adalah admin, pengguna memasukkan pilihan 1-5. Pilihan diperiksa secara berurutan: 1 untuk tambah     antrean(), 2 untuk lihat antrean(), 3 untuk ubah data(), 4 untuk hapus antrean(), dan 5 untuk keluar. Setelah salah satu     fungsi selesai dijalankan, program kembali ke input pilihan 1-5.

5. Apabila pilihan admin bukan 1-5, program menampilkan "menu tidak tersedia" dan kembali ke input pilihan 1-5. Apabila pilihan adalah 5, progarm menampilkan pesan selesai dan berhenti.

6. Apabila status akun bukan admin (user), pengguna memasukkan pilihan 1-2, sedangkan pilihan 2 menampilkan pesan selesai dan program berhenti.

7. Apabila pilihan user bukan 1 atau 2, program menampilkan "menu tidak tersedia" dan kembali ke input pilihan 1-2

# Dokumentasi Program dan Ouput

# 1. Login

   <img width="981" height="465" alt="Screenshot 2026-10-06 202424" src="https://github.com/user-attachments/assets/81142f7d-bf69-4d63-a716-a7c5580a60a8" />

# Output Login Berhasil

<img width="700" height="595" alt="Screenshot 2026-10-06 202633" src="https://github.com/user-attachments/assets/aed82699-7da8-470e-8852-74969a5e1847" />

# Output Login Gagal

<img width="879" height="303" alt="Screenshot 2026-10-06 202837" src="https://github.com/user-attachments/assets/b2b409c5-8bf0-4efd-81d4-357d7cb35f9a" />
Penjelasan: Fungsi login meminta pengguna memasukkan username dan password. Password diinput menggunakan pwinput sehingga tidak terlihat pada layar. Program kemudian memeriksa apakah username terdapat pada user dan password yang dimasukkan sesuai. Apabila tidak sesuai, fungsi mengembalikan None, sehingga menu_utama() memanggil kembali login() melalui while status == None.

# 2. Menu Utama

   <img width="1492" height="548" alt="Screenshot 2026-10-06 203630" src="https://github.com/user-attachments/assets/91ff504b-906b-48cb-a201-bab0480fb0e3" />

# Output Menu Admin
<img width="1603" height="549" alt="Screenshot 2026-10-06 203823" src="https://github.com/user-attachments/assets/3b512b56-39f2-459b-a094-0df3dcc19cdc" />

 # Output Menu User  
 <img width="1012" height="527" alt="Screenshot 2026-10-06 203908" src="https://github.com/user-attachments/assets/02a51edc-a1be-4f13-907e-5247783be83f" />

Penjelasan: Setelah login berhasil, fungsi menu_utama() masuk ke perulangan while True dan menampilkan menu sesuai status akun. Admin memperoleh 5 menu, sedangkan user memperoleh 2 menu hanya untuk melihat antrean dan keluar program. Perulangan ini berlangsung terus hingga pengguna memilih keluar.

# 3. Tambah Antrean

   <img width="1492" height="731" alt="Screenshot 2026-10-06 204728" src="https://github.com/user-attachments/assets/5a061801-4e94-43f7-8ba3-e08cd72bbf1d" />

# Output Tambah Antrean Berhasil
<img width="1382" height="561" alt="Screenshot 2026-10-06 205203" src="https://github.com/user-attachments/assets/c6aeb9b2-4d6e-48ce-9ab2-b2274561d811" />

# Output Plat Kosong atau Sudah Terdaftar
<img width="1600" height="509" alt="image" src="https://github.com/user-attachments/assets/4edde7b1-6ef6-4e24-aee4-153832d33cfb" />

Penjelasan: Admin memasukkan plat nomor, nama pemilik, jenis motor, dan jenis cucian. Sebelum data disimpan, program melakukan validasi, yaitu plat motor tidak boleh kosong dan tidak boleh sama dengan plat yang sudah ada pada antrean. Apabila validasi terpenuhi, data disimpan dengan plat motor sebagai key.

# 4. Lihat Antrean (Admin dan User)
   <img width="1588" height="386" alt="Screenshot 2026-10-06 210249" src="https://github.com/user-attachments/assets/e33ea7ff-c972-45db-b7f2-bb5ff6c80535" />

# Output Lihat Antrean
<img width="1573" height="687" alt="Screenshot 2026-10-06 210436" src="https://github.com/user-attachments/assets/68c2aed6-67bb-41a7-93d7-c4b77be83400" />

Penjelasan: Apabila terdapat data, program menampilkannya dalam bentuk tabel menggunakan PrettyTabel agar lebih rapi dan mudah dibaca.

# 5. Ubah Data Antrean (Admin)
   <img width="1559" height="662" alt="Screenshot 2026-10-06 212140" src="https://github.com/user-attachments/assets/4883f11c-55a7-47e4-8093-09f81f5888cf" />

# Output Ubah Data Berhasil
<img width="1322" height="483" alt="Screenshot 2026-10-06 212027" src="https://github.com/user-attachments/assets/a788ef67-5c8e-44f0-a079-64ddb12b1a76" />

Penjelasan: Admin memasukkan plat nomor yang datanya ingin diubah. Apabila plat ditemukan pada Antrean, program meminta data lama diganti dengan data tersebut. Apabila plat tidak ditemukan, program menampilkan kesalahan.


# 6. Hapus Antrean (Admin)
   <img width="1023" height="325" alt="Screenshot 2026-10-06 213019" src="https://github.com/user-attachments/assets/fe82ff3c-74c0-4ebc-a446-9d309ca23731" />

# Output Hapus Antrean Berhasil
<img width="909" height="496" alt="Screenshot 2026-10-06 213444" src="https://github.com/user-attachments/assets/48bc074e-930e-43ed-ad75-0a8f532d3fbd" />

# Output Plat Tidak ditemukan
<img width="1101" height="438" alt="Screenshot 2026-10-06 213523" src="https://github.com/user-attachments/assets/eb029814-a57b-4858-abeb-4d9b3f3d3f66" />

Penjelasan: Admin memasukkan plat motor yang ingin dihapus. Apabila plat terdapat pada Antrean, data tersebut dihapus menggunakan perintah del. Apabila tidak terdapat, program menampilkan pesan "plat motor tidak ditemukan".

# 7. Keluar Program

# Output Keluar Program
   <img width="1062" height="409" alt="Screenshot 2026-10-06 214518" src="https://github.com/user-attachments/assets/01e60903-8317-4fbd-877b-d32f83c15431" />

Penjelasa: Apabila pengguna memilih keluar program, maka program menampilkan pesan terimakasih dan perulangan dihentikan menngunakan break. 


 # Penerapan Nilai Tambah

 1. Password tersembunyi menggunakan pwinput. Password yang diketik tidak terlihat jelas pada layar sehingga lebih aman dari pihak yang melihat layar pengguna

 2. Tampilan tabel menggunakan PrettyTabel. Daftar antrean ditampilkan dalam bentuk tebel sehingga lebih rapi dan lebih  mudah dibaca dibandingkan menggunakan print biasa.

 3. Penggunaan modul os dan time. modul os digunakan untuk membersihkan layar terminal, sedangkan time.sleep digunakan untuk memberi jeda agar pesan dapat terbaca oleh pengguna.

Selain itu, program ini juga memiliki fitur tambahan seperti:

a. Pembagian hak akses admin dan user. Menu yang di tampilakan berbeda sesuai staus akun, sehingga user tidak dapat menambahkan, mengubah, maupun menghapus data antrean.

b. Pemeriksaan input menggunakan percabangan if. Plat motor tidak boleh kosong dan tidak boleh sama dengan data yang sudah ada. Program juga memeriksa keberadaan plat motor ketika proses ubah dan hapus data.
