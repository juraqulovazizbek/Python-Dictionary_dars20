kalit = input("kalit nomi: ")
password = {
    "email": "vali123",
    "github": "vali2022",
    "telegram": "4379312"
}

if kalit in password:
    print(password[kalit])
else:
    print("Topilmadi")