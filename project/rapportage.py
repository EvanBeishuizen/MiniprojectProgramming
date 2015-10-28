__author__ = 'Dennis'
import database


db = "database/reisgegevens.db"



def write_amount_travels(db):
    data = database.get_countOV(db)
    f = open("rapportage/rapportage.txt", "w")
    f.write("Aantal reizen per ov-nummer:" + "\n")

    for ov in data:
        f.write(str(ov[0]) + " : " + str(ov[1]) + "\n")




if __name__ == "__main__":
    database.setup(db)
    write_amount_travels(db)