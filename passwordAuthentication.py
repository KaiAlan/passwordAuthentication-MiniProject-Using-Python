from cryptography.fernet import  Fernet
import getpass

# def write_key():
#     key = Fernet.generate_key()
#     with open('passAuthKey.key','wb') as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    with open('passAuthKey.key','rb') as f:
        key = f.read()
    return key


key = load_key()
fer = Fernet(key)

# To add and view the database------------------------------------------------------

def add():
    user = input('User: ')
    pwd = input('Password: ')
    
    with open('passwordAuth.txt','a') as f:
        f.write(user+'|'+fer.encrypt(pwd.encode()).decode()+'\n')

def view():
    with open('passwordAuth.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split('|')
            print('User: '+ user +'| Password: '+ fer.decrypt(passwd.encode()).decode())



while True:
    
    choice = input('Would you wanna add a new Password or view the existing one(add/view/quit): ').lower()
    
    if choice == 'quit':
        break
    elif choice == 'add':
        add()
    elif choice == 'view':
        view()
    else:
        print('Wrong choice! Try Again -_-')

# -----------------------------------------------------------------------------------

# name = input("Enter UserName: ")
# passwd=getpass.getpass("Enter Password: ")
# with open('passwordAuth.txt','r') as f:
#     for line in f.readlines():
#         data = line.rstrip()
#         user, passwrd = data.split('|')
#         if(user == name):
#             if(fer.decrypt(passwrd.encode()).decode() == passwd):
#                 print('Correct Password :)')
#                 quit()
#             else:
#                 print("Wrong Password -_-")
#                 quit()
        
#     print('Wrong Username Try Again :(')