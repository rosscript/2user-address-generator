# Simple Address Generator

Questo progetto contiene due script Python per la generazione sicura di wallet dividendo la chiave privata tra due utenti.

1. `walletcreatebtc.py` - Generatore di wallet Bitcoin
2. `walletcreateth.py` - Generatore di wallet Ethereum

## Caratteristiche

- Generazione sicura di chiavi private
- Supporto multi-utente per maggiore sicurezza
- Compatibilità con Windows e Unix/Linux
- Integrazione con client come Electrum (Bitcoin) e MetaMask (Ethereum)

## Requisiti

- Python 3.x
- Librerie Python:
  - hashlib
  - base58
  - ecdsa
  - eth_account

## Installazione

```bash
pip install base58 ecdsa eth_account
```

## Utilizzo

1. Eseguire lo script desiderato:
   ```bash
   python walletcreatebtc.py  # Per Bitcoin
   # oppure
   python walletcreateth.py   # Per Ethereum
   ```

2. Seguire le istruzioni a schermo per la generazione del wallet
