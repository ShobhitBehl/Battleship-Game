
import pygame,sys
from checks import *
from ships import *
def multi():
	def display_invalid(): 										#Function for popup if invalid block is selected for placement or attacking
		root = tk.Tk()
		root.withdraw()
		tkMessageBox.showinfo("Message", "Sorry, Invalid block")
		root.update()

	def fill_yellow(x,y,rect1):									#Function to display a yellow filled block if valid block is selected for placing ship
		rect1.append([x,y])
	 	pygame.draw.rect(screen,yellow,(x*50,y*50,50,50))
		pygame.display.update()

	def place_ship(ctr,rect,rect1,count,length):				#Function to place a ship in selected block if valid, using various checks impoted from module checks
		flag2 = 0
		[x,y] = pygame.mouse.get_pos()
		x = (x/50)
		y = (y/50)
		if check_if_in_box(ctr,x,y) == 1:
			flag2 = 1
		if check_if_ship_present(ctr,x,y,rect,rect1) == 1:
			flag2 = 1
		if count<length and flag2 == 0:
			if count == 0:
				if check_if_can(ctr,x,y,rect,rect1,length,count) == 1:
					flag1 = 1
					display_invalid()
				else:
					flag1 = 0
			if count == 1:
				flag1 = 0
				if  check_if_valid(x,y,rect1) == 1:
					if check_if_can(ctr,x,y,rect,rect1,length,count) == 1:
						flag1 = 1
						display_invalid()
					else:
						flag1 = 0
				else:
					display_invalid()
					flag1 = 1
			if count>1:
				if check_orientation(rect1[0],rect1[1]) == 0:
					if check_if_horizontal(x,y,rect1,count) == 1:
						flag1 = 0
					else:
						flag1 = 1
						display_invalid()
				else:
					if check_if_vertical(x,y,rect1,count) == 1:
						flag1 = 0
					else:
						flag1 = 1
						display_invalid()
			if flag1 == 0:
				fill_yellow(x,y,rect1)
				return 1
		return 0
	# Setting up of display - Start
	black = (0,0,0)
	white = (255,255,255)
	yellow = (255,255,0)
	green = (0,255,0)
	red = (255,0,0)
	pygame.mixer.pre_init(4410,16,2,4096)
	pygame.init()
	pygame.mixer.music.load("music.mp3")
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)
	background = pygame.Rect(0,0,0,0)
	screen = pygame.display.set_mode((1300,700))
	pygame.display.set_caption("Battleship")
	back = pygame.image.load('background1.png')
	back_image = pygame.transform.scale(back,(1300,700))
	screen.blit(back_image,background)
	clock = pygame.time.Clock()



	rect1= [] 													#For storing the coordinates of the ship whose placing is in progress, reseted each the placement is complete
	rectplayer1 = []											#For storing the coordinates of ships of player 1
	rectplayer2 = []											#For storing the coordinates of ships of player 2
	rect = [rectplayer1,rectplayer2]
	count = 0													#To iterate through various loops
	ctr = 0
	flag = 0													#|
	flag1 = 0													#|----> To create various conditions for taking input
	flag5 = 0													#|
	ctr = 0
	check = -1

	for i in range(10):
		for j in range(10):
			pygame.draw.rect(screen,black,((j+2)*50,(i+2)*50,50,50),2)
	for i in range(14,24):
		for j in range(10):
			pygame.draw.rect(screen,white,((i)*50,(j+2)*50,50,50),2)
	myfont = pygame.font.SysFont("monospace",30)
	text1 = myfont.render("Player 1",1, black)
	text2 = myfont.render("Player 2",1, white)
	screen.blit(text1, (250,50))
	screen.blit(text2, (900,50))
	pygame.display.update()

	#Setting up display - End

	#Input Loop - start

	while True and ctr<2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:						#If exit button is pressed, quit the game
				pygame.quit()
				sys.exit()

			if ctr == 0 and flag == 0:							#Displaying a circle next to the player whose turn it is
				pygame.draw.circle(screen, black, (230,60),10)
				pygame.display.update()
			if ctr == 1 and flag == 0:
				pygame.draw.circle(screen, white, (870,60),10)
				pygame.display.update()

			if flag ==  0:
				flag = 1
				import Tkinter as tk
				import tkMessageBox
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your destroyer, 2 adjacent blocks")
				root.update()

			if count == 2 and flag == 1:
				count+=1
				flag = 2

			if flag == 1 and event.type == pygame.MOUSEBUTTONDOWN :											#If mouse button is pressed, check for various conditions and assign a block
				if place_ship(ctr,rect,rect1,count,2) == 1:
					count += 1


			if count == 3 and flag == 2:
				rect[ctr].append(rect1)
				rect1 = []
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your submarine, 3 adjacent blocks")
				root.update()
				count = 0
				flag = 3

			if count == 3 and flag == 3:
				count+=1
				flag = 4

			if event.type == pygame.MOUSEBUTTONDOWN and flag == 3:
				if place_ship(ctr,rect,rect1,count,3) == 1:
					count += 1

			if count == 4 and flag == 4:
				rect[ctr].append(rect1)
				rect1 = []
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your cruiser, 3 adjacent blocks")
				root.update()
				count = 0
				flag = 5

			if count == 3 and flag == 5:
				count+=1
				flag = 6

			if event.type == pygame.MOUSEBUTTONDOWN and flag == 5:
				if place_ship(ctr,rect,rect1,count,3) == 1:
					count += 1

			if count == 4 and flag == 6:
				rect[ctr].append(rect1)
				rect1 = []
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your battleship, 4 adjacent blocks")
				root.update()
				count = 0
				flag = 7

			if count == 4 and flag == 7:
				count+=1
				flag = 8

			if event.type == pygame.MOUSEBUTTONDOWN and flag == 7:
				if place_ship(ctr,rect,rect1,count,4) == 1:
					count += 1

			if count == 5 and flag == 8:
				rect[ctr].append(rect1)
				rect1 = []
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Player " + str(ctr+1) + ", place your carrier, 5 adjacent blocks")
				root.update()
				count = 0
				flag = 9

			if count == 5 and flag == 9:
				count+=1
				flag = 10

			if event.type == pygame.MOUSEBUTTONDOWN and flag == 9:
				if place_ship(ctr,rect,rect1,count,5) == 1:
					count += 1

			if count == 6 and flag == 10:
				rect[ctr].append(rect1)
				rect1 = []
				count = 0
				flag = 0
				ctr += 1
				screen.blit(back_image,background)
				for i in range(10):
					for j in range(10):
						pygame.draw.rect(screen,black,((j+2)*50,(i+2)*50,50,50),2)
				for i in range(14,24):
					for j in range(10):
						pygame.draw.rect(screen,white,((i)*50,(j+2)*50,50,50),2)
				screen.blit(text1, (250,50))
				screen.blit(text2, (900,50))
		pygame.display.update()

	#Input Loop - end
	#Game Loop - start

	if ctr == 2:
		moves_of_p1 = []																				#For storing attacked blocks of p1
		moves_of_p2 = []																				#For storing attacked blocks of p2
		ships_p1 = 5																					#Number of ships remaining of player 1
		ships_p2 = 5																					#Number of ships remaining of player 2
		for i in range(5):																				#|
			rectplayer1[i] = map(lambda x : (x[0]+12,x[1]),rectplayer1[i])								#|
		for i in range(5):																				#|------->For swapping the position of ships of players between each others grids
			rectplayer2[i] = map(lambda x : (x[0]-12,x[1]),rectplayer2[i])								#|
		rect = [rectplayer1,rectplayer2]																#|

	#Setting up display - Start

		myfont = pygame.font.SysFont("monospace",30)
		text1 = myfont.render("Player 1 attack here",1, black)
		text2 = myfont.render("Player 2 attack here",1, white)
		text3 = myfont.render(" = Miss",1,black)
		text4 = myfont.render("Hit = ",1,white)
		text5 = myfont.render("Player 2 ships remaining = " + str(ships_p1),1,black)
		text6 = myfont.render("Player 1 ships remaining = " + str(ships_p2),1,white)
		ctr = 0
		pygame.draw.rect(screen,white,(0,0,650,700))
		pygame.draw.rect(screen,black,(650,0,650,700))
		for i in range(10):
			for j in range(10):
				pygame.draw.rect(screen,black,((j+2)*50,(i+2)*50,50,50),2)
		for i in range(14,24):
			for j in range(10):
				pygame.draw.rect(screen,white,((i)*50,(j+2)*50,50,50),2)
		screen.blit(text1, (80,50))
		screen.blit(text2, (870,50))
		screen.blit(text3, (505,50))
		screen.blit(text4, (680,50))
		screen.blit(text5, (100,620))
		screen.blit(text6, (750,620))
		pygame.draw.rect(screen,green,(450,40,50,50))
		pygame.draw.rect(screen,red,(800,40,50,50))
		pygame.display.update()

	#Setting up display - end

		while True and ctr<=2:
			if flag == 0:
				flag = 1
				import random
				ctr = random.randrange(1,3) 																	#Randomly selecting the player who starts the attack
				root = tk.Tk()
				root.withdraw()
				tkMessageBox.showinfo("Message", "Player " + str(ctr) + " starts the attack!!")
				root.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if ctr == 1:																					#Displaying a circle beside the player whose turn it is
					pygame.draw.circle(screen, black, (60,65),10)
					pygame.draw.circle(screen, black, (1260,65),10)
				elif ctr == 2:
					pygame.draw.circle(screen, white, (1260,65),10)
					pygame.draw.circle(screen, white, (60,65),10)
				pygame.display.update()
				if event.type == pygame.MOUSEBUTTONDOWN:					#If button is pressed on a block, check if opponents ship is there or not along with a few other conditions
					flag4 = 0
					[x,y] = pygame.mouse.get_pos()
					x = x/50
					y = y/50
					flag2 = 0
					if check_if_in_box(ctr-1,x,y) == 1:
						flag2 = 1
						display_invalid()
					if check_if_attacked(ctr,x,y,moves_of_p1,moves_of_p2) == 1:
						flag2 = 1
						root = tk.Tk()
						root.withdraw()
						tkMessageBox.showinfo("Message", "This block has already been attacked")
						root.update()
					if ctr == 1:
						if flag2 == 0:
							index1 = -1
							for i in rect[1]:
								index1 += 1
								index = -1
								for [xc,yc] in i:
									index += 1
									if x == xc and y == yc:
										flag4 = 1
										moves_of_p1.append([x,y])										#displaying a red filled rectangle if player hits the opponents ship
										pygame.draw.rect(screen,red,(x*50,y*50,50,50))
										pygame.display.update()
										rect[1][index1].pop(index)
										rect[1][index1].append([0,0])
										break
								if flag4 == 1:
									break
							if flag4 == 1:
								if rect[1][index1][0][0] == 0 and rect[1][index1][0][1] == 0:			#Checking if a ship has sunken, if so displaying a message
									root = tk.Tk()
									root.withdraw()
									tkMessageBox.showinfo("Message", "Congratulations, you have sunken the Player 2's " + check_ship(index1).name + " !!!")
									root.update()
									ships_p2 -= 1
									text5 = myfont.render("Player 2 ships remaining = " + str(ships_p2),1,black)
									pygame.draw.rect(screen,white,(100,620,550,50))
									screen.blit(text5, (100,620))
									pygame.display.update()

								if check_if_win(rect,ctr) == 1:
									ctr = 3
									root = tk.Tk()
									root.withdraw()
									tkMessageBox.showinfo("Message", "Player 1 wins!!!")
									root.update()
						if flag4 == 0 and flag2 == 0:													#Displaying a green filled rectangle if player misses and switching turn
							moves_of_p1.append([x,y])
							pygame.draw.rect(screen, green, (x*50, y*50, 50, 50))
							pygame.display.update()
							ctr += 1

					elif ctr == 2:
						if flag2 == 0:
							index1 = -1
							for i in rect[0]:
								index1 += 1
								index = -1
								for [xc,yc] in i:
									index += 1
									if x == xc and y == yc:
										flag4 = 1
										moves_of_p2.append([x,y])
										pygame.draw.rect(screen,red,(x*50,y*50,50,50))
										pygame.display.update()
										rect[0][index1].pop(index)
										rect[0][index1].append([0,0])
										break
								if flag4 == 1:
									break
							if flag4 == 1:
								if rect[0][index1][0][0] == 0 and rect[0][index1][0][1] == 0:
									root = tk.Tk()
									root.withdraw()
									tkMessageBox.showinfo("Message", "Congratulations, you have sunken Player 1's " + check_ship(index1).name + " !!!")
									root.update()
									ships_p1 -= 1
									text6 = myfont.render("Player 1 ships remaining = " + str(ships_p1),1,white)
									pygame.draw.rect(screen,black,(750,620,650,50))
									screen.blit(text6,(750,620))
									pygame.display.update()
								if check_if_win(rect,ctr):
									ctr = 4
									root = tk.Tk()
									root.withdraw()
									tkMessageBox.showinfo("Message", "Player 2 wins!!!")
									root.update()
						if flag4 == 0 and flag2 == 0:
							moves_of_p2.append([x,y])
							pygame.draw.rect(screen, green, (x*50, y*50, 50, 50))
							pygame.display.update()
							ctr -= 1
			if ctr>2:
				pygame.quit()
				return 1
