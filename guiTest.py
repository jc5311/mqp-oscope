import Tkinter as tk

window = tk.Tk() #create TK object as window

window.title("RasPi_Scope")

#funcs
def say_something():
	name = str(entry_field1.get())

	#create text field
	phrase_display = tk.Text(master=window, height=10, width=30)
	#position it
	phrase_display.grid(row=3, column=2)
	phrase_display.insert(tk.END, name)

#window properties
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(str(width) + 'x' + str(height)) #set window size to dims of screen
#window.geometry("400x400")
#label
title = tk.Label(text="Enter your name", font=("Times New Roman", 20))
title.grid(row=0, column=0)
#entry field
entry_field1 = tk.Entry()
entry_field1.grid(row=2, column=1)
#button
button1 = tk.Button(text="Click me!", font=("Arial", 20), bg="red", command = say_something)
button1.grid(row=1, column=1)

#show screen
window.mainloop() #run the window?
