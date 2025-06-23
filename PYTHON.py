import serial
import time
import tkinter as tk
from tkinter import messagebox

# Cambia la porta COM con quella del tuo Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # Aspetta che la seriale si stabilizzi
except:
    arduino = None
    print("Errore: Arduino non connesso")

def led_on():
    if arduino:
        arduino.write(b'1')
    else:
        messagebox.showerror("Errore", "Arduino non connesso")

def led_off():
    if arduino:
        arduino.write(b'0')
    else:
        messagebox.showerror("Errore", "Arduino non connesso")

root = tk.Tk()
root.title("Controllo LED Arduino")

btn_on = tk.Button(root, text="Accendi LED", command=led_on, width=20, bg="green", fg="white")
btn_on.pack(pady=10)

btn_off = tk.Button(root, text="Spegni LED", command=led_off, width=20, bg="red", fg="white")
btn_off.pack(pady=10)

root.mainloop()
