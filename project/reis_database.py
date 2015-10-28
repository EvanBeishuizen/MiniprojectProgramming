from database import *
from qr import *
from tkinter import *


""" Naam,Ov-chipkaartnummer , Beginstation, Eindstation worden in de variabele 'velden opgeslagen zodat deze kunnen worden gebruikt om gegevens in te vullen """


class reis_database(object):

    def __init__(self, db):
        self.db = db
        self.db_connection = database(self.db)
        self.qr_connection = qr()
        self.setupUI()


    def send_data(self, data):
        self.db_connection.insert_traveldata(data[0][1].get(), data[1][1].get(), data[2][1].get(), data[3][1].get())
        self.qr_connection.create_qr(self.db_connection.get_travelID(data[1][1].get()))

        ents[0][1].delete(0,END)
        ents[1][1].delete(0,END)
        ents[2][1].delete(0,END)
        ents[3][1].delete(0,END)

    def makeform(self, root, velden):
        NS_logo=Canvas(root, highlightthickness=0)
        NS_logo.pack(expand=TRUE, fill=NONE)
        image1=PhotoImage(file="Nederlandse_spoorwegen_logo.gif")
        NS_logo.img=image1
        NS_logo.create_image(-10, 0, anchor=NW, image=image1)
        invoer = []

        for veld in velden:
            row = Frame(root, bg= "#fc3")
            """ Van elk tekstvlak rij krijgt de rand een gele kleur """

            lab = Label(row, font = "Arial 13 bold", width=17, text=veld,fg = "#000066",  anchor='w', bg='#fc3' )
            """instellingen voor uiterlijk window"""
            root.resizable(0,0)
            """grootte window staat vast"""
            ent = Entry(row)
            """mogelijkheid voor input gebruiker"""
            row.pack(side=TOP, fill=X, padx=60, pady=2)
            """Maat voor label van invoeveld"""
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X , padx = 80, pady = 23)
            """maat voor invoerveld"""
            invoer.append((veld, ent))
            root.configure(bg='#fc3')
            """ Achtergrond van de root (applicatie) krijgt een gele kleur """
        return invoer


    def setupUI(self):
        velden = 'Naam', 'Ov-chipkaartnummer', 'Beginstation', 'Eindstation'
        root = Tk()
        root.wm_title("Reis database")
        global ents
        ents = self.makeform(root, velden)
        root.bind('<Return>', (lambda event, e=ents: self.send(e)))
        b1 = Button(root, text='sluiten', bg = "#000066", fg= "white", width = 8, height =2,
          command=root.destroy)
        """ Door op deze button te klikken worden jouw ingevoerde gegevens opgeslagen in de database """
        b1.pack(side=RIGHT, padx=0 , pady=10)
        """"maten knop 1"""
        b2 = Button(root, text='voer in', bg = "#000066", fg= "white", width = 8, height =2,command=(lambda e=ents: self.send_data(e)))
        """ Het programma sluiten d.m.v. deze knop """
        b2.pack(side=RIGHT, padx=10, pady=10)
        root.mainloop()


if __name__ == "__main__":
    reis_database = reis_database("database/reisgegevens.db")


