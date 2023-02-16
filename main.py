from tkinter import *
from config import Config
from config import *

background = Label(root, image=background_image, bd=0)
background.pack()

class Durak(Config):
	def __init__(self):
		super().__init__()
		self.resetb.place(x=600,y=400,width=300,height=100)
		self.saveb.place(x=400,y=400,width=200,height=100)
		self.setb.place(x=0,y=400,width=200,height=100)
		self.fullset.place(x=200,y=400,width=200,height=100)

		self.forgot_list = []

		self.repair()

		root.mainloop()

	def repair(self):
		for i in range(0, len(self.button_list)):
			self.button_list[i].place(x=self.button_pos_list[i][0], y=self.button_pos_list[i][1], width=100, height=100)

	def set(self):
		num = self.forgot_list.pop(-1)
		self.button_list[num].place(x=self.button_pos_list[num][0], y=self.button_pos_list[num][1], width=100, height=100)

	def fullset(self):
		for i in self.forgot_list:
			self.button_list[i].place(x=self.button_pos_list[i][0], y=self.button_pos_list[i][1], width=100, height=100)

	def hide(self, index):
		self.forgot_list.append(index)
		self.button_list[index].place_forget()

	def save(self):
		self.forgot_list.clear()

if __name__ == '__main__':
	Durak()