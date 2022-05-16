from tkinter import *
import tkinter as tk
window=Tk()
# add widgets here
window.iconbitmap(r'C:\Users\Costas\Desktop\Pytorch\logo-modified.ico')  
window.title('Pocket Gym')
#window.aspect(1,1,1,1)
window.geometry("1200x600+10+20")
window.configure(bg='white')
def not_working():
   text.config(text= "Not Working yet")

#Import the image using PhotoImage function
aithmata= PhotoImage(file='buttons/aitimata.png')
drastiriothta=PhotoImage(file='buttons/drastiriotita.png')
news=PhotoImage(file='buttons/news.png')
profil=PhotoImage(file='buttons/profil.png')
istoriko=PhotoImage(file='buttons/istoriko.png')
logo= PhotoImage(file='logo-modified.png')
#Let us create a label for button event

frameA = tk.Frame(background="#ffffff")
frameB = tk.Frame(width=400, height = 600, background="#ffffff")
# Nested Frame. framebb is created within frameB without width or height
framebb = tk.Frame(frameB, background="#ffffff")


frameA.pack(side='top', fill=None)
frameB.pack(side='top')
# expand is the key parameter to center the framebb within frameB
framebb.pack(expand=True)


#frameA.pack_propagate(False)
frameB.pack_propagate(False)


#%% Buttons and Labels
tk.Label(frameA, image=logo).pack()
Button(window, image=aithmata,command= not_working,
borderwidth=0)

a = tk.Button(framebb, image=aithmata,command= not_working,
borderwidth=0).pack()
b = tk.Button(framebb, image=drastiriothta,command= not_working,
borderwidth=0).pack()
c = tk.Button(framebb, image=istoriko,command= not_working,
borderwidth=0).pack()
d=tk.Button(framebb, image=profil,command= not_working,
borderwidth=0).pack()
e=tk.Button(framebb, image=news,command= not_working,
borderwidth=0).pack()
f=tk.Button(framebb, image=aithmata,command= not_working,
borderwidth=0).pack()
text= Label(window, text= "")
text.pack()

tk.mainloop()