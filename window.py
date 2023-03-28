from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import lab3 as cryp

loadpath = '' 
class Win:

	def crypt_file(self):
		filename = askopenfilename()
		if filename:
			loadpath = filename
		else:
			messagebox.showwarning("Key error", "Cannot to open file")
		self.textFieldOut.delete(1.0, END)
		p = int(self.textKey.get())
		q = int(self.textQ.get())
		b = int(self.textB.get())
		try:
			cryp.check_keys(p,q,b)
			if loadpath == "":
				messagebox.showwarning("Key error", "Choose file")
			else:
				result = cryp.Encrypt(loadpath, p, q, b)
				self.textFieldIn.delete(1.0, END)
				self.textFieldIn.insert(1.0, result[0])
				self.textFieldOut.delete(1.0, END)
				self.textFieldOut.insert(1.0, result[1])

		except ValueError as err:
			messagebox.showwarning("Key error", str(err))

		


	def decrypt_file(self):
		filename = askopenfilename()
		if filename:
			loadpath = filename
		else:
			messagebox.showwarning("Key error", "Cannot to open file")
		self.textFieldOut.delete(1.0, END)
		p = int(self.textKey.get())
		q = int(self.textQ.get())
		b = int(self.textB.get())
		try:
			cryp.check_keys(p,q,b)
			if loadpath == "":
				messagebox.showwarning("Key error", "Choose file")
			else:
				result = cryp.Decrypt(loadpath, p, q, b)
				self.textFieldIn.delete(1.0, END)
				self.textFieldIn.insert(1.0, result[0])
				self.textFieldOut.delete(1.0, END)
				self.textFieldOut.insert(1.0, result[1])

		except ValueError as err:
			messagebox.showwarning("Key error", str(err))

	def clear(self):
		self.textFieldIn.delete(1.0, END)
		self.textFieldOut.delete(1.0, END)

	def __init__(self, width, height, title='Cipher'):
		self.color = '#c0c0c0'

		self.root = Tk()
		self.root['bg'] = self.color  # цвет фона
		self.root.title(title)
		self.root.geometry(f'{width}x{height}')

		self.frame = Frame(self.root, bg=self.color)  # frame fot textFiledIn
		self.frame1 = Frame(self.root, bg=self.color)

		self.entryFrame = Frame(self.root, bg=self.color)
		self.entryFrame1 = Frame(self.root, bg=self.color)
		self.entryFrame2 = Frame(self.root, bg=self.color)

		self.txtFrame = Frame(self.root, bg=self.color)
		self.txtFrame1 = Frame(self.root, bg=self.color)
		self.txtFrame2 = Frame(self.root, bg=self.color)
		self.txtFrame3 = Frame(self.root, bg=self.color)
		self.txtFrame4 = Frame(self.root, bg=self.color)
		
		self.btnFrame = Frame(self.root, bg=self.color)
		self.btnFrame1 = Frame(self.root, bg=self.color)
		self.btnFrame2 = Frame(self.root, bg=self.color)

		self.textFieldIn = Text(self.frame, height=30, width=35, font='Consolas 15', wrap=WORD)
		self.textFieldOut = Text(self.frame1, height=30, width=35, font='Consolas 15', wrap=WORD)
		self.textKey = Entry(self.entryFrame,  font='Consolas 15')
		self.textQ = Entry(self.entryFrame1,  font='Consolas 15')
		self.textB = Entry(self.entryFrame2,  font='Consolas 15')

		self.lblTextIn = Label(self.txtFrame, text='Plain File', font="Cosolas 20", bg=self.color, fg='black')
		self.lblTextOut = Label(self.txtFrame1, text='Ciphed File', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey = Label(self.txtFrame2, text='p', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey1 = Label(self.txtFrame3, text='q', font="Cosolas 20", bg=self.color, fg='black')
		self.lblKey2 = Label(self.txtFrame4, text='b', font="Cosolas 20", bg=self.color, fg='black')
		

		self.btnEcnrypt = Button(self.btnFrame, height=2, width=8, text="Encrypt", font="Consalas 20",
								 command=self.crypt_file)
		self.btnDecrypt = Button(self.btnFrame1, height=2, width=8, text="Decrypt", font="Consalas 20",
								 command=self.decrypt_file)
		self.btnLoadFile = Button(self.btnFrame2, height=2, width=10, text="Clear", font="Consalas 20",
								  command=self.clear)
		
		

	def draw_win(self):
		self.txtFrame.place(x=70, y=20, width=200, height=30)
		self.txtFrame1.place(x=400, y=20, width=200, height=30)
		self.txtFrame2.place(x=700, y=20, width=200, height=30)
		self.txtFrame3.place(x=700, y=90, width=200, height=30)
		self.txtFrame4.place(x=700, y=160, width=200, height=30)

		
		self.frame.place(x=25, y=50, width=300, height=350)
		self.frame1.place(x=355, y=50, width=300, height=350)

		self.entryFrame.place(x=695, y=50, width=300, height=30)
		self.entryFrame1.place(x=695, y=120, width=300, height=30)
		self.entryFrame2.place(x=695, y=190, width=300, height=30)

		self.btnFrame.place(x=740, y=250, width=90, height=50)
		self.btnFrame1.place(x=865, y=250, width=90, height=50)
		self.btnFrame2.place(x=740, y=320, width=200, height=50)

		self.textFieldIn.pack()
		self.textFieldOut.pack()
		self.textKey.pack()
		self.textQ.pack()
		self.textB.pack()
		

		self.lblTextIn.pack()
		self.lblTextOut.pack()
		self.lblKey.pack()
		self.lblKey1.pack()
		self.lblKey2.pack()
		
		self.btnEcnrypt.pack()
		self.btnDecrypt.pack()
		self.btnLoadFile.pack()
		



	def run(self):  # запуск стартового окна
		self.draw_win()
		self.root.mainloop()


window = Win(1000, 500)
window.run()