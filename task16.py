kalit = input("kalit nomi: ")
password = {
    "email": "vali123",
    "github": "vali2022",
    "telegram": "4379312"
}

if kalit in password:
    password.pop(kalit)
    print(f"{kalit} o'chirildi.")
else:
    print("Bunday kalit yo'q")