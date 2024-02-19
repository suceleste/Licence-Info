from tkinter import *
import sys

class VueMessage :
	def __init__(self, message) :
		self.Mess = message
		self.SCREEN = Tk()

	def Affichage(self) :
		label = Label(self.SCREEN, text=self.Mess)
		label.pack()
		button = Button(self.SCREEN, text="Au revoir", command=sys.exit)
		button.pack()

		self.SCREEN.mainloop()


class VueMessage2 :
	def __init__(self) :
		self.SCREEN = Tk()
		self.Mess = 'Bonjour '
		self.Input = StringVar(self.SCREEN)

	def Affichage(self) :
		self.label = Label(self.SCREEN, text=self.Mess)
		self.label.grid(column=0, row=0, columnspan=2)
		Ent = Entry(self.SCREEN, textvariable=self.Input)
		Ent.grid(column=0, row=1, columnspan=2)
		b2 = Button(self.SCREEN, text='Valider', command=self.Valider)
		b2.grid(column=0, row=2)
		button = Button(self.SCREEN, text="Au revoir", command=sys.exit)
		button.grid(column=1, row=2)

		self.SCREEN.mainloop()

	def Valider(self) :
		self.label['text'] = f'Bonjour {self.Input.get()}'

c = VueMessage2()

c.Affichage()