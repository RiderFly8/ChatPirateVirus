from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label

# Créez une fenêtre tkinter
root = tk.Tk()
root.title("CHAT PIRATE ?!?!?!?!?!?!?!?!?!")

# Chargez l'image
image = Image.open("chatpirate.jpg")  # Remplacez "votre_image.jpg" par le chemin de votre image

# Convertissez l'image en format tkinter
tk_image = ImageTk.PhotoImage(image)

# Créez un label pour afficher l'image
label = Label(root, image=tk_image)
label.pack()

# Démarrez la boucle principale de tkinter
root.mainloop()
