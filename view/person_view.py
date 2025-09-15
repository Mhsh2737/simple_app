from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from tools.validation import *
from data_access.database_manager import save_parking
import datetime



def save_click():
    try:
        name_validator(name.get())
        model_validator(model.get())
        plate_validator(plate.get())
        save_parking(name.get(),model.get(),plate.get(),color.get())
        msg.showinfo("Saved", "Parking Saved")
    except Exception as e:
        e.with_traceback()
        msg.showerror("error",f"{e}")

window = Tk()

window.title("Public Parking")
window.geometry("500x300")

#name
name = StringVar()
Label(window, text="Name",bg="dark blue",fg="white").place(x=27,y=30)
Entry(window,textvariable=name,width=24).place(x=100,y=30)

#model
model = StringVar()
Label(window, text="Model",bg="dark blue",fg="white").place(x=27,y=70)
Entry(window,textvariable=model,width=24).place(x=100,y=70)

#plate
plate = StringVar()
Label(window, text="Plate",bg="dark blue",fg="white").place(x=27,y=110)
Entry(window,textvariable=plate,width=24).place(x=100,y=110)

#color
color = StringVar(value="white")
Label(window, text="Color",bg="dark blue",fg="white").place(x=27,y=150)
ttk.Combobox(
    window,
    values = ["white","black","red"],
    width=21,
    textvariable=color,
    state="readonly"
).place(x=100,y=150)

#date time
#current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#datetime.set(current_time)

datetime = StringVar(value=datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))
Label(window, text="datetime",bg="dark blue",fg="white").place(x=27,y=190)
Entry(window,textvariable=datetime,width=24,state="readonly").place(x=100,y=190)

Button(window, text="Save",bg="dark blue",fg="white",width=9,command=save_click).place(x=100,y=250)

window.mainloop()
