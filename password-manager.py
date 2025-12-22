from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() #encode: takes the string and converts it to bytes
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f: # r: read existing file exist
        for line in f.readlines():
            data = line.rstrip() # strip() removes extra new lines
            user, passw = data.split('|')
            print('User:', user, '| Password:', fer.decrypt(passw.encode()).decode()) # decode(): converts bytes back to string
    
def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    with open('passwords.txt', 'a') as f: # a: add to the end of existing file or create new file if it does not exist
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n') 

while True:
    mode = input('Would you like to add a new password or view existing ones (view/add) or q to quit? ').lower()

    if mode =='q':
        break

    elif mode == 'view':
        view()

    elif mode == 'add':
        add()
        
    else:
        print('Invalid mode.')
        continue 