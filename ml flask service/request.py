# 0 = krediver, 1 = verme
# 0 = evsahibi, 1 = kiracı
# 0 = telefon yok, 1 = var

import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
payload = {
    'krediMiktari': 300000,
    "yas": 25,
    "evDurumu": 0,
    "aldigi_kredi_sayi": 2,
    "telefonDurumu": 0
}

r = requests.post(url, json=payload)

print(r.json())
