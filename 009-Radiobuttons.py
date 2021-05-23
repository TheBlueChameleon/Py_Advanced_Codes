import tkinter as tk

top = tk.Tk()

optionL = tk.IntVar()
optionR = tk.IntVar()
optionC = tk.IntVar()

rows = 5

getChoiceText = lambda : chr(optionL.get() + 65) + str(optionR.get())  + "\n" + str(optionC.get())

for i in range(rows) :
    tk.Radiobutton(
        text=chr(i + 65),
        variable=optionL,
        val=i % 2
    ).grid(
        row=i,
        column=0
    )

for i in range(rows) :
    tk.Radiobutton(
        text=str(i),
        variable=optionR,
        val=i
    ).grid(
        row=i,
        column=1
    )

tk.Button(
    text="Print Choice",
    command = lambda : print( getChoiceText() )
).grid(
    row=rows,
    column=0,
    columnspan=2
)

chk = tk.Checkbutton(top, variable=optionC)
chk.grid(row=rows+1)

#chk.select()
#optionC.set(1)

print( optionC.get() )


top.mainloop()
