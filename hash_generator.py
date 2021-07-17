import hashlib
import itertools
import shutil
import colorama
from colorama import Fore, Back, Style

colorama.init()

cols, rows = shutil.get_terminal_size()
print(Back.GREEN + "WELCOME::TO::THE::SIMPLE::HASH::GENERATOR".center(cols) + Style.RESET_ALL)

for i in itertools.count():
    file_or_str = input("\n1. String\n2. File \nPlease enter your choice (1-2): ")
    if file_or_str == '1':
        print(Back.WHITE, Fore.BLACK + "THESE ARE THE HASHES I PROVIDE".center(cols) + Style.RESET_ALL)
        print("\n1.MD5\n2.SHA-256\n3.SHA-512\n4.SHA3-256\n5.SHA3-512\n")
        hash_choice = input("Please Enter Your Choice (1-5): ")
        user_string = input("Please Enter Your Text: ")
    else:
        file_path = input(r"Please enter your file path: ")


    def md5_generator(user_string):
        md5hash = hashlib.md5(user_string.encode('utf-8')).hexdigest()
        print(f"MD5 HASH: ", Fore.RED + md5hash + Style.RESET_ALL)


    def sha256_generator(user_string):
        sha256hash = hashlib.sha256(user_string.encode('utf-8')).hexdigest()
        print(f"SHA256 HASH: ", Fore.RED + sha256hash + Style.RESET_ALL)


    def sha512_generator(user_string):
        sha512_hash = hashlib.sha512(user_string.encode('utf-8')).hexdigest()
        print(f"SHA512 HASH: ", Fore.RED + sha512_hash + Style.RESET_ALL)


    def sha3_256_generator(user_string):
        sha3_256_hash = hashlib.sha3_256(user_string.encode('utf-8')).hexdigest()
        print(f"SHA3-256 HASH: ", Fore.RED + sha3_256_hash + Style.RESET_ALL)


    def sha3_512_generator(user_string):
        sha3_512_hash = hashlib.sha3_512(user_string.encode('utf-8')).hexdigest()
        print(f"SHA3-512 HASH: ", Fore.RED + sha3_512_hash + Style.RESET_ALL)


    def file_hash(file_path):
        try:
            md5 = hashlib.md5()
            sha = hashlib.sha256()

            with open(file_path, 'rb') as f:
                chunk = 0
                while chunk != b'':
                    chunk = f.read(1024)
                    md5.update(chunk)
                    sha.update(chunk)
            print("MD5: ", Fore.RED + md5.hexdigest() + Style.RESET_ALL, "\nSHA: ",
                  Fore.RED + sha.hexdigest() + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "ERROR!: " + Style.RESET_ALL, str(e))


    if file_or_str == '1':
        if hash_choice == '1':
            md5_generator(user_string)
        elif hash_choice == '2':
            sha256_generator(user_string)
        elif hash_choice == '3':
            sha512_generator(user_string)
        elif hash_choice == '4':
            sha3_256_generator(user_string)
        elif hash_choice == '5':
            sha3_512_generator(user_string)
        else:
            print(Back.RED + "\nINVALID::CHOICE! Please Enter a Valid Choice (1-5)" + Style.RESET_ALL)
    elif file_or_str == '2':
        file_hash(file_path)
    else:
        print(Back.RED + "\nINVALID::CHOICE! Please Enter a Valid Choice (1-2)" + Style.RESET_ALL)

    input("\nPress ENTER to Generate Another Hash or Ctrl+C to Exit...\n")