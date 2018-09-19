from Multiplayer import *
from Singleplayer import *
from Tkinter import*
import pygame,sys
from checks import *
from ships import *
import pygame,sys
import random
import Tkinter
import tkMessageBox
from pygame.locals import*
  
 # ******************************************FUNCTION FOR PLAYER V/S PLAYER *************************************************************************


def player_player():
	window.withdraw()
	if multi() == 1:
		window.deiconify()                      
 # ****************************************FUNCTION FOR PLAYER V/S COMPUTER *************************************************************************

		
def player_computer():
	 window.withdraw()
	 if single() == 1:
	 	window.deiconify()
    
 # ******************************************FUNCTIONS FOR MAIN DISPLAY *************************************************************************
 

def Rules_page():        # functon to display the rules page  
	 
	   p_v_p.place_forget()
	   p_v_s.place_forget()
	   rules_button.place_forget()
	   window.configure(background="moccasin")
	   Back_button.place(x=450,y=600)
	   Rules_label.place(x=300,y=30)
def Home_back():          # functon to bring back the home page from rules pages
	   Back_button.place_forget()
	   Rules_label.place_forget()
	   p_v_p.place(x=420,y=400)
	   p_v_s.place(x=420,y=500)
	   img.grid(row=0,column=90,padx=0,pady=0)
	   rules_button.place(x=420,y=600)
	   pic.place(x=350,y=30)

def Home_Page():     #functon to display the home page  
  start.place_forget()
  lbl.place_forget()
  p_v_p.place(x=420,y=400)
  p_v_s.place(x=420,y=500)
  rules_button.place(x=420,y=600)

 # opening Tkinter window

window=Tk()     
window.title("Battleship")
window.geometry("1020x1000")

  # setting the background 

logo=PhotoImage(file="background.png")
img=Label(window,image=logo)
img.grid(row=0,column=90)
ship_img=PhotoImage(file="Photo.png")
pic=Label(window,image=ship_img)
pic.place(x=350,y=30)

  # creating neccessary buttons

p_v_p=Button(window,text="PLAYER V/S PLAYER",command=player_player,bg="firebrick1",padx=10,pady=20)
p_v_s=Button(window,text="PLAYER V/S COMPUTER",command=player_computer,bg="firebrick1",padx=10,pady=20)
rules_button=Button(window,text="Rules",command=Rules_page,bg="firebrick1",padx=40,pady=20)
Back_button=Button(window,text="Back",command=Home_back,bg="firebrick1",padx=40,pady=20)

   # creating label to display rules in rules page              
   
Rules_label=Label(window,text="RULES:\n\nPlayers v/s Players:Each player places\nthe 5 ships somewhere on their board.The ships\ncan only be placed vertically\nor horizontally consecutively.Diagonal placement is not\nallowed.Ships may not overlap each other\n.No ships may be placed on another ship.Player's\ntake turns guessing by selecting random\npositions on the grid.The opponent responds with\nhitor miss as appropriate.A miss recorded by any player\nshifts the hitting chance to his opponent\n.When all of the squares that\nyour ships occupies have been hit,the ship will be sunk\n.Once if the player tries to makeout all the ships of\n opponentsthen he is declared as a winner\n.Player v/s Computer:\nHere compute randomly places five ships\n horizontally or vertically in a grid and player\nmust try to guess the expected positions\nof ships.Player must guess all the ships within a\nconstraint of 50 moves.If he does so he\nis declared winner,other wise loser.",font=1000,bg="cyan",padx=10,pady=40,relief=RAISED)
lbl=Label(window,text="Enjoy the Experience  of the Battleship",bg="cornflower blue",fg="blue",font=1000,relief=RAISED,padx=30,pady=30,justify=CENTER)
lbl.place(x=315,y=420)
start=Button(window,text="Start the Game",command=Home_Page,bg="springgreen2",padx=40,pady=20)
start.place(x=400,y=550)
window.mainloop()


 # **************************************************************** THE END *************************************************************************



