from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

"""
Label
"""

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0) # To include to the screen
# my_label.pack("left") # To include to the screen and move it to the left

"""
Another approach to set text in label
"""
my_label["text"] = 'Heyooo'
my_label.config(text="hooooo")

"""
Button Implementation
"""
def button_click_listener():
    my_label["text"] = input.get()

button = Button(text="Click Me", command=button_click_listener)
button.grid(row=1, column=1)
button.config(pady=0, padx=10)

#Entries
entry = Entry(width=30)
'''
Add some text to begin with
END -> represent ends of char, cursor will start at end of the hint
0 -> represents start of char, cursor will start at start of the hint
'''
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(row=2, column=3)

button = Button(text="New Button")
button.grid(row=0, column=2)



"""
Layout Manager
Pack, Grid, Place
"""



# TO maintain screen
window.mainloop()