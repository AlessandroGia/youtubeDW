from tkinter import *

Urlq = "p"


def getUrl():
	#Lb1 = Label(frame, text = Url.get())
	#b1.pack()

	lbl1 = Label(frame, text = "")
	lbl1.pack()

	lbl1.destroy()

	if Mp3.get() or Mp4.get():
		
		lbl1 = Label(frame, text = "Nice choice")
		lbl1.pack()
		lbD = 1

	else:

		lbl1 = Label(frame, text = "Devi inserire un formato")
		lbl1.pack()
		lbD = 1

	Urlq = Url.get()
	print(Mp3.get())
	print(Mp4.get())


root = Tk()
root.geometry('400x200')


frame = Frame(root)
frame.pack()


Url = Entry(frame, width = 30, bg = "white")
Url.pack(padx = 5, pady = 5)



Mp3 = IntVar()
Mp4 = IntVar()
 
chkBtnMp3 = Checkbutton(frame, text = "Mp3", variable = Mp3)
chkBtnMp3.pack(padx = 5, pady = 2)
 
chkBtnMp4 = Checkbutton(frame, text = "Mp4", variable = Mp4)
chkBtnMp4.pack(padx = 5, pady = 2)



button = Button(frame, text = "ciao negro", command = getUrl)
button.pack()

print(Urlq)

w = Label(root, text = 'hello world')
w.pack()

root.mainloop()