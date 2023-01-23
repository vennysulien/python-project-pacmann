#buat Class Item
class Item:
    
     def __init__(self,nama_item,jumlah_item,harga_per_item):
        self.nama_item = nama_item
        self.jumlah_item = jumlah_item
        self.harga_per_item = harga_per_item
        
#buat Class Cashier
class Cashier():
    list_item = [];
    
    #buat Method add item untuk menambahkan data dari item yang didefine ke dalam list_item
    def add_item(self):
        nama_item = input("Masukkan nama item:")
        jumlah_item = input("Masukkan jumlah item:")
        harga_per_item = input("Masukkan harga per item:")
        new_item = Item(nama_item, jumlah_item, harga_per_item)
        self.list_item.append(new_item)
        self.show_selection()
     
    #buat Method delete item untuk menghapus item dari list_item
    def delete_item(self):
        input_item = input("Masukkan item yang ingin dihapus:")
        temp_item = None;
        for item in self.list_item:
            if item.nama_item == input_item:
                temp_item = item
                break
        if temp_item is not None:
            self.list_item.remove(item)
        self.show_selection()
    
    #buat Method reset transaksi untuk menghapus semua list_item
    def reset_transactions(self):
        self.list_item.clear()
        print("Semua item berhasil di delete!")
        self.show_selection()
    
    #buat Method check order untuk mengecek apakah customer melakukan kesalahan saat input
    def check_order(self):
        is_order_correct = False
        for item in self.list_item:
            if item.nama_item == '' or not item.jumlah_item.isnumeric() or not item.harga_per_item.isnumeric():
                is_order_correct = False
            else:
                is_order_correct = True
                
        if is_order_correct:
            print("Pemesanan Sudah Benar")
        else:
            print("Terdapat kesalahan input data")
        return is_order_correct
    
    #buat Method total belanja untuk menghitung total belanja yang harus dibayarkan
    def total_belanja(self):
        #define total_belanja = 0
        if self.check_order():
            total_belanja = 0
            #total semua belanja
            for item in self.list_item:
                total_belanja += int(item.jumlah_item) * int(item.harga_per_item)
            print('total belanja sebesar: Rp', total_belanja)
            self.total_belanja_after_diskon(total_belanja)
        else:
            self.show_selection()
     
    #buat Method total belanja after diskon untuk menghitung total belanja yang dibayar setelah diskon
    def total_belanja_after_diskon(self, total_belanja):
        diskon = 0
        if total_belanja > 200_000:
            diskon = 0.05
        elif total_belanja > 300_000:
            diskon = 0.08
        elif total_belanja > 500_000:
            diskon = 0.1
        else:
            diskon = 0
        total_belanja_after_diskon = total_belanja * (1 - diskon)
        print(f' Selamat anda mendapatkan diskon sebesar {diskon} Sehingga total belanja menjadi: {total_belanja_after_diskon}')
    
    #buat Method untuk menampilkan list_item yang dibeli
    def show_list(self):
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        for idx in range(len(self.list_item)):
            item = self.list_item[idx]
            print(f' | {idx + 1} | {item.nama_item} | {item.jumlah_item} | {item.harga_per_item} |')
    
     #buat Method untuk menampilkan pilihan proses yang akan dilakukan customer
    def show_selection(self):
        self.show_list()
        options = {'1': self.add_item, '2': self.total_belanja, '3': self.delete_item, '4': self.reset_transactions}
        input_option = input('Pilih opsi angka yang diinginkan (1:Add Item, 2: Hitung total harga, 3:Delete Item, 4:Reset Transaksi) : ')
        return options[input_option]()

#proses 
cashier_1 = Cashier()
cashier_1.show_selection()