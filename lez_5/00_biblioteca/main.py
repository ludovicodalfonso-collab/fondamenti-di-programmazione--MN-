from biblioteca import *

aggiungi_libro("Il nome della rosa", "Umberto Eco")
aggiungi_libro("1984", "George Orwell")
aggiungi_libro("1984", "George Orwell")
aggiungi_utente("Mario Rossi")
aggiungi_utente("Luigi Bianchi")
aggiungi_utente("Marco Mamei")
print(cerca_utente("Mario Rossi"))  # Output: [1]
print(cerca_libro("1984"))          # Output: [2]

id = cerca_utente("Mario Rossi")[0]
ok = presta_libro(id, "1984", "2025-10-30")
id = cerca_utente("Luigi Bianchi")[0]
ok = presta_libro(id, "1984", "2025-10-30")
id = cerca_utente("Marco Mamei")[0]
ok = presta_libro(id, "1984", "2025-10-30")

