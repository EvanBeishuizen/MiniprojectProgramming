from tkinter import *
import incheckzuil
import doctest
doctest.testmod()

class incheckzuil(object):

    def __init__(self, db):
        self.db = db
        self.db_connection = database(self.db)
        self.qr_connection = qr()
        self.setupUI()


    def send_data(entry):
        incheckzuil.send_ovnummer(incheckzuil.db, entry[0].get())
        ent.delete(0,END)


    def print_travels(self):


    def makeform(root):
        NS_logo=Canvas(root, highlightthickness=0)
        NS_logo.pack(expand=TRUE, fill=NONE)
        image1=PhotoImage(file="Nederlandse_spoorwegen_logo.gif")
        NS_logo.img=image1
        NS_logo.create_image(-10, 0, anchor=NW, image=image1)
        """window wordt voorzien van een NS-logo"""
        invoer = []
        row = Frame(root, bg= "#fc3")
        """ Van elk tekstvlak rij krijgt de rand een gele kleur """

        lab = Label(row, font = "Arial 13 bold", width=17, text='OV-chipkaartnummer',fg = "#000066",  anchor='w', bg='#fc3' )
        """instellingen voor uiterlijk window"""
        root.resizable(0,0)
        """grootte window staat vast"""
        global ent
        ent = Entry(row)
        """mogelijkheid voor input gebruiker"""
        row.pack(side=TOP, fill=X, padx=60, pady=2)
        """Maat voor label van invoeveld"""
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X , padx = 80, pady = 23)
        """maat voor invoerveld"""
        invoer.append((ent))
        root.configure(bg='#fc3')
        """ Achtergrond van de root (applicatie) krijgt een gele kleur """
        return invoer

    def setupUI():
         root = Tk()
         root.wm_title("Reis database")
        ents = makeform(root)
        root.bind('<Return>', (lambda event, e=ents: send(e)))
         b1 = Button(root, text='sluiten', bg = "#000066", fg= "white", width = 8, height =2,
          command=root.quit)
        """ Door op deze buttonte klikken worden jouw ingevoerde gegevens opgeslagen in de database """
        b1.pack(side=RIGHT, padx=0 , pady=10)
        """"maten knop 1"""
        b2 = Button(root, text='voer in', bg = "#000066", fg= "white", width = 8, height =2,command=(lambda e=ents: send(e)) )
        """ Het programma sluiten d.m.v. deze knop """
        b2.pack(side=RIGHT, padx=10, pady=10)
        root.mainloop()
