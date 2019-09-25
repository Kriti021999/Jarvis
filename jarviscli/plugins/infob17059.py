from plugin import LINUX, PYTHON3, plugin, require
@require(python=PYTHON3, platform=LINUX)
@plugin('infob17059')
def infob17059(jarvis, s):
	"""
	prints the info for b17059
	"""

	print('''
		Welcome to the info plugin of Saurabh Bansal
		roll num B17059. Please select one of the options below:
		[F]ull name // prints your full name
		[H]ometown // prints your hometownFavourite
		[M]ovie // prints your fav movieFavourite
		[S]portsperson // prints your fav sportspersonLaunch
		[P]ython program written by me // launch a (short)// python program
		[E]xit
		''')
	while(1):
		instr = input("command:$ ")
		
		if(instr == "F"):
			print("SAURABH BANSAL")
		elif(instr == "H"):
			print("Narela")	
		elif(instr == "M"):
			print("Bahubali")	
		elif(instr == "S"):
			print("Ben Stokes")	
		elif(instr == "P"):
			print("Python program")	
		elif(instr == "E"):
			return
		else:
			print("Invalid input")				


