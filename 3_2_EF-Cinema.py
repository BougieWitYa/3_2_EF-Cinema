python
import tkinter as tk
from tkinter import font

# Créer la fenêtre principale
window = tk.Tk()
window.title("Menu Popcorn")
window.geometry("300x300")

# les styles de police
title_font = font.Font(family="Arial", size=20, weight="bold")
label_font = font.Font(family="Arial", size=12)
button_font = font.Font(family="Arial", size=12, weight="bold")

# Créer un fond rouge pour le titre
title_label = tk.Label(window, text="Popcorn", font=title_font, bg="red", fg="white")
title_label.pack(fill=tk.X)

# Les prix
prices = {
   "Jumbo": 10.00,
   "Grande": 8.00,
   "Moyene": 6.00,
   "Petite": 4.00
}

# Créer des variables
selected_option = tk.StringVar()
total_price = tk.DoubleVar()

# Calculation avec tax
def calculate_total():
   selected_price = prices[selected_option.get()]
   total = selected_price + (selected_price * 0.13)  # Adding 13% tax
   total_price.set(total)

# Le menu de option
option_menu = tk.OptionMenu(window, selected_option, *prices.keys())
option_menu.config(font=label_font)
option_menu.pack()

# l'option et le prix sélectionnés
selected_label = tk.Label(window, textvariable=selected_option, font=label_font)
selected_label.pack()

price_label = tk.Label(window, text="Prix: $", font=label_font)
price_label.pack()

# Le button de calculation
calculate_button = tk.Button(window, text="Calculer le total", command=calculate_total, font=button_font)
calculate_button.pack()

# Le prix total
total_label = tk.Label(window, textvariable=total_price, font=label_font)
total_label.pack()

# Commencer
window.mainloop()

