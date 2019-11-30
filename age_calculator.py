# create Person class
# create init method
# 2 attributes (fullname, birthdate)
# create an object from the Person class

import datetime


import tkinter as tk #GUI
# a tk object(window is the object) has been created from the tk module
#frame is created
window = tk.Tk() #Tk is the class
window.geometry("400x400")  #geometry is a method of the Tk class - a frame is created

window.title("Age Calculater App 2020")

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)

#Entry are the inputs fields that user will use to input data
year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)

# this connects with the calculate now button
def calculate_age(): # check to see if button was actually clicked
    print(year_entry.get()) # pulls value from year
    print(month_entry.get()) # pulls value from month
    print(day_entry.get()) # pulls value from day
    
    user = Person('User', datetime.date(int(year_entry.get()),
                                        int(month_entry.get()),
                                        int(day_entry.get())))
    
    
    print(user.age())
    #print("Button was clicked!")
    text_answer = tk.Text(master=window, height=5, width=10) # how large should the text-box be
    text_answer.grid(column=1, row=5)
    answer_text = "{name} is {age} years old".format(name=user.fullname, age=user.age())
    text_answer.insert(tk.END, answer_text) #prints to the window



calculate_button = tk.Button(text="Calculate Here & Now", command=calculate_age)
calculate_button.grid(column=1, row=4)

class Person:
    def __init__(self, fullname, birthdate):
        self.fullname = fullname
        self.birthdate = birthdate
        
    #def __str__(self):
        #return "Fullname is {}, birthdate is {}".format(self.fullname, self.birthdate)
        
        

    def age(self): # method that calculates the age for user
        today = datetime.date.today()
        age = today.year - self.birthdate.year 
        return age



# Used to check if method was working
# always be testing to see if code works
#sharaine = Person("Sharaine Handsome", datetime.date(1992,10,2))

#print(sharaine.fullname)
#print(sharaine.birthdate)
#print(sharaine.age())


window.mainloop()
