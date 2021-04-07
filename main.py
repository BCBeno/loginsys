import json
import hashlib
import bcrypt
import sqlite3

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
        pw = pw.encode('utf-8')
        if bcrypt.checkpw(pw2.encode('utf-8'), pw) == 0:
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
    result = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    result = result.decode('utf-8')
    login[user] = result
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
        if bcrypt.checkpw(old.encode('utf-8'), login[user].encode('utf-8')) == 0:
            print('Wrong password!')
            main()
            return
        else:
            pw = input('Enter new password:\n')
            result = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
            result = result.decode('utf-8')
            login[user] = result
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
