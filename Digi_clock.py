import tkinter as tk

import time

clock = tk.Tk()
clock.title('Digital_Clock')

def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    
    label.config(text=current_time)
    label.after(1000, update_time)
    
label = tk.Label(clock, font=('handjet', 40, 'bold'), background='black', foreground='red')

label.pack(anchor='center')

def update_date():
    current_date = time.strftime('%D %a')
    
    label1.config(text=current_date)
    label1.after(1000, update_date)
    
label1 = tk.Label(clock, font=('handjet', 23, 'bold'), background='black', foreground='red')

label1.pack(anchor='center')


update_time()
update_date()

clock.mainloop()
