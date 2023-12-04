from tkinter import *



# label.pack()

userID = ''
def addToUserBox(symbol):
    global userID
    userID += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, userID)




#(button = Frame(root)
#(root.columnconfigure(0, weight=1)
#(root.columnconfigure(1, weight=1)
#(root.columnconfigure(2, weight=1)


# clock_in_button.pack()


#(root.pack(fill="x")
# clock_out_button.pack()\
root = Tk()

root.geometry("500x500")
label = Label(root, text="Employee ID:")

text_result = Text(root, height=2, width=26)
text_result.grid(columnspan=5)

btn1 = Button(root, text="1",command= lambda: addToUserBox(1), width=10 )
btn1.grid(row=2, column=0, sticky=W+E)
btn2 = Button(root, text="2", command= lambda: addToUserBox(2), width=10)
btn2.grid(row=2, column=1, sticky=W+E)
btn3 = Button(root, text="3",command= lambda: addToUserBox(3), width=10)
btn3.grid(row=2, column=2, sticky=W+E)
btn4 = Button(root, text="4",command= lambda: addToUserBox(4), width=10)
btn4.grid(row=3, column=0, sticky=W+E)
btn5 = Button(root, text="5",command= lambda: addToUserBox(5), width=10)
btn5.grid(row=3, column=1, sticky=W+E)
btn6 = Button(root, text="6",command= lambda: addToUserBox(6), width=10)
btn6.grid(row=3, column=2, sticky=W+E)
btn7 = Button(root, text="7",command= lambda: addToUserBox(7), width=10)
btn7.grid(row=4, column=0, sticky=W+E)
btn8 = Button(root, text="8",command= lambda: addToUserBox(8), width=10 )
btn8.grid(row=4, column=1, sticky=W+E)
btn9 = Button(root, text="9",command= lambda: addToUserBox(9), width=10)
btn9.grid(row=4, column=2, sticky=W+E)
btn0 = Button(root, text="0",command= lambda: addToUserBox(0), width=10)
btn0.grid(row=5, column=1, sticky=W+E)
root.mainloop()