import json
import hashlib

def log():
    with open('user.json') as f:
         global login
         login = json.load(f)
    user = input('Enter username:\n')
    if user not in login:
        print('User not found!\nRetry?')
        retry = input('YES/NO (Y/N)')
        if retry in ['YES', 'yes', 'y', 'Y']:
            main()
        else:
            quit()
    else:
        pw = login[user]
        pw2 = input('Enter password:\n')
        pw3 = hashlib.md5(pw2.encode()).hexdigest()
        if pw3 != pw:
            print('Wrong password! Retry?')
            while True:
                retry = str(input('YES/NO (Y/N)\n'))
                if retry != '':
                    break
            if retry in ['YES', 'yes', 'y', 'Y']:
                main()
            elif retry in ['NO', 'no', 'n', 'N']:
                quit()
        else:
            print('Nice you\'re logged in! B)')
            input()


def register():
    with open('user.json') as f:
        global login
        login = json.load(f)
    user = input('Enter username:\n')
    if user in login:
        print('You are already registered.\n')
        main()
    pw = input('Enter password:\n')
    result = hashlib.md5(pw.encode())
    login[user] = result.hexdigest()
    save()
    print('You are now registered!')
    main()

def change():
    with open('user.json') as f:
        global login
        login = json.load(f)
    user = input('Enter username:\n')
    if user in login:
        old = input('Enter old password:\n')
        old = hashlib.md5((old.encode())).hexdigest()
        if old != login[user]:
            print('Wrong password!')
            main()
            return
        else:
            pw = input('Enter new password:\n')
            result = hashlib.md5(pw.encode())
            login[user] = result.hexdigest()
            save()
            print('Your password has been changed!')
    else:
        print('Name not found!\n')
        main()

def save():
    with open('user.json', '+w') as f:
        json.dump(login, f)

def main():
    print("What would you like to do?\n1. Login\n2. Register\n3. Change password\n4. Quit")
    c = int(input('\n\nYour choice: '))
    if c == 1:
        log()
    elif c == 2:
        register()
    elif c == 3:
        change()
    elif c == 4:
        quit()
    else:
        print('Wrong choice...Retry...')
        main()

main()
