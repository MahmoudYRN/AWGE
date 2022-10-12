print("""\t\t\tWelcome to HappyPhones :)\n""")
# this message is displayed when the program starts
#############

balance = 75
tariff = "A"

def Login_system():

    useranswer = input("""\n\nplease choose one of the actions:

1] Login

2] Register

3] Exit

>> """)
#this here asks the user if they want to register or login if they're already a memeber
#if the user chose to login the login funtion will start
#if they chose to register it will take them to register funtion
    if useranswer == "1":
        Login()
    elif useranswer == "2":
        Register()
    elif useranswer == "3":
        print("bye.........")
        exit()
        
    else:
        print(" Invalid input...")
        Login_system()
###############
def Login():
	print(" ")
	import time
	#this imports time so it allows us to make the script to pause at certain times
	attempts = 0

	while True:
		username = input("Username: ")
		password = input("Password: ")
	# while True loops this part of the script untill you tell it to stop
		if username == "mahmoud" and password == "endless":
			print("Access Granted")
			break
	# the username and password both has to be correct 
		elif username == "frank" and password == "provider":
			print("Access Granted")
			break
		elif username == "endless" and password == "nostalgiaultra":
			print("Access Granted")
			break
	# if the user enters any of these combinations they well get access to the system
	#script only runs if the user enters incorrect details
		else:
			print("Access Denied")
			attempts = attempts + 1
			time.sleep(0.5)
			if attempts == 2:
				create = input("""\nwould you like to create an account? y,n 
>>> """) #if the username chose "y" to create an account this script will run, 
			 #otherwise it will just continue asking them for username and password
			# once the user has created an account they program will continue 	
				if create == "y":
					input("name: ")
					input("username: ")
					input("password: ")
					break#this tells the program to break and continue
				
			
	#if they enter incorrect details 3 times program will block them and and stops running
			if attempts == 3:
				time.sleep(0.5)
				print("\nyou have entered incorrect logins too many times")
				input("press enter to continue")
				exit()#this exits the whole program
                #only if user fails to provide correct details


def Register():
	input("name: ")
	input("username: ")
	input("password: ")
Login_system() #what evr is above wont be execute from this point
## we are telling the program to stop this function and carry on with the rest of the program

def menu():
#tripple quotes is used here so whatever is in between them can be displayed by the program with
#no problems
    useranswer = input("""\n\nWhich of the following would you like to do?:

1] Check current account balance

2] display current tariff

3] view list of rates

4] Alter or keep current tariff

5] Choose a new tariff

6] Display total bill

7] enter minutes

8] Help

9] Exit

>> """)



###

###
# Menu fuction with 5 options

    if useranswer == "1":
        optionone()#if the entered value is "1" the function "option one" will run
    elif useranswer == "2":
        optiontwo()  #same with this....
    elif useranswer == "3":
        optionthree()
    elif useranswer == "4":
        optionfour()
    elif useranswer == "5":
        optionfive()
    elif useranswer == "6":
        optionsix()
    elif useranswer == "7":
        optionseven()
    elif useranswer == "8":
        help()#this a function named "help"
    elif useranswer =="9":
        print("bye.......")
        exit()#if the value = 7 the program closes itself
    else:  # if the entered value isnt above this code below will be executed
        print(" Invalid input...")
        menu()
#current account balance
def optionone(): #####balance
    print(" ")
    #import random #random is module that we impport to allow us do things like generate random numbers
    #balance = random.randint(10,45) #the randomly generated number has to be high than 10 and less than 45
    print("your current balance is ",balance)
    input("press enter to continue")
    menu()

#current tariff
def optiontwo():####display current tariff
    global tariff
    print("Your current tariff is ",tariff)
    #
    input("press enter to continue")
    menu()

#list of rates                
def optionthree():####view list of rates
    print("""
     _____________________________________________
    | Tariff | Peak Rate | Off-Peak |  Line Rental| 
    | A      | £ 0.30    | £ 0.05   | £ 15.00     |
    | B      | £ 0.10    | £ 0.02   | £ 20.00     |
    | C      | £ 0.90    | £  -     | £ 30.00     |
    -----------------------------------------------
    """)
    input("press enter to continue")
    menu()
#anything within this function "def optionfour) wont be executed without calling it
def optionfour():###Alter or keep current tariff
    global balance
    print("")
    ok = input("""\nare you sure you want to alter your tariff

this will cost you (£9) y/n
>>>> """)
    if ok == "y":
        print("you have paid your previous bill you can now change your tariff.\n")
        balance = balance -9
        print("your balace is now £",balance )
    else:
        pass
    input("press enter to continue")
    
    menu()#this makes the progra return back to the menu

#5] Choose a new tariff

def optionfive():#####Choose a new tariff
    global tariff
    global balance
    print("")
    ac = input("""

     _____________________________________________
    | Tariff | Peak Rate | Off-Peak |  Line Rental| 
    | A      | £ 0.30    | £ 0.05   | £ 15.00     |
    | B      | £ 0.10    | £ 0.02   | £ 20.00     |
    | C      | £ 0.90    | £  -     | £ 30.00     |
    -----------------------------------------------
    
which of the following Tariff would you like to switch to?
>>>  """)
    if ac == "a":
        tariff = "A"
        balance = balance -15
        print("\nyour current tarrif is",tariff)
        
        
    elif ac == "b":
        tariff = "B"
        balance = balance -20
        print("you have succesfully switched to tarrif",tariff)
    elif ac == "c":
        balance = balance -30
        tariff = "C"
        print("you have succesfully switched to tarrif",tariff)
    print("your new balance is",balance)    
    input("\npress enter to continue")
    menu()
def optionsix():#total bills
    global tariff
    if tariff == "A":
        print(" your total bills is", 0.30+0.05+15,"and 20% VAT")
    elif tariff == "B":
        print("your total bills is", 0.10+0.02+20,"and 20% VAT")
    elif tariff == "C":
        print("your total bills is", 0.90+30,"and 20% VAT")
    
    input("\npress enter to continue")
    menu()
def optionseven():# total bills
    global tariff
    try:
        minutes = int(input("\nenter your minutes: "))
    except:
        print("\nyou must enter a number")
        optionseven()
    
    if tariff == "A":
        print("\nBased On your current Tariff This will cost you £", minutes / 60 * 0.30)
    if tariff == "B":
        print("\nBased On your current Tariff This will cost you £", minutes / 60 * 0.10)
    if tariff == "C":
        print("\nBased On your current Tariff This will cost you £", minutes / 60 * 0.90)
    print ("""

     _____________________________________________
    | Tariff | Peak Rate | Off-Peak |  Line Rental| 
    | A      | £ 0.30    | £ 0.05   | £ 15.00     |
    | B      | £ 0.10    | £ 0.02   | £ 20.00     |
    | C      | £ 0.90    | £  -     | £ 30.00     |
    -----------------------------------------------

        """)

    input("\npress enter to continue")
    menu()
 #help
def help():
    print("\t\t\tWelcome to HappyPhones Support\n") #\t is tab and \n starts new line
    print("""
1] Check current account balance
This will displays your current balance on your screen

2] display current tariff
this displays your current tariff and may asks you if you want to change it

3] view list of rates
this will show a table with the list of different rates

4] Alter or keep current tariff
you can alter your tarrif or change it here
may require you to pay some fees

5] Choose a new tariff
here you can change your tarrif without paying any additional fees
only if you are eligable

6] Help
this is for the help 
""")
    
    input("press enter to continue") 
    menu()
menu()
