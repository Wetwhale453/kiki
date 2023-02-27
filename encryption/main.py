from key import *
# if you do not have this file, kill yourself

file = fileGet()

while True:
    try:
        with open(file) as file:
            raw = file.read()
            encrypt(raw)
            print('success. check your directory for the "encrypted.txt" file')
            break
    except:
        print("there was an error loading the file, double check the directory and try again")
