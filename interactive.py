#Main program executor
import pyRecipeBook
import FoodGroups
import ShoppingList as List

#Welcome screen
welcomeMessage =  "Welcome to pyRecipeBook!\n"
welcomeMessage += "Enter a command below:\n"
print(welcomeMessage)

#Initiate a shopping list
myShoppingList = []

#Method for `exit` command
def exitCom(args):
	#Predefined so args is never less than 1
	if len(args) > 1: #Too many arguements
		return True
	#Interactive mode should is not on
	return False

#Method to print the shopping list
def printShoppingList(myList):
	print myList

#Method to initialize the shopping list from file
def initShoppingList(filename=None):
	myList = []
	#Attempt to read file
	try:
    		content = open(filename, "r")
    		#Convert file to usable list
    	#Return an empty lisst
	except FileNotFoundError:
		#Hangle error
	return myList

#Method to run commands
def runCommand(command,myShoppingList=[]):
	#Split command
	args = command.split()
	#
	if len(args) < 1: #No command -> pass
		return True
	elif args[0] == 'exit': #Exit command
		print('Exiting...')
		return exitCom(args)
	#Proceed to add what is given
	elif args[0] == 'add': 
		#Test whether the arguements are valid
		if len(args) == 1: #Not enough arguements
			print "Minimum of 2 arguements must be given"
		elif len(args) >4:
			print "Maximum of 4 arguements must be given"
		else: #Add item to list
			#Convert the arguements to something to input into Python method 
			newArgs = (myShoppingList,) + tuple(args[1:]) #list, item, (quantity), (unit)
			#Add to the shopping list
			myShoppingList = addToList(*newArgs)
		return True
	#Operate on the shopping list
	elif args[0] == 'shoppingList': 
		#
		if len(args) == 1: #Print the list
			printShoppingList()
		else: #Not valid arguments
			print "Command not valid"
		return True
	#Command isn't defined	
	else: 
		print('That command doesn\'t exist.')
		return True

#Add item to shopping list
def addToList(myList,item,quantity=1,unit=''):
	myItem = List.Item(item,quantity,unit)
	myList.append(myItem)
	return myList
#
pre = '# '
on = True

#Keep asking for inpyt
while(on):
	#Enter a command
	command = raw_input(pre)
	#Run command
	on = runCommand(command)

#Exiting commands
exitMessage = "\nThank you for choosing to use pyRecipeBook!\n"	
print(exitMessage)
