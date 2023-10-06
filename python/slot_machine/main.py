def deposit(): #can execute a block of code and can return a value
    while true: #can continually accept amount until valid amount entered
        amount = input("What would you like to deposit? $") #creates a prompt asking for input
            if amount.isdigit() #will accept a value for 'amount' only if it is a digit
