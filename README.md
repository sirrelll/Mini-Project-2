# Mini-Project-2
Nama : Darel Prasetya Fawwaz, NIM : 2409116064, Nama Tugas : Mini Project 2
Tema : Sistem Reservasi Restoran

========Flowchart(https://drive.google.com/file/d/1lmIHDax062-FHEZ0A83h4NE2MNKTE41Y/view?usp=sharing)=========
![Mini Project 2 drawio (1)](https://github.com/user-attachments/assets/5f2d08d4-b153-4a05-a5b7-af87ee910095)
Diawali dengan tombol start, kemudian muncul simbol decision yang memiliki 3 pilihan, jika memilih 1 maka akan masuk ke proses Admin ,jika memilih 2 maka akan masuk ke proses Pembeli, jika memilih 3 maka akan keluar atau end.

Untuk pilihan 1 akan muncul login admin dan setelah kita masukkan user dan password admin maka akan dapat akses ke menu admin yang dimana menu admin terdapat beberapa pilihan yaitu:
1. Tambah Menu -> Berfungsi untuk Menambahkan Menu serta Harga dengan cara Memasukkan Nama dan Harga menu setelah di input maka penambahan menu telah berhasil.
2. Lihat Menu -> Berfungsi untuk Menampilkan Menu.
3. Ubah Menu -> Berfungsi untuk mengubah menu yang telah ditambah dengan cara memasukkan nama dan harga menu yang baru setelah itu pengubahan menu telah berhasil.
4. Hapus Menu -> Berfungsi untuk menghapus menu yang sudah ada dengan cara menginput nama menu yang ingin dihapus.
5. Kembali -> Mengembalikan ke simbol decision awal.

Untuk pilihan 2 akan muncul simbol decision yang dimana jika memilih 1 akan masuk ke proses login dan jika belum memiliki akun akan diulang dan memilih pilihan 2 yaitu untuk registrasi, dan pilihan 3 itu kembali maka akan dikembalikan ke menu sebelumnya, 
Setelah registrasi dengan memasukkan nama serta sandi maka registarsi telah berhasil kemudian dikembalikan ke simbol decision untuk melakukan proses login, dengan memasukkan nama dan sandi yang sama seperti registrasi anda telah berhasil login. Setelah login maka akan muncul Menu Pembeli didalam menu tersebut terdapat simbol decision yang memberikan pilihan yaitu:
1. Lihat Menu -> Berfungsi untuk Menampilkan Menu.
2. Lihat Meja -> Berfungsi untuk Menampilkan Status dari meja apakah tersedia atau tidak.
3. Pesan Menu -> Berfungsi untuk memesan menu yang tersedia dengan cara Memilih menu yang ada serta jumlah dan pilih nomor meja yang diinginkan untuk reservasi.
4. Lihat Transaksi -> Berfungsi untuk Menampilkan transaksi yang sudah lakukan oleh pembeli.
5. Kembali -> Mengembalikan ke Menu Awal
Jika sudah melakukan pemesanan maka jika ingin keluar atau end pembeli bisa memilih opsi kembali yang akan menghubungkan ke end

============Output==============
**Role Admin**
![Screenshot 2024-10-14 204554](https://github.com/user-attachments/assets/ee3ab7ff-8390-4315-b687-b7a69120bbfc)
![Screenshot 2024-10-14 204637](https://github.com/user-attachments/assets/cfe518a4-7344-4864-9dbe-a12511b539ee)
**Role Pembeli**
![Screenshot 2024-10-14 205226](https://github.com/user-attachments/assets/2fd529c0-5b76-403f-9874-6b4a8a20ad4d)
![Screenshot 2024-10-14 205238](https://github.com/user-attachments/assets/63ccac5d-0d58-4635-bb48-32638b91eaf4)
![Screenshot 2024-10-14 205250](https://github.com/user-attachments/assets/c4f7af23-69f7-48ef-a3fe-65fd2cfef1e5)

==========Baris Code===========
Baris 36-37 berfungsi untuk memanggil prettytable serta membuat tabel yang mudah dibaca, kemudian untuk datetime berfungsi untuk memanggil tanggal dan waktu.
from prettytable import PrettyTable
from datetime import datetime

Baris 40-44 yaitu berfungsi untuk menyimpan data data yang telah diinputkan contohnya menambahkan menu yang baru ditambah maka data itu ada tersimpan disini begitu juga dengan bayar seta pembeli, dan untuk meja disini terdapat 5 meja karena "in range(1,6) jadi untuk menyimpan status dari ke 5 meja tersebut apakah kosong atau sudah dipesan.
# menyimpan data
menu = []
bayar = []
meja = [{'id': i, 'status': 'kosong'} for i in range(1, 6)]
pembeli = []

Baris 48-49 merupakan cara login admin untuk mengakses role admin dengan menggunakan id dan password yang telah disiapkan.
# login untuk admin
id_admin = "admin"
pw_admin = "admin123"

Baris 53-56 merupakan fungsi role admin untuk menambahkan menu, seperti "id_menu = len(menu) + 1" itu ibaratkan nomor contoh menambahkan menu ayam maka akan dianggap sebagai no 1 atau id 1 begitu juga seterusnya, untuk "menu.append" untuk menambahkan menu baru kedalam yang berisi id, menu, dan harga.
# fungsi role admin
def tambah_menu(nama, harga):
    id_menu = len(menu) + 1
    menu.append({"id": id_menu, "menu": nama, "harga": harga})
    print(f"===menu '{nama}' telah ditambahkan.===")

Baris 59-66 merupakan fungsi role admin untuk melihat menu, disini menampilkan menu menggunakan prettytable dan jika menu belum ada maka akan muncul "else"
def lihat_menu():
    if menu:
        tabel = PrettyTable(['Nomor', 'Menu', 'Harga'])
        for item in menu:
            tabel.add_row([item['id'], item['menu'], item['harga']])
        print(tabel)
    else:
        print("menu tidak ada silahkan ditambah dulu.")

Baris 69-76 merupakan fungsi role admin untuk mengubah menu, fungsi ini menggunakan loop jika memasukkan nomor atau id dari menu yang telah ada maka akan diminta untuk mengubah nama serta harga yang ada didalam menu tersebut.
def ubah_menu(id_menu, nama, harga):
    for item in menu:
        if item['id'] == id_menu:
            item['menu'] = nama
            item['harga'] = harga
            print(f"menu {id_menu} telah berhasil diubah.")
            return
    print(f"menu {id_menu} tidak ada.")

Baris 79-84 merupakan fungsi role admin untuk menghapus menu, fungsi ini juga menggunakan loop jika kita memasukkan nomor atau id dari menu yang telah ada maka menu tersebut akan dihapus menggunakan "menu.remove(item)"
def hapus_menu(id_menu):
    for item in menu:
        if item['id'] == id_menu:
            menu.remove(item)
        break
    print(f"menu {id_menu} telah dihapus.")

Baris 88-92 merupakan fungsi role pembeli untuk melihat meja yang tersedia, 
# fungsi role pembeli
def lihat_meja():
    tabel = PrettyTable(['No Meja', 'Status Meja'])
    for m in meja:
        tabel.add_row([m['id'], m['status']])
    print(tabel)

def pesan_meja(id_meja):
    status_meja = None
    for m in meja:
        if m['id'] == id_meja:
            status_meja = m['status']
            break  
    if status_meja is None: # meja tidak ditemukan
        print(f"===meja No {id_meja} tidak ditemukan===")
        return False
    if status_meja == 'kosong': # meja kosong
        m['status'] = 'dipesan' # meja dipesan
        print(f"===meja {id_meja} berhasil dipesan===")
        return True
    print(f"===meja {id_meja} sudah dipesan===")
    return False

def bayar_pesanan(id_menu, jumlah, nama, id_meja):
    if pesan_meja(id_meja):
        for item in menu:
            if item['id'] == id_menu:
                total = item['harga'] * jumlah
                tanggal = datetime.now().strftime("%Y-%m-%d")
                bayar.append({
                    "menu": item['menu'], "jumlah": jumlah, "total": total,
                    "nama": nama, "meja": id_meja, "tanggal": tanggal,
                })
                tabel = PrettyTable(['Nama', 'Nomor Meja', 'Menu', 'Jumlah', 'Tanggal', 'Total'])
                tabel.add_row([nama, id_meja, item['menu'], jumlah, tanggal, total])
                print(tabel)
                return
        print(f"===menu {id_menu} tidak ditemukan===")
    else:
        print("===meja tidak ada, transaksi dibatalkan===")

def lihat_transaksi():
    if bayar:
        tabel = PrettyTable(['Nama', 'Meja', 'Menu', 'Jumlah','Tanggal', 'Total'])
        for t in bayar:
            tabel.add_row([t['nama'], t['meja'], t['menu'], t['jumlah'], t['tanggal'], t['total']])
        print(tabel)
    else:
        print("===belum ada transaksi===")

# Fungsi register dan login pembeli
def register(username, password):
    for akun in pembeli:
        if akun['username'] == username:
            print("===username sudah ada===")
            return  
    pembeli.append({'username': username, 'password': password})
    print(f"===registrasi telah berhasil {username}===")

def login(username, password):
    for akun in pembeli:
        if akun['username'] == username and akun['password'] == password:
            print(f"===login berhasil {username}===")
            return True
    print("===login gagal, silahkan coba lagi===")
    return False

# Menu utama
def main():
    while True:
        print("\n===Reservasi Restoran====")
        print("1. Admin")
        print("2. Pembeli")
        print("3. Keluar")
        print("===========================")

        pilihan = input("Pilihlah opsi: ")

        if pilihan == '1':
            username = input("Masukkan username admin: ")
            password = input("Masukkan password admin: ")
            if username == id_admin and password == pw_admin:
                while True:
                    print("\n===Menu Admin===")
                    print("1. Tambah Menu")
                    print("2. Lihat Menu")
                    print("3. Ubah Menu")
                    print("4. Hapus Menu")
                    print("5. Kembali")
                    print("==================")

                    pilihan_admin = input("Pilih opsi: ")

                    if pilihan_admin == '1':
                        nama = input("Nama menu: ")
                        harga = float(input("Harga menu: "))
                        tambah_menu(nama, harga)
                    elif pilihan_admin == '2':
                        lihat_menu()
                    elif pilihan_admin == '3':
                        id_menu = int(input("No menu: "))
                        nama = input("Nama baru: ")
                        harga = float(input("Harga baru: "))
                        ubah_menu(id_menu, nama, harga)
                    elif pilihan_admin == '4':
                        id_menu = int(input("No menu: "))
                        hapus_menu(id_menu)
                    elif pilihan_admin == '5':
                        break
                    
        elif pilihan == '2':
            while True:
                print("\n===Menu===")
                print("1. Login")
                print("2. Registrasi")
                print("3. Kembali")
                print("====================")

                pilihan_pembeli = input("Pilih opsi: ")

                if pilihan_pembeli == '1':
                    username = input("Username: ")
                    password = input("Password: ")
                    if login(username, password):
                        print("login anda berhasil!")
                        while True:
                            print("\n===Menu Pembeli===")
                            print("1. Lihat Menu")
                            print("2. Lihat Meja")
                            print("3. Pesan Menu")
                            print("4. Lihat Transaksi")
                            print("5. Kembali")
                            print("====================")

                            pilihan_transaksi = input("Pilih opsi: ")

                            if pilihan_transaksi == '1':
                                lihat_menu()
                            elif pilihan_transaksi == '2':
                                lihat_meja()
                            elif pilihan_transaksi == '3':
                                id_menu = int(input("No menu: "))
                                jumlah = int(input("Jumlah: "))
                                id_meja = int(input("No meja: "))
                                bayar_pesanan(id_menu, jumlah, username, id_meja)
                            elif pilihan_transaksi == '4':
                                lihat_transaksi()
                            elif pilihan_transaksi == '5':
                                break
                            
                elif pilihan_pembeli == '2':
                    username = input("Username: ")
                    password = input("Password: ")
                    register(username, password)
                    print("register berhasil, silahkan login")

                elif pilihan_pembeli == '3':
                    break

        elif pilihan == '3':
            print("terima kasih")
            break

if __name__ == '__main__':
    main()
