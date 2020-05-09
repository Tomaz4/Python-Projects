import tkinter
#from tkinter import *
class Slikar():
    """Graficna aplikacija za risanje."""

    def __init__(self, glavnoOkno):
        okvir = tkinter.Frame()
        okvir.pack(side=tkinter.LEFT, fill = tkinter.Y)
        tkinter.Label(okvir,text = 'Parametri').grid(row = 1,column = 1,sticky = tkinter.W)
        self.par = tkinter.Entry(okvir)
        self.par.grid(row = 1,column = 2)
        tkinter.Label(okvir,text = 'Položaj x').grid(row = 2,column = 1,sticky = tkinter.W)
        self.polX = tkinter.Entry(okvir)
        self.polX.grid(row = 2,column = 2)
        tkinter.Label(okvir,text = 'Položaj y').grid(row = 3,column = 1,sticky = tkinter.W)
        self.polY = tkinter.Entry(okvir)
        self.polY.grid(row = 3,column = 2)
        # Glavni menu
        self.platno = tkinter.Canvas(glavnoOkno,
                                     width=640, height=480)
        self.platno.pack()


        glavniMenu = tkinter.Menu(glavnoOkno)
        glavnoOkno.config(menu=glavniMenu) # Dodamo glavni menu v okno
        # Podmenu za urejanje
        
        menuNarisi = tkinter.Menu(glavniMenu)
        glavniMenu.add_cascade(label="Narisi", menu=menuNarisi)
        menuNarisi.add_cascade(label="Piramida",command = self.piramida)
        menuNarisi.add_cascade(label="Tarca",command = self.tarca)


        menuPobrisi = tkinter.Menu(glavniMenu)
        glavniMenu.add_cascade(label="Pobrisi", menu=menuPobrisi)
        menuPobrisi.add_cascade(label="Zbrisi vse",command = self.zbrisiSliko)
        menuPobrisi.add_cascade(label="Zbrisi zadnjega",command = self.zbrisiZadnji)

        glavniMenu.add_cascade(label="Koncaj", command = glavnoOkno.destroy)
        self.slika = []

        self.platno.bind('<Button-1>',self.zacni)
        self.platno.bind('<B1-Motion>',self.premik)
        self.izbira = None

    def zacni(self,event):
        self.x = event.x
        self.y = event.y
        seznam = self.platno.find_overlapping(self.x,self.y,self.x+1,self.y+1)
        if seznam == []:
            self.izbira = None
        else:
            el = seznam[-1]
            for lik in self.slika:
                if el in lik:
                    self.izbira = lik
                    break

    def premik(self,event):
        if self.izbira == None:
            return
        dx = (self.x - event.x)*(-1)
        dy = -1*(self.y - event.y)
        for el in self.izbira:
            self.platno.move(el,dx,dy)
        self.x = event.x
        self.y = event.y
        

                               
    def piramida(self):
        n = int(self.par.get() or 5)
        polx = int(self.polX.get() or 0)
        poly = int(self.polY.get() or 0)
        s = piramida(self.platno,n,polx,poly,20)
        self.slika.append(s)
        
    def tarca(self):
        s = tarca(self.platno,8,200,200,20)
        self.slika.append(s)

    def zbrisiSliko(self):
        self.platno.delete('all')
        self.slika = []

    def zbrisiZadnji(self):
        if self.slika == []:
            return
        seznam = self.slika.pop()
        for el in seznam:
            self.platno.delete(el)
        


def piramida(platno,n,x,y,d):
    '''Narišemo piramido'''
    seznam = []
    stevec =1
    x1 = x
    y1 =y
    x2= x+d
    y2 = y+d
    while stevec <= n:
        id = platno.create_rectangle(x1,y1,x2,y2,outline='',fill='orange')
        x1 = x1-d
        y1 =y1+d
        x2= x2+d
        y2 = y2+d
        stevec +=1
        seznam.append(id)
    return seznam

#def trikotnik(platno,n,x,y,d):
    ''' na platno nariše trikotnik Sierpinskega reda n,
    pri čemer je (x, y) levo spodnje oglišče, d pa dolžina osnovnice'''
    
    
def tarca(platno,n,x,y,d):
    """Narišemo tarco"""
    seznam = []
    stevec =1
    x1 = x-n*d
    y1 =y-n*d
    x2= x+n*d
    y2 = y+n*d
    if n%2==0:
        while stevec <= n:
            if stevec %2==0:
                id = platno.create_oval(x1, y1, x2,y2,outline='',fill='black')
                seznam.append(id)

            else:
                id = platno.create_oval(x1, y1, x2,y2,outline='',fill='white')
                seznam.append(id)
            x1 = x1+d
            y1 =y1+d
            x2= x2-d
            y2 = y2-d
            stevec +=1
    else:
         while stevec <= n:
            if stevec %2==0:
                id = platno.create_oval(x1, y1, x2,y2,outline='',fill='white')
                seznam.append(id)
            else:
                id = platno.create_oval(x1, y1, x2,y2,outline='',fill='black')
                seznam.append(id)
            x1 = x1+d
            y1 =y1+d
            x2= x2-d
            y2 = y2-d
            stevec +=1
    return seznam

if __name__ =="__main__":
    #ustvarimo okno
    glavno = tkinter.Tk()
    glavno.title("Slikar")
    aplikacija = Slikar(glavno)
    glavno.mainloop()
