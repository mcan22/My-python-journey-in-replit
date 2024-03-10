# Kullanıcıdan bilgileri al
name = input("Adınız: ")
date_of_birth = input("Doğum Tarihiniz: ")
telephone_number = input("Telefon Numaranız: ")
email = input("E-posta Adresiniz: ")
address = input("Adresiniz: ")

# Bilgileri içeren dictionary oluştur
user_info = {
    "Name": name,
    "Date of Birth": date_of_birth,
    "Telephone Number": telephone_number,
    "Email": email,
    "Address": address
}

# Dictionary'yi satır satır print et
print("\nKullanıcı Bilgileri:")
for key, value in user_info.items():
    print(f"{key}: {value}")

