import tkinter as tk
from tkinter import messagebox

# Créez une fenêtre tkinter (invisible)
root = tk.Tk()
root.withdraw()

# Affichez une boîte de dialogue d'erreur
messagebox.showerror("Error", "Le chat pirate a detruit ton pc lol.")

# Fermez la fenêtre tkinter
root.destroy()
