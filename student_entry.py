'''
            _                                                                     
           | |                                                                    
  ___ _   _| |__   ___ _ __   _ __  _ __ ___   __ _ _ __ __ _ _ __ ___   ___ _ __ 
 / __| | | | '_ \ / _ \ '__| | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \ / _ \ '__|
| (__| |_| | |_) |  __/ |    | |_) | | | (_) | (_| | | | (_| | | | | | |  __/ |   
 \___|\__, |_.__/ \___|_|    | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|\___|_|   
       __/ |                 | |               __/ |                              
      |___/                  |_|              |___/                               

      
                                    Assalamu alaikum  ❤
                                This is not any hacking tool 
                        This is a gui project.(student form project)

                    Owner    : Md siFaT isLaM
                    fb       : https://www.facebook.com/root.lovs
                    telegram : @root_lovs

     If you want to make this type's of project's so please contact with  me..........

'''



from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Data Entry project')
root.resizable(False,False)


def data_entry():
    # -------- Get data----------#
    first_name = F_name_entry_box.get()
    last_name = S_name_entry_box.get()

    age = age_Spinbox.get()

    nationality = combo_ns.get()

    clas = class_combo.get()

    rool = Rool_entry_box.get()

    subject = subject_combo.get()

    #---------Outpute Data--------------#

    data = f'''
    First name : {first_name}
    Last name : {last_name}
    Age        : {age}
    Nationality: {nationality}
    Class      : {clas}
    Rool       : {rool}
    Subject    : {subject}

    '''
    if first_name:
        pass
    elif last_name:
        print(data)
        
    else:
        print('Eroor')
    



frame = Frame(root)
frame.pack()

# User info fraim
user_info_fraim = LabelFrame(frame,text='User Info')
user_info_fraim.grid(row=0,column=0,padx=20,pady=20)

# Name Text
first_name_lable = Label(user_info_fraim,text="First Name")
first_name_lable.grid(row=0,column=0)

second_name_lable = Label(user_info_fraim,text='Second Name')
second_name_lable.grid(row=0,column=1)

# Name entry box
F_name_entry_box = Entry(user_info_fraim)
F_name_entry_box.grid(row=1,column=0)

S_name_entry_box = Entry(user_info_fraim)
S_name_entry_box.grid(row=1,column=1)

# Age lable

age_lable = Label(user_info_fraim,text='Age')
age_lable.grid(row=2,column=0)

age_Spinbox = Spinbox(user_info_fraim,from_=10,to=100)
age_Spinbox.grid(row=3,column=0)

# Nationality

ns_lable = Label(user_info_fraim,text='Nationality')
ns_lable.grid(row=2,column=1)

combo_ns = ttk.Combobox(user_info_fraim,values=['Bangladeshi','Indian','Pakistani','Saudi','Russian','Serbian','Korean','Spanish','Turkish','American '])
combo_ns.grid(row=3,column=1)




#------------------Second Fraim------------------#


student_details_fraim = LabelFrame(frame,text='Student info')
student_details_fraim.grid(row=1,column=0,padx=20,pady=20)

# Class

Class_lable = Label(student_details_fraim,text='Class')
Class_lable.grid(row=0,column=0)

class_combo = ttk.Combobox(student_details_fraim,values=['1','2','3','4','5','6','7','8','9','10'])
class_combo.grid(row=1,column=0)


# Rool 

Rool_lable = Label(student_details_fraim,text='Student Rool')
Rool_lable.grid(row=0,column=1)

Rool_entry_box = Spinbox(student_details_fraim,from_=1,to=100)
Rool_entry_box.grid(row=1,column=1)

# Subject
subject_lable = Label(student_details_fraim,text='Subject')
subject_lable.grid(row=2,column=0)

subject_combo = ttk.Combobox(student_details_fraim,values=['science','arts','commerce'])
subject_combo.grid(row=3,column=0)



#------------------Button ( last )------------------#



btn = Button(frame,text='Entry',bg='#262829',fg='#a8a7a4',command=data_entry)
btn.grid(row=2,column=0,sticky='news',padx=20,pady=20)


root.mainloop()
