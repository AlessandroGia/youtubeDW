from tkinter import *
from tkinter import filedialog
import subprocess
import threading
import time

global thread_stop

root = Tk()
root.geometry('400x200')
root.title('YutubeDW')

frame = Frame(root, width = 1000, height = 400)
frame.pack()

frame2 = Frame(frame)
frame2.pack()

frame3 = Frame(frame)
frame3.pack()

frame4 = Frame(frame)
frame4.pack()

frame5 = Frame(frame)
frame5.pack()

def threadCaricamento():

	global thread_stop

	while True:

		if not thread_stop:
			break
		lbl1["text"] = "Caricamento."
		if not thread_stop:
			break
		time.sleep(1)
		if not thread_stop:
			break
		lbl1["text"] = "Caricamento.."
		if not thread_stop:
			break
		time.sleep(1)
		if not thread_stop:
			break
		lbl1["text"] = "Caricamento..."
		if not thread_stop:
			break
		time.sleep(1)
		if not thread_stop:
			break

def threadScarica(command):

	global thread_stop

	ErrLvl = 0

	commandSplit = command.split('*')

	for cmd in commandSplit:

		process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)

		output, error = process.communicate()

		thread_stop = False

		if error:

			ERR = "is not a valid URL" in format(error)
			if ERR:
				ErrLvl = 1
				break

			ERR = "Unable to extract video data"  in format(error)
			if ERR:
				ErrLvl = 2
				break

			ERR = "looks truncated" in format(error)
			if ERR:
				ErrLvl = 3
				break

		if output:

			Out = "Deleting original file" in format(output)
			if Out:
				ErrLvl = 4
				

		btnScarica["state"] = 'normal'

		print("Output:" + format(output))
		print("Error:" + format(error))

	thread_stop = False
	time.sleep(1)

	if ErrLvl == 1:
		lbl1["text"] = "L'Url non e' valido"

	if ErrLvl == 2:
		lbl1["text"] = "L'Url e' sbagliato"

	if ErrLvl == 3:
		lbl1["text"] = "L'Url e' incompleto"

	if ErrLvl == 4:
		lbl1["text"] = "Download completato"



def scarica():

	global thread_stop

	cmd = []

	btnScarica["state"] = 'disable'

	thread_stop = True

	caricamThr = threading.Thread(target = threadCaricamento, args = (), daemon = True)
	caricamThr.start()

	UrlVid = Url.get()


	DirDest = root.directory + "/"
	#DirDest = D.replace("/", "//")
	Dirr = '"' + DirDest + "/%(title)s.%(ext)s" + '"'

	if Mp3.get():

		command = "youtube-dl --extract-audio --audio-format mp3 -o" + " " + Dirr + " " + Url.get()
		cmd.append(command)

	if Mp4.get():

		if Mp3.get():

			command = "youtube-dl -f mp4 -o" + " " + Dirr + " " + Url.get()
			cmd.append(command)

	for comm in cmd:
		
		scaricaThr = threading.Thread(target = threadScarica, args = (comm,), daemon = True)
		scaricaThr.start()



def sfoglia():

	root.directory = filedialog.askdirectory()

	lblDirDest["text"] = root.directory

def getUrl():
	#Lb1 = Label(frame2, text = Url.get())
	#b1.pack()


	if Mp3.get() or Mp4.get():

		if lblDirDest["text"] != "":

			scarica()

		else:

			lbl1["text"] = 'Devi inserire un percorso'

		
		#lbl1 = Label(frame2, text = "Nice choice")
		#lbl1.pack()vet

	else:

		lbl1["text"] = 'Devi inserire un formato'

		#lbl1 = Label(frame2, text = "Devi inserire un formato")
		#lbl1.pack()

	Urlq = Url.get()

lbl1 = Label(frame2, text = "")
lbl1.pack()


Url = Entry(frame2, width = 35,  bg = "white", justify = CENTER, bd = 2, fg = 'blue', font = 'times-new-roman')
Url.pack(padx = 5, pady = 5)


Mp3 = IntVar()
Mp4 = IntVar()


btnSfoglia = Button(frame3, text = "Sfoglia", command = sfoglia)
btnSfoglia.pack(side = LEFT, padx = 5, pady = 8)

lblDirDest = Label(frame3, text = "")
lblDirDest.pack(side = LEFT, padx = 5, pady = 8)


chkBtnMp3 = Checkbutton(frame4, text = "Mp3", variable = Mp3)
chkBtnMp3.pack(side = LEFT)
 
chkBtnMp4 = Checkbutton(frame4, text = "Mp4", variable = Mp4)
chkBtnMp4.pack(side = LEFT)


btnScarica = Button(frame5, text = "Scarica", width = 25, height = 2, command = getUrl)
btnScarica.pack( padx = 5, pady = 8)


root.mainloop()