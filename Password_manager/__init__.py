# learning:-

# Description:- You have to kind of organize or store the password so we will store all the password along with the username
# or the account they are associated with along with the text file
# We are not going to store password as plane text we will encrypt the password
# This is just for the fun purpose
from cryptography.fernet import Fernet
'''
def write_key():
    key= Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
write_key()
'''
def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)
print(key, fer , 'i m master_pwd debugger')
def view():
    with open('Password_manager\password.txt','r') as f:
        for line in f.readlines():
            print(line, "step-1 view debug")
            data = (line.rstrip())
            # print(data,'step-2 data debug')
            user,passw = data.split('|')
            # print(user,passw, 'i m  from view')
            print('user: ',user,' | password : ',fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name : ")
    pwd = input( "Password : ")
    print(name, pwd , ' i m from add to debug before')
    with open('Password_manager\password.txt','a') as f:
        f.write(name+'|' +str(fer.encrypt(pwd.encode()).decode())
 + "\n")
        print(name, pwd , ' i m from add to debug')

while True:
    mode = input(
        "Would you like to add a new password? or view existing one? type (view or add ), press q to quit ").lower()
    if mode=='q':
        break

    if mode =="view":
        view()

    elif mode=='add':
        add()

    else:
        print('invalid mode.')
        continue
