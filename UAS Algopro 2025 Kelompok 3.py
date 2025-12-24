# UAS PROYEK – ALGORITMA PEMROGRAMAN 2025 #
# SISTEM PENJUALAN HARIAN #

data_penjualan = []

def menambah_data_penjualan():
    # Fungsi untuk menambah data penjualan #
    print ("\n=== SILAHKAN TAMBAHKAN DATA ===")
    nama_barang = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah terjual: "))
    harga = int(input("Masukkan harga satuan: "))

    total = jumlah * harga

    penjualan = {
        "nama_barang": nama_barang,
        "jumlah": jumlah,
        "harga": harga,
        "total": total
    }

    data_penjualan.append(penjualan)
    print("\n===BERHASIL MENAMBAHKAN DATA===")


def melihat_data_penjualan():
    # Fungsi untuk melihat data penjualan #
    if len(data_penjualan) == 0:
        print("❌ Belum ada data penjualan.")
    else:
        print("\n--- DATA PENJUALAN ---")
        for i, p in enumerate(data_penjualan, start=1):
            print(f"{i}. {p['nama_barang']} | Jumlah: {p['jumlah']} | "
                f"Harga: {p['harga']} | Total: {p['total']}")
            
        # Bubble_sorting #
        print("\n===Sorting Data Penjualan===")
        pilihan = input("Apakah Anda ingin Mengsorting Data Terbesar Sampai Terkecil? (y/n): ")
        if pilihan == 'y':
            n = len(data_penjualan)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if data_penjualan[j]["total"] < data_penjualan[j + 1]["total"]:
                        data_penjualan[j], data_penjualan[j + 1] = data_penjualan[j + 1], data_penjualan[j]

            print("\n🔄 Data berhasil diurutkan berdasarkan total penjualan terbesar ke terkecil.")


def menghitung_total_pendapatan(index=0):
    # Fungsi untuk menghitung total pendapatan #
    if index == len(data_penjualan):
        return 0
    return data_penjualan[index]["total"] + menghitung_total_pendapatan(index + 1)



# MENU SISTEM PENJUALAN HARIAN #
while True:
    print("\n=== SISTEM DATA PENJUALAN HARIAN ===")
    print("1. Tambah Data Penjualan")
    print("2. Lihat Data Penjualan")
    print("3. Hitung Total Pendapatan")
    print("4. Info Pembuat")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        menambah_data_penjualan()
        
    elif pilihan == "2":
        melihat_data_penjualan()

    elif pilihan == "3":
        menghitung_total_pendapatan()
        print(f"\n 💵 Total Pendapatan Hari Ini: Rp {menghitung_total_pendapatan()}")

    elif pilihan == "4":
        print("\n=== 🥰 KELOMPOK 3 😘 ===")
        print("1. Naufal Zaidan Zidna NPM 625C004")
        print("2. Iqbal Nur Rizki NPM 625C002")
        print("3. Aghnia khoirunnisa NPM 625C0011")
        print("4. Mohammad Rizal Fahmi NPM 625C0015")

    elif pilihan == "5":
        print("\n=== Terima Kasih Telah Menggunakan Sistem Ini ===")
        break