from tkinter import*
import random
from PIL import Image,ImageTk
root=Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(background="black")

img = ImageTk.PhotoImage(Image.open("Dice.jpg"))

label1=Label(root,text="Player1",bg="#345beb",fg="white")
label1.place(relx = 0.1, rely =0.2, anchor = CENTER)
label3=Label(root,bg="#ff0000",fg="white")
label3.place(relx = 0.1, rely =0.3, anchor = CENTER)

label5=Label(root,bg="#ff7300",fg="white")
label5.place(relx = 0.5, rely =0.5, anchor = CENTER)

label2=Label(root,text="Player2",bg="#345beb",fg="white")
label2.place(relx = 0.9, rely =0.2, anchor = CENTER)
label4=Label(root,bg="#ff0000",fg="white")
label4.place(relx = 0.9, rely =0.3, anchor = CENTER)

player1_score=0
player2_score=0

def player1():
    random_no=random.randint(1,6)
    global player1_score
    label5["text"]="player1 dice score= "+str(random_no)
    player1_score=player1_score+random_no
    label3["text"]=str(player1_score)
def player2():
     random_no=random.randint(1,6)
     global player2_score
     label5["text"]="player2 dice score= "+str(random_no)
     player2_score=player2_score+random_no
     label4["text"]=str(player2_score)
   
    

button1=Button(root,image=img,command=player1,anchor = CENTER)
button1.place(relx = 0.1, rely =0.5, anchor = CENTER)

button2=Button(root,image=img,command=player2,anchor = CENTER)
button2.place(relx = 0.9, rely =0.5, anchor = CENTER)









root.mainloop()