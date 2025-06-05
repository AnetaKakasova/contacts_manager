contacts = [
    {
        "name": "Anička",
        "email": "anicka@email.com",
        "phone": "777 777 777"
    },
    {
        "name": "Nikol",
        "email": "nikol@email.com",
        "phone": "777 777 777"
    }
]

def hlavni_menu():
    print("1. Zobrazit kontakty\n2. Přidat kontakt\n3. Ukončit")
    # načte vstup od uživatele
    vyber_funkce = input("Vyberte funkci 1-3: ")
    print("Byla vybrána funkce: " + vyber_funkce)
