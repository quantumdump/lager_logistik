from tkinter import *
from tkinter import ttk
import sqlite3
#connect to db##########################
conn=sqlite3.connect('warehouse.db')

c = conn.cursor()
######################################
#Init Tkinter
window = Tk()
window.title("SEP logistik AG - Since 1980")
#window.iconbitmap('logo.ico')
window.geometry("600x500")

#tabs############################################################################
tab_system = ttk.Notebook()
tab_system.pack(pady=30)

#fn to navigate to Warehouse View
def get_to_warehouse_view():
    tab_system.select(1)

    

frame_a = Frame(tab_system, width="600", height="500", bg="grey")
frame_b = Frame(tab_system, width="600", height="500", bg="red")
frame_c = Frame(tab_system, width="600", height="500", bg="blue")

frame_a.pack(fill="both", expand=1)
frame_b.pack(fill="both", expand=1)
frame_c.pack(fill="both", expand=1)

tab_system.add(frame_a, text="General")
tab_system.add(frame_b, text="Warehouse 2d view")
tab_system.add(frame_c, text="Location")
###################################################################################
#Button to get to Warehouse view
warehouse_button = Button(frame_a, text="Warehouse View", command=get_to_warehouse_view).pack(pady=20)
#Canvas
warehouse_canvas = Canvas(frame_b, width="290", height="440", bg="black")
warehouse_canvas.pack()
#Create shelf rack

c.execute("SELECT * FROM shelf_racks")
all_racks = c.fetchall()
print(all_racks)
for rack in all_racks:
    
    warehouse_canvas.create_rectangle(rack[3]*10,rack[4]*10,rack[5]*10,rack[6]*10, fill="red" )
    
conn.commit()
conn.close()




#run the mainloop
window.mainloop()