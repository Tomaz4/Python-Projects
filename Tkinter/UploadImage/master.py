from tkinter import *
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('Learn To Code')
root.iconbitmap('file.ico')

bledImage = ImageTk.PhotoImage(Image.open('Bled.jpg'))

my_label = Label(image=bledImage)
my_label.pack()

exitButton = Button(root, text = "Exit Program", command = root.destroy)
exitButton.pack()

root.mainloop()
