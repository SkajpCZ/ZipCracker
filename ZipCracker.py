import zipfile, os, time, random

count = 1
def extrac(zfile, password):
    global count
    try:
        zfile.extractall(f"Cracked/{folderCracked}", pwd=bytes(password, 'utf-8'))
        return password
    except:
        spaceafter = " "*18
        print(f" \033[4;31mCracking\033[0;91m ({count}) \033[1;90m> \033[1;37m{password[:16]}{spaceafter*3}", end='\r')
        count += 1
        return

def rockyou():
    global dpfile
    passlistlenght = len(open('utf8-rockyou.txt', 'r', encoding='utf-8').readlines())
    passlistlenght = ('{:,}'.format(passlistlenght))
    zfile = zipfile.ZipFile(dpfile)
    passFile = open('utf8-rockyou.txt', 'r', encoding='utf-8')
    print()
    # print(f"\n\033[1;96m Passwords \033[1;90m> \033[1;37m{passlistlenght}\n\n")

    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extrac(zfile, password)
        if guess:
            spaceafter = " "*18
            print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
            # input('\n\n\n\033[1;37m Press \033[1;93m[ Enter ]\033[1;37m to exit')
            break

def rand_digits():
    global dpfile
    zfile = zipfile.ZipFile(dpfile)
    passFile = open('utf8-rockyou.txt', 'r', encoding='utf-8')
    print()
    for line in passFile.readlines():
        chars1 = "1234567890"
        password = ''.join((random.choice(chars1) for i in range(random.randint(2, 16))))
        # password = line.strip('\n')
        guess = extrac(zfile, password)
        if guess:
            spaceafter = " "*18
            print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
            break

def every_rand():
    global dpfile
    zfile = zipfile.ZipFile(dpfile)
    passFile = open('utf8-rockyou.txt', 'r', encoding='utf-8')
    print()
    for line in passFile.readlines():
        chars1 = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!._-*,"
        randsom = ''.join((random.choice(chars1) for i in range(random.randint(2, 16))))
        chars2 = "1234567890"
        num = ''.join((random.choice(chars2) for i in range(random.randint(2, 16))))
        rockpass = line.strip('\n')
        password = random.choice((randsom, rockpass, rockpass, rockpass, rockpass, rockpass, rockpass, randsom, randsom, num, num, randsom))
        guess = extrac(zfile, password)
        if guess:
            spaceafter = " "*18
            print(f" \033[4;32mCracked\033[0;92m ({count}) \033[1;90m> \033[1;37m{password}{spaceafter*3}\n\n", end='\r')
            break



def MainMenu():
    cho = input("\033[1;93m Option \033[1;90m> \033[1;37m").lower()
    if cho == 'rockyou' or cho == '1':
        rockyou()
        MainMenu()
    if cho == 'digits' or cho == '2':
        rand_digits()
        MainMenu()
    if cho == 'random' or cho == '3':
        every_rand()
        MainMenu()
    else:
        print("\n\033[1;91m Uknown options\n")
        MainMenu()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print(f"""\033[1;36m
     _____   _       ______                __            
    /__  /  (_)___  / ____/________ ______/ /_____  _____
      / /  / / __ \/ /   / ___/ __ `/ ___/ //_/ _ \/ ___/
     / /__/ / /_/ / /___/ /  / /_/ / /__/ ,< /  __/ /    
    /____/_/ .___/\____/_/   \__,_/\___/_/|_|\___/_/     
          /_/                                       \033[1;37mby \033[1;90mSkajp
                                                    \033[1;37mVersion: \033[1;90m1
""")

FoundRockYou = True if os.path.exists("utf8-rockyou.txt") else False
if FoundRockYou == False:
    print('\033[1;32m' + "\n Downloading" + '\033[0;90m' + " > " + '\033[0;37m' + f"rockyou.txt  (modified to work with this script)  \n")
    if os.name == 'nt':
        os.system("curl -s https://raw.githubusercontent.com/SkajpCZ/Rockyou.txtUTF-8/main/utf8-rockyou.zip -o ./utf8-rockyou.zip && tar -xf utf8-rockyou.zip")
        os.system("del /F /S /Q utf8-rockyou.zip >nul")
    else:
        os.system("curl -s https://raw.githubusercontent.com/SkajpCZ/Rockyou.txtUTF-8/main/utf8-rockyou.zip -o ./utf8-rockyou.zip && unzip utf8-rockyou.zip")
        os.system("rm utf8-rockyou.zip")
dpfile = input(f'\033[1;93m Drag your zip file here \033[1;90m> \033[1;37m')
folderCracked = dpfile.strip('"').split('\\')
folderCracked.reverse()
folderCracked = folderCracked[0]
dpfile = dpfile.replace('\\', '/').strip('"')


print("\n\n\033[1;36m Passwords Lists\033[1;90m:")
print("\033[1;93m    1)\033[1;37m Rockyou")
print("\033[1;93m    2)\033[1;37m Digits (Max 16 lenght)")
print("\033[1;93m    3)\033[1;37m Random (Mix of everything - 60% Rock you / 25% Random words / 15% Random digits)\n\n")
MainMenu()
