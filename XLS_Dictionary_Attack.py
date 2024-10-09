import msoffcrypto
import io

excel_file = "HR-confidential.xls" 
with open('common_passwords.txt', 'r', encoding='ISO-8859-1') as f:
    password_list = f.read().split()
decrypted = io.BytesIO()

with open(excel_file, "rb") as file:
    excel_open = msoffcrypto.OfficeFile(file)
    i = 0
    while i < len(password_list):
        password = password_list[i]
        try:
            excel_open.load_key(password=password)
            excel_open.decrypt(decrypted)
            print("Your password is: " + password)
            break
        except:
            print("Wrong Password: ", password)
            i += 1
            continue
