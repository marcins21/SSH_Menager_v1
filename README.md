# Podstawowa Struktura Json
### Plik `servers.json` musi posiadac podana strukture

    {
    "servers": [
          {
             "[nazwa]": {
                "username": "[nazwa]",
                "password": "[nazwa]",
                "ip": "[address_ip]"
             }
          }
       ]
    }
Poniewaz nowe rekordy sa dodawane za pomoca funkcji `append`
jezeli tej struktury nie bedzie, program nie zadziała


# Plik `menu.py`
W tym pliku znajduja sie sie funkcje odpowiadajace za dodawanie usuwanie edycje
oraz pokazywanie danych o serwerach




















