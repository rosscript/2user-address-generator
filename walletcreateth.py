## Comando Carabinieri Antifalsificazione Monetaria - Sezione Criptovalute
## Creazione di un wallet ETH (e layer 2) utilizzabile con client tipo Metamask

import hashlib
from eth_account import Account
import os

x = input("Comando Carabinieri Antifalsificazione Monetaria - Sezione Criptovalute. Generazione sicura di un wallet ETH. Premere invio per iniziare")

os.system('clear')

insert1 = input("UTENTE 1 digitare una stringa casuale e annotare, poi premere invio: ")

os.system('clear')

insert2 = input("UTENTE 2 digitare una stringa casuale e annotare, poi premere invio: ")

os.system('clear')

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
    
    
ax = input("Passare il computer all'Utente 1 e premere invio")

os.system('clear')

priv_key1()

print("")

bx = input("Annotare la private key e premere invio, poi passare all'utente 2")

os.system('clear')

c = input("Utente 2, quando pronto premere invio")

os.system('clear')

priv_key2()

print("")

dx = input("Procedura terminata, premere invio per visualizzare l'address del wallet")

os.system('clear')

address()

address()
