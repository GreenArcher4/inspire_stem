import tkinter as tk


#to retrieve the student data
def submit():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    age = age_entry.get()


    print("first name :", firstname)
    print("Last name:", lastname)
    print("age:", age)
    print("---------------------------------") #this is a seperator



window = tk.Tk()
window.title("Student Data Entry Form ")

frame= tk.Frame(window)
frame.pack()

#Saving user info
student_info_frame = tk.LabelFrame(frame, text="Student info") #parent is frame
student_info_frame.grid(row=0, column = 0, padx= 20, pady= 20)

first_name_label = tk.Label(student_info_frame, text ="First Name")            # parent is student info
first_name_label.grid(row=0, column = 0)

last_name_label = tk.Label(student_info_frame, text ="Last Name")            # parent is student info
last_name_label.grid(row=1, column = 0)

first_name_entry =tk.Entry(student_info_frame)
last_name_entry =tk.Entry(student_info_frame)
first_name_entry.grid(row=0, column = 1)
last_name_entry.grid(row=1, column = 1)

age_label = tk.Label(student_info_frame, text ="Age")            # parent is student info
age_label.grid(row=2, column = 0)

age_entry =tk.Entry(student_info_frame)
age_entry.grid(row=2, column = 1)

button = tk.Button(window , text="Submit", command = submit, font=("Times New Roman", 14 ) )
button.pack(padx=15, pady=15)





for widget in student_info_frame.winfo_children():  # to space up the grids for data entry
    widget.grid_configure(padx= 10, pady = 5)



window.mainloop()
