from tkinter import *

root = Tk()

root.geometry("500x500")
label = Label(root, text="Employee ID:")

label.pack()



userID_textBox = Entry(root)
userID_textBox.pack()

buttonFrame = Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = Button(buttonFrame, text="1", )
btn1.grid(row=0, column=0, sticky=W+E)
btn2 = Button(buttonFrame, text="2", )
btn2.grid(row=0, column=1, sticky=W+E)
btn3 = Button(buttonFrame, text="3", )
btn3.grid(row=0, column=2, sticky=W+E)
btn4 = Button(buttonFrame, text="4", )
btn4.grid(row=1, column=0, sticky=W+E)
btn5 = Button(buttonFrame, text="5", )
btn5.grid(row=1, column=1, sticky=W+E)
btn6 = Button(buttonFrame, text="6", )
btn6.grid(row=1, column=2, sticky=W+E)
btn7 = Button(buttonFrame, text="7", )
btn7.grid(row=2, column=0, sticky=W+E)
btn8 = Button(buttonFrame, text="8", )
btn8.grid(row=2, column=1, sticky=W+E)
btn9 = Button(buttonFrame, text="9", )
btn9.grid(row=2, column=2, sticky=W+E)
btn0 = Button(buttonFrame, text="0", )
btn0.grid(row=3, column=1, sticky=W+E)
# clock_in_button.pack()


buttonFrame.pack(fill="x")
# clock_out_button.pack()
root.mainloop()