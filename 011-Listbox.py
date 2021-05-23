import tkinter as tk
import tkinter.messagebox as msg

defaultOptions = ("Tomatoes", "Bellpeppers", "Eggplants", "Broccoli", "Corn",
                  "Arugula", "Olives", "Onions", "Chilies", "Mushrooms",
                  "Artichokes", "Mozzarella", "Gorgonzola")

# numerical constants: describe width and height of the interface
N = len(defaultOptions)
W = 6

top = tk.Tk()
top.title("Order your custom pizza!")

buttons = []
for i, ingredient in enumerate(defaultOptions) :
    buttons.append(tk.Button(
        top,
        text = ingredient,
        command = lambda c=i: lst.insert(tk.END, buttons[c]["text"])
    ))
    buttons[i].grid(
        column = 0, row = i,
        columnspan = W,
        sticky = "WE"
    )


txt = tk.Entry (top)
txt.grid(
    column = 0, row = N,
    columnspan = W - 1
)

tk.Button(
    top,
    text = ">",
    command = lambda : lst.insert(tk.END, txt.get())
).grid(column = W - 1, row = N)

lst = tk.Listbox(top, height = 2*N)
lst.grid(column = W + 1, row = 0, rowspan=N)

tk.Button(
    top,
    text = "remove",
    command = lambda :
        lst.delete(*lst.curselection()) if len(lst.curselection()) else None
).grid(
    column = W + 1, row = N,
    sticky = "WE"
)

def getOrderText () :
    reVal = "One pizza with"
    if lst.size() == 0 :
        reVal += " nothing"
    else :
        for ID in range(lst.size()) :
            reVal += "\n* " + lst.get(ID)
    return reVal

def orderMsgBox () :
    msg.showinfo("your Order", getOrderText())
    top.destroy()

tk.Button(
    top,
    text = "Order!",
    command = orderMsgBox
).grid(
    column = 0, row = N + 1,
    columnspan = W + 2,
    sticky = "WE"
)

top.mainloop()
