import hashlib
import itertools
import shutil
import colorama
from colorama import Fore, Back, Style
colorama.init()

cols, rows = shutil.get_terminal_size()
print(Back.GREEN + "WELCOME::TO::THE::SIMPLE::HASH::GENERATOR".center(cols) + Style.RESET_ALL)

for i in itertools.count():
    print(Back.WHITE, Fore.BLACK + "THESE ARE THE HASHES I PROVIDE".center(cols) + Style.RESET_ALL)
    print("\n1.MD5\n2.SHA-256\n3.SHA-512\n4.SHA3-256\n5.SHA3-512\n")
    hash_choice = input("Please Enter Your Choice (1-5): ")
    user_string = input("Please Enter Your Text: ")


    def md5_generator(user_string):
        md5hash = hashlib.md5(user_string.encode('utf-8')).hexdigest()
       # print(Fore.RED + f"MD5: {md5hash}\n" + Style.RESET_ALL)
        print(f"MD5 HASH: ", Fore.RED + md5hash + Style.RESET_ALL)


    def sha256_generator(user_string):
        sha256hash = hashlib.sha256(user_string.encode('utf-8')).hexdigest()
        #print(Fore.RED + f"SHA256: {sha256hash}\n" + Style.RESET_ALL)
        print(f"SHA256 HASH: ", Fore.RED + sha256hash + Style.RESET_ALL)


    def sha512_generator(user_string):
        sha512_hash = hashlib.sha512(user_string.encode('utf-8')).hexdigest()
        #print(Fore.RED + f"SHA512: {sha512_hash}\n" + Style.RESET_ALL)
        print(f"SHA512 HASH: ", Fore.RED + sha512_hash + Style.RESET_ALL)

    def sha3_256_generator(user_string):
        sha3_256_hash = hashlib.sha3_256(user_string.encode('utf-8')).hexdigest()
        #print(Fore.RED + f"SHA3-256: {sha3_256_hash}\n" + Style.RESET_ALL)
        print(f"SHA3-256 HASH: ", Fore.RED + sha3_256_hash + Style.RESET_ALL)


    def sha3_512_generator(user_string):
        sha3_512_hash = hashlib.sha3_512(user_string.encode('utf-8')).hexdigest()
        #print(Fore.RED + f"SHA3-512: {sha3_512_hash}\n" + Style.RESET_ALL)
        print(f"SHA3-512 HASH: ", Fore.RED + sha3_512_hash + Style.RESET_ALL)


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

    input("\nPress ENTER to Generate Another Hash or Ctrl+C to Exit...\n")
