from tkinter import *
from PIL import Image
from PIL import ImageTk
import os


def nextPhoto(photos):
    '''This function displays next picture'''
    
    global picLabel
    global picNumber
    global nextButton
    global exitButton
    
    picLabel.grid_forget()
    picNumber+=1
    picLabel = Button(root, image = photos[picNumber])
    picLabel.grid(row = 0, column = 0, columnspan = 3)
    
    if(picNumber >= (len(photos) - 1)):
        nextButton = Button(root, text = ">>", command= lambda: nextPhoto(photos), state = DISABLED)
        nextButton.grid(row = 1, column = 3)

    if(picNumber > 0):
        backButton = Button(root, text = "<<", command= lambda: previousPhoto(photos), state=NORMAL)
        backButton.grid(row = 1, column = 1)

    
def previousPhoto(photos):
    '''This function displays previous picture'''
    
    global picLabel
    global picNumber
    global nextButton
    global exitButton
    
    picLabel.grid_forget()
    picNumber-=1
    picLabel = Button(root, image = photos[picNumber])
    picLabel.grid(row = 0, column = 0, columnspan = 3)
    
    if(picNumber == 0):
        backButton = Button(root, text = "<<", command= lambda: previousPhoto(photos), state=DISABLED)
        backButton.grid(row = 1, column = 1)

    if(picNumber < (len(photos) - 1)):
        nextButton = Button(root, text = ">>", command= lambda: nextPhoto(photos), state = NORMAL)
        nextButton.grid(row = 1, column = 3)
    
picNumber = 0

root = Tk()
root.title("Photo viewer")

#Append all jpg and png pictures on array
photos = []
stevec = 0
for file in os.listdir('.'):
    if(file.endswith('.jpg') or file.endswith('.png')):
        stevec+=1
        image = Image.open(file)
        image = image.resize((832, 468), Image.ANTIALIAS)
        photos.append(ImageTk.PhotoImage(image))

#Label for a picture
picLabel = Button(root, image = photos[0])
picLabel.grid(row = 0, column = 0, columnspan = 3)

#Back button
backButton = Button(root, text = "<<", command= lambda: previousPhoto(photos), state=DISABLED)
backButton.grid(row = 1, column = 1)

#Exit button
exitButton = Button(root, text = "Exit Program", command=root.destroy)
exitButton.grid(row = 1, column = 2)

#Next Button
nextButton = Button(root, text = ">>", command= lambda: nextPhoto(photos))
nextButton.grid(row = 1, column = 3)

root.mainloop()


