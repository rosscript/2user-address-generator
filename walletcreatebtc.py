## Creating a bitcoin wallet that can be used with Electrum-type clients.

## Importing the necessary libraries.
import hashlib, base58, ecdsa, os
import platform

def clear_screen():
    '''Pulisce lo schermo in modo compatibile con Windows e Unix'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#INIZIO FUNZIONI
def hash256(key):
    '''restituisce il doppio sha'''
    return hashlib.sha256(hashlib.sha256(key).digest()).digest()

def hash160(key):
    '''restituisce il ripemd160'''
    ripemd = hashlib.new('ripemd160')
    ripemd.update(hashlib.sha256(key).digest())
    return ripemd.digest()

def wif(key):
    '''restituisce chiave in formato wif'''
    sk_net = bytes.fromhex('80') +  key
    addr = sk_net + hash256(sk_net)[:4]
    return base58.b58encode(addr)

def addr(key):
    '''restituisce indirizzo btc'''
    ec_sk = ecdsa.SigningKey.from_string(secretKey, curve = ecdsa.SECP256k1)
    ec_pubk = ec_sk.get_verifying_key()
    pubk = bytes.fromhex('04') + ec_pubk.to_string()
    pkh = bytes.fromhex('00') + hash160(pubk)
    checksum = hash256(pkh)[:4]
    return base58.b58encode(pkh + checksum)

def pub_key(key):
    '''restituisce la public key'''
    ec_sk = ecdsa.SigningKey.from_string(secretKey, curve = ecdsa.SECP256k1)
    ec_pubk = ec_sk.get_verifying_key()
    pubk = bytes.fromhex('04') + ec_pubk.to_string()
    return pubk.hex()

#FINE FUNZIONI

#visualizzazione del titolo 
messaggio = input("Secure generation of a bitcoin wallet. Press enter to begin")
clear_screen()

#acquisizione della prima stringa casuale dal primo utente
stringa1 = input("USER 1 type a random string and annotate, then press enter: ")
clear_screen()

#acquisizione della seconda stringa casuale dal secondo utente
stringa2 = input("USER 2 type a random string and annotate, then press enter: ")
clear_screen()

#concatenazione delle due stringhe in un unica stringa
stringa = stringa1 + stringa2

#calcolo dell'hash della stringa ottenuta
secretKey = hashlib.sha256(stringa.encode()).digest()
secretKeyW = wif(secretKey)

#visualizzazione al PRIMO utente della prima metá dell'hash ottenuto
messaggio = input("Switch the computer to User 1 and press enter")
clear_screen()
print("Private key part 1:     " + secretKeyW.decode("utf-8")[:25])
print("")
messaggio = input("Write down the private key and press enter, then go to user 2")
clear_screen()

#visualizzazione al SECONDO utente della seconda metá dell'hash ottenuto
messaggio = input("User 2, when ready press enter")
clear_screen()
print("Private key part 2:     " + secretKeyW.decode("utf-8")[25:])
print("")
messaggio = input("Write down the private key and press enter")
clear_screen()

#messaggio di fine procedura e visualizzazione dell'indirizzo bitcoin generato
messaggio = input("Procedure finished, press enter to display the wallet address")
clear_screen()
print("Wallet:      " + addr(secretKey).decode("utf-8"))
