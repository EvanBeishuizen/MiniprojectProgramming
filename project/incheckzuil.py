__author__ = 'Dennis'

import database
import incheckzuil_ui


db = "database/reisgegevens.db"

if __name__ == "__main__":
    database.setup(db)
    incheckzuil_ui.setupUI()

def send_ovnummer(db,ov_nummer):
    gegevens = database.get_traveldata(db,ov_nummer)
    if gegevens:
        print("\novnummer:" + str(ov_nummer))
        print("naam: " + gegevens[0][2])
        print("\nReizen:")
        for row in gegevens:
            print("ReisID: " + str(row[0]))
            print("Beginstation: " + row[3])
            print("Eindstation: " + row[4] + "\n")

    else:
        print("Geen gegevens beschikbaar van het ovnummer: " + ov_nummer)




