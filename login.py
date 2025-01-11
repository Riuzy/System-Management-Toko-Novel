def login():
    print("SELAMAT DATANG")
    print("Silakan login terlebih dahulu")
    
    users = {
        "rizky": "kasir1",
        "alfan": "kasir2",
    }
    
    while True:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in users:
            if users[username] == password:
                print("\nLOGIN BERHASIL! Selamat datang, {}!".format(username.capitalize()))
                return True
            else:
                print("Password salah. Coba lagi.\n")
        else:
            print("Username tidak ditemukan. Coba lagi.\n")
