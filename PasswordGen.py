import random
import tkinter

# initializing GUI
main_window=tkinter.Tk()
main_window.title("Password Generator")
main_window.geometry('300x300')

padd = 50
main_window['padx'] = padd # "padx" is the external padding on each side of the slave widget

# Reads integer variable from each checkbox
chk1=tkinter.IntVar()
chk2=tkinter.IntVar()
chk3 = tkinter.IntVar()
chk4 = tkinter.IntVar()

# Using the library 'random' to generate random characters

def password_gen(len):
    chars = "abcdefghajklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`\[]-=#,./?><~@:}{+_|¬!£$%^&*()"
    password = "".join(random.sample(chars, len))
    display_result.delete(0,tkinter.END)
    display_result.insert(0, password)
        
#Assigning each checkbox to desired number of characters
   
def checkbox_check():
    if chk1.get()==6:
        password_gen(6)  # Generate 6 Character Password      
    elif chk2.get()==10:
        password_gen(10) # Generate 10 Character Password      
    elif chk3.get()==12:
        password_gen(12) # Generate 12 Character Password 
    elif chk4.get()==16:
        password_gen(16) # Generate 16 Character Password       
    else:
        password_gen(8)  # Generate 8 Character Password if no Checkbox is clicked  

    
# Creating Textbox, Checkbox and Buttons

title_text=tkinter.Label(text= 'Password Generator')
title_text.grid(row=0, column = 0)

display_result=tkinter.Entry()
display_result.grid(row = 1, column=0)

chkone=tkinter.Checkbutton(text= '6 Character', onvalue=6, offvalue=0, variable=chk1)
chkone.grid (row = 2, column = 0)

chktwo=tkinter.Checkbutton(text= '10 Character', onvalue=10, offvalue=0, variable=chk2)
chktwo.grid (row = 3, column = 0)

chkthree=tkinter.Checkbutton(text= '12 Character', onvalue=12, offvalue=0, variable=chk3)
chkthree.grid (row = 4, column = 0)

chkfour=tkinter.Checkbutton(text= '16 Character', onvalue=16, offvalue=0, variable=chk4)
chkfour.grid (row = 5, column = 0)

pass_generate= tkinter.Button(text= 'Generate', command=checkbox_check)
pass_generate.grid(row = 6, column = 0)

main_window.mainloop()


            