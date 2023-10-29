import tkinter as tk
import random

#win
win = tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("400x300")

#font
title_font = ("Arial", 13, "bold")
button_font = ("Arial", 9, "bold")
resoult_font = ("Arial", 12, "bold")
choose_font = ("Arial", 10, "bold")

#label1
label1 = tk.Label(win, text="You                   Opponent", font=title_font)
label1.pack()

#Selected button label
#player
y_selected_label = tk.Label(text="", font=choose_font)
y_selected_label.place(x="30", y="250")

#opponent
o_selected_label = tk.Label(text="", font=choose_font)
o_selected_label.place(x="300", y="250")

#resoult label
resoult = tk.Label(font=resoult_font)
resoult.place(x="150", y="250")
#o_choose
o = ["rock", "scissors", "paper"]
o_choose = random.choice(o)

#rock function
def y_ro_button():
    y_choose = "rock"
    y_selected_label.config(text="Rock")
    
    o_choose = random.choice(o)
    o_selected_label.config(text=o_choose)
    
    if o_choose == "rock":
        resoult.config(text="Parity")
        
    elif o_choose == "scissors":
        resoult.config(text="You win")
       
    elif o_choose == "paper":
        resoult.config(text="You lose")

#scissors function
def y_sc_button():
    y_choose = "scissors"
    y_selected_label.config(text="Scissors")
    
    o_choose = random.choice(o)
    o_selected_label.config(text=o_choose)
    
    if o_choose == "rock":
        resoult.config(text="You lose")
        
    elif o_choose == "scissors":
        resoult.config(text="Parity")
       
    elif o_choose == "paper":
        resoult.config(text="You win")

#paper function
def y_pa_button():
    y_choose = "paper"
    y_selected_label.config(text="Paper")
    
    o_choose = random.choice(o)
    o_selected_label.config(text=o_choose)
    
    if o_choose == "rock":
        resoult.config(text="You win")
        
    elif o_choose == "scissors":
        resoult.config(text="You lose")
       
    elif o_choose == "paper":
        resoult.config(text="Parity")



        

#player buttons
#rock
y_rock_button = tk.Button(win, text="Rock", font=button_font, command=y_ro_button)
y_rock_button.config(height="2", width="10")
y_rock_button.place(x="6", y="70")
#scissors
y_scissors_button = tk.Button(win, text="Scissors", font=button_font, command=y_sc_button)
y_scissors_button.config(height="2", width="10")
y_scissors_button.place(x="6", y="120")
#paper
y_paper_button = tk.Button(win, text="Paper", font=button_font, command=y_pa_button)
y_paper_button.config(height="2", width="10")
y_paper_button.place(x="6", y="170")













win.mainloop()