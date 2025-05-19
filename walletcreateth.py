## Creating an ETH wallet (and layer 2) that can be used with Metamask-type clients.

import hashlib
from eth_account import Account
import os
import platform

def clear_screen():
    '''Pulisce lo schermo in modo compatibile con Windows e Unix'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

x = input("Secure generation of an ETH wallet. Press enter to begin")

clear_screen()

insert1 = input("USER 1 type a random string and annotate, then press enter:")

clear_screen()

insert2 = input("USER 2 type a random string and annotate, then press enter:")

clear_screen()

insert = insert1 + insert2

# Creazione private key
def priv_key1():
    b = hashlib.sha256(insert.encode())
    prvk1 = "0x" + b.hexdigest()
    print('Private key parte 1:  ' + prvk1[:33])
    
def priv_key2():
    k = hashlib.sha256(insert.encode())
    prvk2 = "0x" + k.hexdigest()
    print('Private key parte 2:  ' + prvk2[33:])
    
def address():
    p = hashlib.sha256(insert.encode())
    prvk = "0x" + p.hexdigest()
    wallet = Account.from_key(prvk)
    print("Address:", wallet.address)
    
    
ax = input("Switch the computer to User 1 and press enter")

clear_screen()

priv_key1()

print("")

bx = input("Write down the private key and press enter, then go to user 2")

clear_screen()

c = input("User 2, when ready press enter")

clear_screen()

priv_key2()

print("")

dx = input("Procedure finished, press enter to display the wallet address")

clear_screen()

address()

address()
