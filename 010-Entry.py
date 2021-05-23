import tkinter as tk

top = tk.Tk()

frametop = tk.Frame(top)
frametop.pack(side=tk.TOP)

framebtm = tk.Frame(top)
framebtm.pack(side=tk.BOTTOM, fill=tk.X)

L1 = tk.Label(frametop, text = "User Name")
L1.pack(side = tk.LEFT)

E1 = tk.Entry(frametop)
E1.pack(side = tk.RIGHT)

B1 = tk.Button(framebtm, text="show", command = lambda : print(E1.get()) )
B1.pack(fill=tk.X)

top.mainloop()
