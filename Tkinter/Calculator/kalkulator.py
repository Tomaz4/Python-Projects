import tkinter

class Kalkulator():

    def __init__(self,glavnoOkno):
        # izpisovanje rezultata
        self.platno = tkinter.Canvas(glavnoOkno,width = 200,height = 70)
        self.platno.grid(row = 0,column = 1,columnspan = 4)
        self.platno.create_rectangle(2,2,198,34)
        self.platno.create_rectangle(2,36,198,70)
        self.v1 = self.platno.create_text(196,27,text= '',anchor=tkinter.SE)
        self.v2 = self.platno.create_text(196,62,text= '',anchor=tkinter.SE)
        # gumbi
        gumb7 = tkinter.Button(glavnoOkno,text='7',command = lambda: self.spremeniv1('7'),height = 2, width = 5)
        gumb7.grid(row = 3,column=1)
        gumb8 = tkinter.Button(glavnoOkno,text='8',height = 2, width = 5,bg = 'orange',command = lambda: self.spremeniv1('8'))
        gumb8.grid(row = 3,column=2)
        gumb9 = tkinter.Button(glavnoOkno,text='9',height = 2, width = 5,command = lambda: self.spremeniv1('9'))
        gumb9.grid(row = 3,column=3)
        gumb4 = tkinter.Button(glavnoOkno,text='4',height = 2, width = 5,command = lambda: self.spremeniv1('4'))
        gumb4.grid(row = 4,column=1)
        gumb5 = tkinter.Button(glavnoOkno,text='5',height = 2, width = 5,command = lambda: self.spremeniv1('5'))
        gumb5.grid(row = 4,column=2)
        gumb6 = tkinter.Button(glavnoOkno,text='6',height = 2, width = 5,command = lambda: self.spremeniv1('6'))
        gumb6.grid(row = 4,column=3)
        gumb1 = tkinter.Button(glavnoOkno,text = '1' ,height = 2, width = 5,command = lambda: self.spremeniv1('1'))
        gumb1.grid(row = 5,column=1)
        gumb2 = tkinter.Button(glavnoOkno,text='2',height = 2, width = 5,command = lambda: self.spremeniv1('2'))
        gumb2.grid(row = 5,column=2)
        gumb3 = tkinter.Button(glavnoOkno,text='3',height = 2, width = 5,command = lambda: self.spremeniv1('3'))
        gumb3.grid(row = 5,column=3)
        gumbplus = tkinter.Button(glavnoOkno,text='+',height = 2, width = 5,command = lambda: self.spremeniv1('+'))
        gumbplus.grid(row = 3,column=4)
        gumbminus = tkinter.Button(glavnoOkno,text='-',height = 2, width = 5,command = lambda: self.spremeniv1('-'))
        gumbminus.grid(row = 4,column=4)
        gumbkrat = tkinter.Button(glavnoOkno,text='*',height = 2, width = 5,command = lambda: self.spremeniv1('*'))
        gumbkrat.grid(row = 5,column=4)
        gumb0 = tkinter.Button(glavnoOkno,text='0',height = 2, width = 5,command = lambda: self.spremeniv1('0'))
        gumb0.grid(row = 6,column=1)
        gumbvejica = tkinter.Button(glavnoOkno,text=',',height = 2, width = 5,command = lambda: self.spremeniv1(','))
        gumbvejica.grid(row = 6,column=2)
        gumbenako = tkinter.Button(glavnoOkno,text='=',height = 2, width = 5,command = self.izracunaj)
        gumbenako.grid(row = 6,column = 3)
        gumbdeljeno = tkinter.Button(glavnoOkno,text='/',height = 2, width = 5,command = lambda: self.spremeniv1('/'))
        gumbdeljeno.grid(row = 6,column = 4)
        gumbzbrisiC = tkinter.Button(glavnoOkno,text='C',height = 2, width = 5,command = self.zbrisi)
        gumbzbrisiC.grid(row = 3,column = 5)
        gumbzbrisiDel = tkinter.Button(glavnoOkno,text='<-',height = 2, width = 5,command = self.zbrisiDel)
        gumbzbrisiDel.grid(row = 4,column = 5)
        gumbOklepaji = tkinter.Button(glavnoOkno, text = '( )',height = 2, width = 5, command = self.dodajOklepaje)
        gumbOklepaji.grid(row =5 , column = 5)
        gumbneg = tkinter.Button(glavnoOkno,text='+/-',height = 2, width = 5,command = self.negiraj)
        gumbneg.grid(row =6 , column = 5)
        # shranjeni podatki
        self.niz = '' # niz za izpis
        self.nizPikce = '' # niz s pikcami, namesto vejicami za decimalno število
        self.rezultat = 0 # poračunan rezultat
        self.pritisnjenEnako = False # ali je bil pritisnjen gumb je enako
        self.error = False # v primeru da je pri prejšnjem izračunu prišlo do error-ja, bo delovala samo tipka, ki vse pobriše


    def zbrisi(self):
        ''' Funkcija izbriše celoten izpisan niz. '''
        self.pritisnjenEnako = False
        self.error = False
        self.niz = ''
        self.nizPikce = ''
        self.platno.itemconfig(self.v1,text=self.niz)
        self.platno.itemconfig(self.v2,text=self.nizPikce)

    def zbrisiDel(self):
        ''' Funkcija zbriše en znak v nizu. '''
        if self.error == False:
            if self.pritisnjenEnako == False:
                if len(self.niz) != 0:
                    if self.niz[-1] == ' ': # če je na koncu presledek, potem pobrišemo presledek, operacijo in še en presledek
                                            # (torej ko pobrišemo presledek, pobrišemo 3 znake)
                        self.niz = self.niz[0:len(self.niz)-3]
                    else:
                        self.niz = self.niz[0:len(self.niz)-1]
                    self.platno.itemconfig(self.v1,text=self.niz)

    
    def spremeniv1(self,podatek):
        ''' Funkcija spreminja niz za izpis. '''
        if self.error == False:
            if self.pritisnjenEnako == False:
                if self.smiselenIzraz(podatek): # ali je izraz še zmeraj smiselen po tem ko dodamo nov znak
                    if len(self.niz) >= 1:
                        if podatek == ',':
                            if self.niz.split()[-1][-1] in '+-*/(':
                                self.niz = self.niz + '0,'
                            else:
                                self.niz = self.niz + ','
                        # številke pišemo skupaj:
                        elif (podatek in '0123456789'):
                            seznam = self.niz.split()
                            # če imamo napisano '0' in želimo nato dodati število, izbrišemo '0' (npr. '02' --> '2')
                            # pogledamo če je pred '0' kakšen operator
                            if (len(seznam) > 1) and seznam[-1][-1] == '0':
                                if len(seznam[-1]) > 1 and seznam[-1][-2] == '(':
                                    self.niz = self.niz[0:len(self.niz)-1] + podatek
                                elif seznam[-1] == '0':
                                    self.niz = self.niz[0:len(self.niz)-1] + podatek
                                else:
                                    self.niz = self.niz + podatek
                            # če imamo v nizu samo '0' in nobene operacije in hočemo dodati številko
                            elif len(seznam) == 1 and self.niz[-1] == '0':
                                if len(self.niz) == 1:
                                    self.niz = self.niz[0:len(self.niz)-1] + podatek
                                else:
                                    if len(self.niz) > 1 and self.niz[-2] == '(':
                                        self.niz = self.niz[0:len(self.niz)-1] + podatek
                                    else:
                                        self.niz = self.niz + podatek
                            else:
                                self.niz = self.niz + podatek
                        else: # med operacijami imamo presledek
                            # preverjamo samo operacije
                            # dodajamo presledke
                            if self.niz[-1] == ',':
                                self.niz = self.niz + '0 '+ podatek + ' '
                            else:
                                self.niz = self.niz + ' ' + podatek + ' '
                    else:
                        if podatek == ',':
                            self.niz = self.niz + '0,'
                        else:
                            self.niz = self.niz + podatek
                    # spreminja tekst ki se izpisuje
                    self.platno.itemconfig(self.v1,text=self.niz)
            else:
                self.pritisnjenEnako = False
                rezultat = str(round(self.rezultat,8))
                rezultat = rezultat.replace('.',',')
                if podatek == ',':
                    self.niz = rezultat
                elif podatek in '+-*/':
                    self.niz = rezultat+' ' + podatek + ' '
                else:
                    self.niz = rezultat+podatek
                self.rezultat = 0
                self.nizPikce = ''
                self.platno.itemconfig(self.v1,text=self.niz)
                self.platno.itemconfig(self.v2,text='')

    def smiselenIzraz(self,podatek):
        ''' Funkcija preverja ali je znak smiselno dodati v niz ali ne. '''
        seznam = self.niz.split() # glede na presledek ločimo vse elemente niza
        if podatek == ',':
            if len(self.niz) > 0:
                if seznam[-1] in '+-*/':
                    return True
                else:
                    if '(' in seznam[-1]:
                        if seznam[-1][-1] == '(':
                            return True
                        # na katerem mestu je zadnji oklepaj
                        mesto = 0
                        for i in range(0,len(seznam[-1])):
                            if seznam[-1][i] != '(':
                                mesto = i
                                break
                        # ali dodamo vejico:
                        nizBrezOklepajev = seznam[-1][mesto:len(seznam[-1])]
                        try:
                            float(nizBrezOklepajev)
                        except:
                            return False
                    else:
                        try:
                            # izraz je smiselen, samo če je decimalno število, ne bo smiselen
                            # če bo npr. '3,4,5' oz. '3,,', ...
                            float(seznam[-1])
                        except:
                            return False
        elif podatek in '+-*/':
            if len(self.niz) == 0:
                return False
            else:
                if self.niz[-1] == '(':
                    return False
                elif seznam[-1] in '+-*/':
                    return False
        elif podatek in '0123456789':
            if len(self.niz) > 1 and self.niz[-1] == ')':
                return False
        return True  
        

    def izracunaj(self):
        ''' Funkcija izračuna izraz podan v nizu. '''
        if self.pritisnjenEnako == True: # 2x ne smemo pritisniti je enako
            pass
        else:
            self.pritisnjenEnako = True
            mestoStevilke = -1
            for i in range(0,len(self.niz)):
                if self.niz[i] == ',':
                    self.nizPikce += '.'
                else:
                    self.nizPikce += self.niz[i]
                if self.niz[i] in '0123456789':
                    mestoStevilke = i
            if mestoStevilke == -1: # sploh nimamo številke v izrazu, torej je error
                self.platno.itemconfig(self.v2,text='Error')
                self.error = True
            else:
                # dodamo manjkajoče zaklepaje
                self.nizPikce = self.nizPikce[0:mestoStevilke + 1]
                self.nizPikce += (self.nizPikce.count('(') - self.nizPikce.count(')'))*')'
                self.niz = self.nizPikce.replace('.',',')
                try:
                    self.rezultat = eval(self.nizPikce)
                    self.nizPikce = self.nizPikce + ' ='
                    self.platno.itemconfig(self.v1,text=self.niz)
                    self.platno.itemconfig(self.v2,text=str(round(self.rezultat,8)))
                except ZeroDivisionError:
                    self.platno.itemconfig(self.v2,text='ZeroDivisionError')
                    self.error = True

    def dodajOklepaje(self):
        ''' Funkcija v niz za izpis dodaja oklepaje, ko je pritisnjen gumb za oklepaje. '''
        if self.error == False:
            if len(self.niz) == 0:
                self.niz = self.niz + '('
            else:
                if self.niz[-1] == ' ' or self.niz[-1] == '(': # na koncu imamo operator in nato presledek
                                                               # ali pa imamo oklepaj in hočemo še enega
                    self.niz = self.niz + '('
                else:
                    # dodajamo zaklepaje
                    if self.niz.count('(') > self.niz.count(')'):
                        if self.niz[-1] == ',':
                            self.niz = self.niz + '0)'
                        elif self.niz[-1] == ')' or self.niz[-1] in '0123456789':
                            self.niz = self.niz + ')'
            self.platno.itemconfig(self.v1,text=self.niz)

    def negiraj(self):
        ''' Funkcija negira zadnje podano število.
            2 -> -2
            '''
        if len(self.niz) > 0:
            if self.niz[-1] in '0123456789': # deluje samo če je zadnji znak
                                             # v nizu števka
                kateroSt = ''
                if len(self.niz) > 0:
                    mesto = -1
                    # ugotovimo na katerem mestu se naše zadnje število konča:
                    for i in range(len(self.niz)-1,-1,-1):
                        if self.niz[i] in '-0123456789,':
                            kateroSt = self.niz[i] + kateroSt
                        else:
                            mesto = i
                            break
                    kateroSt = kateroSt.replace(',','.')
                    try:
                        kateroSt = int(kateroSt) # ne izpisujemo nepotrebnih decimalnih mest
                    except:
                        kateroSt = float(kateroSt)
                    if mesto == -1: # niz je zelo kratek, torej npr samo '2'
                        self.niz = '('+str(-1*kateroSt)+')'
                        self.niz = self.niz.replace('.',',')
                        self.platno.itemconfig(self.v1,text=self.niz)
                    else:
                        self.niz = self.niz[0:mesto+1]+'('+str(-1*kateroSt)+')'
                        self.niz = self.niz.replace('.',',')
                        self.platno.itemconfig(self.v1,text=self.niz)
                    
glavno = tkinter.Tk()
glavno.title('Kalkulator')
aplikacija = Kalkulator(glavno)
glavno.mainloop()
