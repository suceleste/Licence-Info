from tkinter import *
from PIL import Image, ImageTk
import sys
from random import randint

class VueDemineur :
	def __init__(self) :
		self.DIM = 20
		self.SCREEN = Tk()
		self.imageName = ["rien", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "mine"]
		self.Images = []
		self.can = Canvas(self.SCREEN, width=self.DIM*5, height=self.DIM*5)
			
		self.InitImage()

	def InitImage(self) :
		for e in self.imageName :
			self.Images.append(ImageTk.PhotoImage(Image.open("demineur/"+e+".gif")))

	def affiche(self) : 
		self.Create()

		bagain = Button(self.SCREEN, text='Recommencer', command=self.Create)
		bagain.grid(column=0, row=1)
		bexit = Button(self.SCREEN, text="Au revoir", command=sys.exit)
		bexit.grid(column=1, row= 1)

		mainloop()

	def Create(self) :
		for x in range(5) :
			for y in range(5) :
				self.can.create_image(self.DIM*x,self.DIM*y, anchor=NW, image=self.Images[randint(-1, 8)])
		self.can.grid(column=0, row=0, columnspan=2)

c = VueDemineur()

c.affiche()