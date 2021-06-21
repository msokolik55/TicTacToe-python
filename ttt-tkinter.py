from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Piskvorky")

counter = 1
player = 1
winner = False

def disable_buttons():
  b1.config(state=DISABLED)
  b2.config(state=DISABLED)
  b3.config(state=DISABLED)
  b4.config(state=DISABLED)
  b5.config(state=DISABLED)
  b6.config(state=DISABLED)
  b7.config(state=DISABLED)
  b8.config(state=DISABLED)
  b9.config(state=DISABLED)

def check_winner(symbol):
  global winner

  # rows
  if b1["text"] == b2["text"] == b3["text"] == symbol:
    b1.config(bg="red")
    b2.config(bg="red")
    b3.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  elif b4["text"] == b5["text"] == b6["text"] == symbol:
    b4.config(bg="red")
    b5.config(bg="red")
    b6.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  elif b7["text"] == b8["text"] == b9["text"] == symbol:
    b7.config(bg="red")
    b8.config(bg="red")
    b9.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  # columns
  elif b1["text"] == b4["text"] == b7["text"] == symbol:
    b1.config(bg="red")
    b4.config(bg="red")
    b7.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  elif b2["text"] == b5["text"] == b8["text"] == symbol:
    b2.config(bg="red")
    b5.config(bg="red")
    b8.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  elif b3["text"] == b6["text"] == b9["text"] == symbol:
    b3.config(bg="red")
    b6.config(bg="red")
    b9.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  # diagonals
  elif b1["text"] == b5["text"] == b9["text"] == symbol:
    b1.config(bg="red")
    b5.config(bg="red")
    b9.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

  elif b3["text"] == b5["text"] == b7["text"] == symbol:
    b3.config(bg="red")
    b5.config(bg="red")
    b7.config(bg="red")
    winner = True
    messagebox.showinfo("Piskvorky", f"Vitazom je {symbol}")
    disable_buttons()

def b_click(b):
  global counter, player, winner
  
  if b["text"] == " ":
    if player % 2 == 1:
      b["text"] = "X"
      check_winner("X")
    else:
      b["text"] = "O"
      check_winner("O")
    
    counter += 1
    player += 1

    if (counter == 10 and not winner):
      messagebox.showinfo("Piskvorky", f"Remiza")

  else:
    messagebox.showerror("Piskvorky", "Neplatny tah")


b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="green", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
