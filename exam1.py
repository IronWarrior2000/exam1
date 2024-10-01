#Bill Nguyen | Exam 1

def main(): #The main function has 
    for value in range(0,51): #for each value in the range between 0-50
        if value%5 ==0: #If the value is divisible by 5 
            print("Hi-Five") #it will print out Hi-Five
        elif value%2 ==0: #If the value is divisible by 2
            print("Hi-Two") #It will print out Hi-Two
        elif value%3 ==0 or value%7 ==0: #If the value is divisible by 3 or 7  
            print("Hi-Three-Or-Hi-Seven") #It will print out Hi-three or Hi-Seven
        else: #Or else 
            print(value) #It will print out the value if it doesnt fit in to another other categories
    print("End of program") #At the end of loop it will end the programming
main() #And this will call the main function to make everything work.