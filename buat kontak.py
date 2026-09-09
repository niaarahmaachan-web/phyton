kontak = {}


def tambah_kontak():
    nama = input("Masukkan nama :")
    nomor = input("Masukkan nomor HP :")
    
    if nama in kontak:
        print("Kontak sudah ada: ")
    else:
        kontak[nomor] = "nomor"
        print("Kontak berhasil ditambahkan.")
        
        
def lihat_kontak():
    print("\n=== DAFTAR KONTAK ===")
    
    if not kontak:
        print("Belum ada kontak.")
        return
    
    for nama, nomor in kontak.items():
        print(f"Nama : {nama}")
        print(f"Nomor : {nomor}")
        print("-" * 25)
        
        
def update_kontak():
    nama = input("Masukkan nama kontak yang ingin diubah :")
    
    if nama in kontak:
        nomor_baru = input("Masukkan nomor HP baru: ")
        kontak[nama] = nomor_baru
        print("Kontak berhasil diubah.")
    else:
        print("Kontak tidak ditemukan.")
        
        
def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus :")
    
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus. ")
    else:
        print("Kontak berhasil dihapus.")
        
        
def main():
    while True:
        print("\n=== GROUP KONTAK HP ===")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Update Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_kontak()
        if pilihan == "2":
            lihat_kontak()
        if pilihan == "3":
            update_kontak()
        if pilihan == "4":
            hapus_kontak()
        if pilihan == "5":
            print("Program selesai. ")
            break
        else:
            print("Pilihan tidak valid!")
            
            
main()

            
            
            
            
             
    
        
        
