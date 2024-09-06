import tkinter as tk
from tkinter import messagebox
import os

def shutdown_pc():
    confirm = messagebox.askokcancel("Confirm Shutdown", "Are you sure you want to shut down your PC?")
    if confirm:
        os.system("shutdown /s /f /t 1")

root = tk.Tk()
root.title("PC_Shutdown")

shutdown_button = tk.Button(root, text="Shutdown PC", command=shutdown_pc,font=('sans serif', 20, 'bold'), background='white', foreground='red').pack(padx=25, pady=25)

root.mainloop()
