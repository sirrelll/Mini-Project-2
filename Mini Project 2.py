from prettytable import PrettyTable
from datetime import datetime

# menyimpan data
menu = []
bayar = []
meja = [{'id': i, 'status': 'kosong'} for i in range(1, 6)]
pembeli = []

# login untuk admin
id_admin = "admin"
pw_admin = "admin123"

# fungsi role admin
def tambah_menu(nama, harga):
    id_menu = len(menu) + 1
    menu.append({"id": id_menu, "menu": nama, "harga": harga})
    print(f"===menu '{nama}' telah ditambahkan.===")

def lihat_menu():
    if menu:
        tabel = PrettyTable(['Nomor', 'Menu', 'Harga'])
        for item in menu:
            tabel.add_row([item['id'], item['menu'], item['harga']])
        print(tabel)
    else:
        print("menu tidak ada silahkan ditambah dulu.")

def ubah_menu(id_menu, nama, harga):
    for item in menu:
        if item['id'] == id_menu:
            item['menu'] = nama
            item['harga'] = harga
            print(f"menu {id_menu} telah berhasil diubah.")
            return
    print(f"menu {id_menu} tidak ada.")

def hapus_menu(id_menu):
    for item in menu:
        if item['id'] == id_menu:
            menu.remove(item)
        break
    print(f"menu {id_menu} telah dihapus.")

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