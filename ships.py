class Ship():														#A class Ship to associate a name, size and index to every ship
	def __init__(self,s,name,index):
		self.size = s
		self.name = name
		self.index = index

destroyer = Ship(2,"Destroyer",0)
submarine = Ship(3,"Submarine",1)
cruiser = Ship(3,"Cruiser",2)
batlleship = Ship(4,"Battleship",3)
carrier = Ship(5,"Carrier",4)

ships = [destroyer,submarine,cruiser,batlleship,carrier]

def check_ship(ind):												#Function to check the index of a ship
	for i in ships:
		if i.index == ind:
			return i
	
