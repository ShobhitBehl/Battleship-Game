def check_if_in_box(ctr,x,y):														#Function to check if player has chosen a block in his own grid
	if ctr == 0 and (x<2 or y<2 or y>=12 or x>=12):
		return 1 
	elif ctr == 1 and (x<14 or y<2 or y>=12 or x>=24):
		return 1
	else:
		return 0

def check_if_ship_present(ctr, x, y, rect, rect1):									#Function to check if a ship is already present on the block
	for i in rect[ctr]:
		if [x,y] not in i:
			continue
		else:
			return 1
	if [x,y] not in rect1:
		return 0
	else:
		return 1

def check_if_diagonal(x,y,rect1):													#Function to check if an attempt is made to place a ship diagonally
	if abs(rect1[0][0]-x) == 1 and abs(y-rect1[0][1]) == 1:
		return 1
	else: 
		return 0

def check_if_valid(x,y,rect1):														#Function to check the validity of placement of ships
	if check_if_diagonal(x,y,rect1) == 1:
		return 0
	elif (abs(x - rect1[0][0]) > 1 or abs(y - rect1[0][1]) > 1):
		return 0
	else:
		return 1
		
def check_orientation((x2,y2),(x1,y1)):												#Function to check the orientation of ship after second block if selected
	if abs(x2-x1) == 1:
		return 0
	else:
		return 1
		
def check_if_horizontal(x,y,rect1,count):											#Function to check if a ship is being placed in a straight horizontal line
	if (abs(x - rect1[0][0]) == 1 and abs(y - rect1[0][1]) == 0) or (abs(x - rect1[count-1][0]) == 1 and abs(y-rect1[count-1][1]) == 0):
		return 1
	else: 
		return 0

def check_if_vertical(x,y,rect1,count):												#Function to check if a ship is being placed in a straight vertical line		
	if (abs(x - rect1[0][0]) == 0 and abs(y - rect1[0][1]) == 1) or (abs(x - rect1[count-1][0]) == 0 and abs(y-rect1[count-1][1]) == 1):
		return 1
	else:
		return 0

def check_if_can(ctr,x,y,rect,rect1,length,count):									#Check if a ship can possibly be placed around one or two selected blocks
	flag5 = 0
	if count == 0:
		for i in range(length):
			if check_if_ship_present(ctr,x+i,y,rect,rect1) == 1 or check_if_in_box(ctr,x+i,y) == 1:
				flag5 = 1
				right_x = i-1
				break
		if flag5 == 1:
			flag5 = 0
			for i in range(length):
				if check_if_ship_present(ctr,x-i,y,rect,rect1) == 1 or check_if_in_box(ctr,x-i,y) == 1:
					flag5 = 1
					left_x = i-1
					break
		if flag5 == 1:
			if right_x + left_x >= length - 1:
				flag5 = 0
		if flag5 == 1:
			flag5 = 0
			for i in range(length):
				if check_if_ship_present(ctr,x,y+i,rect,rect1) == 1 or check_if_in_box(ctr,x,y+i) == 1:
					flag5 = 1
					down_y = i-1
					break
		if flag5 == 1:
			flag5 = 0
			for i in range(length):
				if check_if_ship_present(ctr,x,y-i,rect,rect1) == 1 or check_if_in_box(ctr,x,y-i) == 1:
					flag5 = 1
					up_y = i-1
					break
		if flag5 == 1:
			if up_y + down_y >= length - 1:
				flag5 = 0
	if count == 1:
		c = check_orientation(rect1[0],[x,y])
		if c == 0:
			for i in range(1,length):
				if check_if_ship_present(ctr,rect1[0][0]+i,rect1[0][1],rect,rect1) == 1 or check_if_in_box(ctr,rect1[0][0]+i,rect1[0][1]) == 1:
					flag5 = 1
					right_x = i-1
					break
			if flag5 == 1:
				flag5 = 0
				for i in range(1,length):
					if check_if_ship_present(ctr,rect1[0][0]-i,rect1[0][1],rect,rect1) == 1  or check_if_in_box(ctr,rect1[0][0]-i,rect1[0][1]) == 1:
						flag5 = 1
						left_x = i-1
						break
			if flag5 == 1 and right_x + left_x == length - 1:
				flag5 = 0	
		else:
			for i in range(1,length):
				if check_if_ship_present(ctr,rect1[0][0],rect1[0][1]+i,rect,rect1) == 1 or check_if_in_box(ctr,rect1[0][0],rect1[0][1]+i) == 1:
					flag5 = 1
					down_y = i-1
					break
			if flag5 == 1:
				flag5 = 0
				for i in range(1,length):
					if check_if_ship_present(ctr,rect1[0][0],rect1[0][1]-i,rect,rect1) == 1  or check_if_in_box(ctr,rect1[0][0],rect1[0][1]-i) == 1:
						flag5 = 1
						up_y = i-1
						break
			if flag5 == 1 and down_y + up_y == length - 1:
				flag5 = 0 
	return flag5

def check_if_attacked(ctr,x,y,moves_of_p1,moves_of_p2):												#Check if the block has already been attacked by the player
	if ctr == 1:
		if [x,y] not in moves_of_p1:
			return 0
		else:
			return 1
	elif ctr == 2:
		if [x,y] not in moves_of_p2:
			return 0
		else:
			return 1
			
def check_if_win(rect,ctr):																			#Check if all the ships of a player have been sunken
	if ctr == 2: 
		if rect[0][0][0][0] == 0 and rect[0][0][0][1] == 0 and rect[0][1][0][0] == 0 and rect[0][1][0][1] == 0 and rect[0][2][0][0] == 0 and rect[0][2][0][1] == 0 and rect[0][3][0][0] == 0 and rect[0][3][0][1] == 0 and rect[0][4][0][0] == 0 and rect[0][4][0][1] == 0:
			return 1
	elif ctr == 1:
		if (rect[1][0][0][0] == 0 and rect[1][0][0][1] == 0) and (rect[1][1][0][0] == 0 and rect[1][1][0][1] == 0) and (rect[1][2][0][0] == 0 and rect[1][2][0][1] == 0) and (rect[1][3][0][0] == 0 and rect[1][3][0][1] == 0)and (rect[1][4][0][0] == 0 and rect[1][4][0][1] == 0):
			return 1
