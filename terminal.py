import os

def main():
    while True:
        print("\nTerminal dasturi:")
        print("1. ls")
        print("2. touch")
        print("3. mkdir")
        print("4. cd")
        print("5. mv")
        print("6. \\q")

        command = input("Tanlangan buyruqni kiriting: ")

        if command == 'ls':
            print(os.listdir())
        
        elif command == 'touch':
            filename = input("Fayl nomini kiriting: ")
            data = ""
            while True:
                line = input("Ma'lumotlarni yozing (to'xtatish uchun 'end' yozing): ")
                if line.lower() == 'end':
                    break
                data += line + '\n'
            with open(filename, 'w') as file:
                file.write(data)
            print(f"{filename} fayliga ma'lumotlar muvaffaqiyatli yozildi.")
        
        elif command == 'mkdir':
            foldername = input("Papka nomini kiriting: ")
            os.makedirs(foldername)
            print(f"{foldername} nomli papka yaratildi.")
        
        elif command == 'cd':
            foldername = input("Papka nomini kiriting (.. uchun '..' yozing): ")
            os.chdir(foldername)
            print(f"{os.getcwd()} papkasi ichida bo'lish uchun '{foldername}' papkasiga kirildi.")
        
        elif command == 'mv':
            filename = input("Fayl nomini kiriting: ")
            destination = input("Yuborish manzilini kiriting: ")
            os.rename(filename, destination)
            print(f"{filename} fayli {destination} ga muvaffaqiyatli ko'chirildi.")
        
        elif command == '\\q':
            print("Terminal dasturi yakunlandi.")
            break
        
        else:
            print("Noto'g'ri buyruq. Qaytadan urinib ko'ring.")

if __name__ == "__main__":
    main()
