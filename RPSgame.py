from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Game Rock Paper Scissors")
window.configure(background="black")

# Load images
image_rock1 = ImageTk.PhotoImage(Image.open("rock.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("paper.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissors.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissors.png"))

# Labels for displaying choices
label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# Labels for displaying scores
computer_score = Label(window, text="0", font=('arial', 40, "bold"), fg="red")
player_score = Label(window, text="0", font=('arial', 40, "bold"), fg="red")
player_score.grid(row=1, column=3)
computer_score.grid(row=1, column=1)

# Labels for player and computer indicators
player_indicator = Label(window, text="PLAYER", font=("arial", 40, "bold"), bg="orange", fg="blue")
computer_indicator = Label(window, text="COMPUTER", font=("arial", 40, "bold"), bg="orange", fg="blue")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

# Function to update the message label
def updateMessage(msg):
    final_message.config(text=msg)

# Function to update computer's score
def Computer_Update():
    final = int(computer_score.cget("text"))
    final += 1
    computer_score.config(text=str(final))

# Function to update player's score
def Player_Update():
    final = int(player_score.cget("text"))
    final += 1
    player_score.config(text=str(final))

# Function to check the winner
def winner_check(p, c):
    if p == c:
        updateMessage("It's a tie")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins")
            Computer_Update()
        else:
            updateMessage("Player Wins")
            Player_Update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins")
            Computer_Update()
        else:
            updateMessage("Player Wins")
            Player_Update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins")
            Computer_Update()
        else:
            updateMessage("Player Wins")
            Player_Update()

# Function to update choices and determine winner
def choice_update(a):
    choices = ["rock", "paper", "scissor"]
    choice_computer = choices[randint(0, 2)]

    if choice_computer == "rock":
        label_computer.config(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.config(image=image_paper2)
    else:
        label_computer.config(image=image_scissor2)

    if a == "rock":
        label_player.config(image=image_rock1)
    elif a == "paper":
        label_player.config(image=image_paper1)
    else:
        label_player.config(image=image_scissor1)

    winner_check(a, choice_computer)

# Button widgets
button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"),
                     bg="yellow", fg="red", command=lambda: choice_update("rock"))
button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"),
                      bg="yellow", fg="red", command=lambda: choice_update("paper"))
button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"),
                        bg="yellow", fg="red", command=lambda: choice_update("scissor"))
button_rock.grid(row=2, column=1)
button_paper.grid(row=2, column=2)
button_scissor.grid(row=2, column=3)

# Message label for displaying game results
final_message = Label(window, font=("arial", 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)

window.mainloop()