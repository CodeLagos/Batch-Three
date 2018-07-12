from Tkinter import *

app = Tk()
app.title("Creating a slide show")
canv = Canvas(bg = 'black', height=500, width=500)

image1 = PhotoImage(file="images/python.gif")
image2 = PhotoImage(file="images/lion.gif")
image3 = PhotoImage(file="images/tiger.gif")
image4 = PhotoImage(file="images/frog.gif")

def img1():
	image = canv.create_image(450, 50, anchor=NE, image=image1)
	
def img2():
	image = canv.create_image(450, 50, anchor=NE, image=image2)

def img3():
	image = canv.create_image(450, 50, anchor=NE, image=image3)

def img4():
	image = canv.create_image(450, 50, anchor=NE, image=image4)

var = IntVar()

R1 = Button(app, text="   1    ", command=img1, bg="red",  fg="black", font="arial 30")
R1.pack(side=LEFT)

R2 = Button(app, text="   2    ", command=img2, bg="blue", fg='white', font="arial 30")
R2.pack(side=LEFT)

R3 = Button(app, text="   4    ", command=img3, bg="yellow", font="arial 30", fg="black")
R3.pack(side=RIGHT)

R4 = Button(app, text="   3    ", command=img4, bg="darkgreen", font="arial 30", fg="white")
R4.pack(side=RIGHT)


three = Label(app, text=" What is This ?", bg="red", fg="white", font="arial 30")
three.pack(fill=X)
	
canv.pack()
app.mainloop()