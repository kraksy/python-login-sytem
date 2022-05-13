from fileinput import filename
import getpass
import os
import random
import string

A = "a"
N = "n"
ADD = 'add'
man = True

file_name = '','.txt'.join(random.choice(string.ascii_lowercase) for i in range(6))

def prin(password, name):
    print("heslo - ", password)
    print("jmeno učtu - ", name)

def login():
    try:
        print(" == ted se prihlas == ")
        input1 = getpass.getpass("zadej svoje jmeno=   ")
        input2 = getpass.getpass("zadej svoje heslo=   ")
        print(" == uspesne prihlasen == ")
        prin()
    except:
        print("o oh nekde se stala chyba vypada to ze nemas ucet nebo si zapomnel informace")
        choice()

def choice():
    odp = input('chces si udelat new ucet nebo si zapomnel informace ( A , N , add) =  ')
    if odp == A:
        login()
    if odp == N:
        register()
    if odp == ADD:
        register()
     
def register():
    try:
        password = getpass.getpass("zadej heslo =   ")
        password2 = getpass.getpass("zadej znovu heslo =   ")
        name = getpass.getpass("zadej jmeno =   ")

        with open(file_name, "w") as f:
            mmm = f.writelines()
            nnn = f.write()

        if password == password2:
            print(" == yaay učet byl založen == ")
            login()
            man = False
    except:
        print("why")

choice()