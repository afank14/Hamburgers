# Alex Fankhauser, Ryan Tetro, Adam Naylor, Marcus Galbraith, Noah Haskett, Jesse Ritter
# This program simulates a Door Dash ordering system
    #It generates a list of 100 random orders, then uses a dictionary to total the number of burgers each customer ordered.
    #It outputs the customer names and total burgers ordered in order from most burgers to least

#Import random for number generation
import random

#Create a class for orders
class Order :
    def __init__(self) :
        #Assign attribute to method
        self.burger_count = self.randomBurgers()

    #Create method to generate a random number of burgers for each order  
    def randomBurgers(self) :
        return(random.randint(1,20))

#Create a class for a person 
class Person :
    def __init__(self) :
        #Assign class attribute to random name generating method
        self.customer_name = self.randomName()
    
    #Create a method to generate a random name from a list of 9 names
    def randomName(self) :
        self.lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return(self.lstCustomers[random.randint(0,8)])

#Create a class for customers that inherit from the person class
class Customer(Person) :
    def __init__(self) :
        #Call the parent contructor to get the name
        super().__init__()
        #Assign the attribute to an object of the Order Class
        self.order = Order()

#Create a queue for customers and a dictionary
queueCustomers = []
dictCustomers = {}

#Use a for loop to add customer objects to the queue
for iCount in range(0,100) :
    oC = Customer()
    queueCustomers.append(oC)

#Create a variable for the length of the customer queue
qLen = len(queueCustomers)

#Use a for loop to load the dictionary for each customer object in the queue
for dNum in range(0, qLen) :
    #Check to see if the customer name is already a key in the dictionary
    if queueCustomers[dNum].customer_name in dictCustomers :
        #If the name is already a key, increment its value pair by the additional burger count attached to that object in the queue
        dictCustomers[queueCustomers[dNum].customer_name] += queueCustomers[dNum].order.burger_count
    else :
        #If the name is not a key, create the key value pair using the customer name and burger count
        dictCustomers[queueCustomers[dNum].customer_name] = queueCustomers[dNum].order.burger_count
    
#Create a new list that orders the dictionary from most burgers ordered to least
listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True) 

#Get the length of the new sorted list
lenSC = len(listSortedCustomers)

#Use a for loop to print the sorted list
for pNum in range(0,lenSC) :
    print(*listSortedCustomers[pNum])