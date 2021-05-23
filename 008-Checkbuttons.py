import tkinter as tk

top = tk.Tk()

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()

def getChoiceText () :
  reVal = ""
  if CheckVar1.get() == 1 and \
     CheckVar2.get() == 1 :
    reVal = "Music and Video"
  elif CheckVar1.get() == 1 :
    reVal = "Music only"
  elif CheckVar2.get() == 1 :
    reVal = "Video only"
  else :
    reVal = "Nothing"
  return reVal

chk1 = tk.Checkbutton(top,
                      text = "Music",
                      variable = CheckVar1)
chk1.pack()

chk2 = tk.Checkbutton(top,
                      text = "Video",
                      variable = CheckVar2)
chk2.pack()

btn = tk.Button(top,
                text = "Print Choice",
                command = lambda :
                    print( getChoiceText() ))
btn.pack()

top.mainloop()
