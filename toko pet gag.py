items1 = {"Nama": "MIMIC OCTOPUS", "Stok": 5, "Harga" : 10000}
items2 = {"Nama": "RACCON", "Stok": 1, "Harga" : 105000}
items3 = {"Nama": "RAINBOW DF", "Stok": 1, "Harga" : 300000}
items4 = {"Nama": "KITSUNE", "Stok": 1, "Harga" : 1000000}
items5 = {"Nama": "BUTTERFLY", "Stok": 14, "Harga" : 75000}

items = [items1,items2,items3,items4,items5]

def tambah_items ():
    Nama = input("Masukan Nama items :")
    Stok = int(input("Masukan Jumlah stok :"))
    Harga = int(input("Masukan Harga :"))
    items6 = {"Nama":Nama, "Stok": Stok, "Harga" : Harga}
    items.append(items6)
    for i in range (len(items)):
        print("Nama Items - ", i, ":", items[i]["Nama"],"Stok Items - ", i, ":", items[i]["Stok"],"Harga Items - ", i, ":", items[i]["Harga"])

def menu ():
    print("\n")
    print("===> Menu <===")
    print("1. Tambah Items ")
    print("2. liat Items")
    print("3. Keluar")
    pilih = input("pilih menu (1-3) : ")

    if pilih == "1":
        tambah_items()
        menu()

    elif pilih == "2" :
            for i in range (len(items)):
              print("Nama Items - ", i, ":", items[i]["Nama"],"Stok Items - ", i, ":", items[i]["Stok"],"Harga Items - ", i, ":", items[i]["Harga"])
            menu()

    elif pilih == "3" :
        print("Telah Keluar dari sistem.")

    else :
        print("pilihan tidak valid \n")
     
menu()