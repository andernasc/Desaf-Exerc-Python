import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('https://google.com/')

mygoogle = Button(root, text='Abrir o google', command=google()).pack(pady=20)
root.mainloop()