
import tkinter as tk

def changer():
    etiket.config(fg="red")

fen = tk.Tk()

fen.title("AAAAAAAAAAAAA")
fen.geometry("700x300+200+200")
fen.config(bg="#228491")

etiket = tk.Label(fen, text="AAAAAAAAAAAAAAAAAAAAAAA")
etiket.pack(expand=1)

leavbut = tk.Button(fen,text="red",command=changer)
leavbut.pack(side=tk.RIGHT,padx=10,pady=10)

fen.mainloop()
