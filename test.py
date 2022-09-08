from curses import BUTTON2_PRESSED
from distutils.cmd import Command
import random
from tkinter import *
from random import randint
from tkinter import ttk
import tkinter as tk
from functools import partial
import time


root = Tk() # fixa detta

root.title("sten, sax, påse")
root.geometry("500x600")

root.config(bg="white")


#button1 = tk.Button(text="       Rock       ",bg="skyblue",command=rock)

ssp = ["sten", "sax", "påse"]

mit_val = ""

val = random.choice(ssp)
    #time.sleep(1)

if mit_val not in ssp:
    label = ttk. Label(root, text="Välj sten sax eller påse")

if val == mit_val:
            
            label = ttk. Label(root, text=f"Du tog {mit_val} och datorn tog {val} så det blir lika")
elif mit_val == "sten":
            if val == "sax":
                label.config
            else:
                label.config

elif mit_val == "sten":
            if val == "sax":
                label.config
            else:
                label.config

elif mit_val == "påse":
            if val == "sten":
                label.config
            else:
                label.config

def make_val(val):
        mit_val = val


button1 = tk.Button(text="Sten", bg="skyblue", command=partial(make_val, "sten"))
button1.pack()

button1 = tk.Button(text="Sten", bg="skyblue", command=partial(make_val, "sax"))
button1.pack()

button1 = tk.Button(text="Sten", bg="skyblue", command=partial(make_val, "påse"))
button1.pack()

label = ttk.Label(root)
label.pack()
label.config(text="sten")


