## Comando Carabinieri Antifalsificazione Monetaria - Sezione Criptovalute
## Creazione di un wallet bitcoin utilizzabile con client tipo Electrum

#importazione delle librerie necessarie
import hashlib, base58, ecdsa, os

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
messaggio = input("Comando Carabinieri Antifalsificazione Monetaria - Sezione Criptovalute. Generazione sicura di un wallet bitcoin. Premere invio per iniziare")
os.system('clear')

#acquisizione della prima stringa casuale dal primo utente
stringa1 = input("UTENTE 1 digitare una stringa casuale e annotare, poi premere invio: ")
os.system('clear')

#acquisizione della seconda stringa casuale dal secondo utente
stringa2 = input("UTENTE 2 digitare una stringa casuale e annotare, poi premere invio: ")
os.system('clear')

#concatenazione delle due stringhe in un unica stringa
stringa = stringa1 + stringa2

#calcolo dell'hash della stringa ottenuta
secretKey = hashlib.sha256(stringa.encode()).digest()
secretKeyW = wif(secretKey)

#visualizzazione al PRIMO utente della prima metá dell'hash ottenuto
messaggio = input("Passare il computer all'Utente 1 e premere invio")
os.system('clear')
print("Private key parte 1:     " + secretKeyW.decode("utf-8")[:25])
print("")
messaggio = input("Annotare la private key e premere invio, poi passare all'utente 2")
os.system('clear')

#visualizzazione al SECONDO utente della seconda metá dell'hash ottenuto
messaggio = input("Utente 2, quando pronto premere invio")
os.system('clear')
print("Private key parte 2:     " + secretKeyW.decode("utf-8")[25:])
print("")
messaggio = input("Annotare la private key e premere invio")
os.system('clear')

#messaggio di fine procedura e visualizzazione dell'indirizzo bitcoin generato
messaggio = input("Procedura terminata, premere invio per visualizzare l'address del wallet")
os.system('clear')
print("Wallet:      " + addr(secretKey).decode("utf-8"))
