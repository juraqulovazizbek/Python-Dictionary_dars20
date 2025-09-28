def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\nPhonebook Menu")
        print("1: Kontakt qo‘shish")
        print("2: Barcha kontaktlarni chiqarish")
        print("3: Ism bo‘yicha telefon qidirish")
        print("0: Chiqish")
        
        choice = input("Tanlovingiz: ")
        
        if choice == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            phonebook[name] = phone
            print(f"{name} qo‘shildi.")
        
        elif choice == "2":
            if not phonebook:
                print("Telefon kitobi bo‘sh.")
            else:
                print("Barcha kontaktlar:")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")
        
        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print(f"{name} topilmadi.")
        
        elif choice == "0":
            print("Chiqish.")
            break
        
        else:
            print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")

my_phonebook = {}
phonebook_menu(my_phonebook)
