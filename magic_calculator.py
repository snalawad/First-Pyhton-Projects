
import re

print("The Magical Calculator")
print("Type quit to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

#Taking Inputs
    if previous == 0:
        equation = input("Enter Equation")
    else:
        equation = input(str(previous))

# For quitting the calculator

    if equation == 'quit':
        print("Goodbye!")
        run = False
  
#Keeping only equations and eliminating the rest
        
    else:
        equation = re.sub('[a-z A-Z,.:{} " "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

#Here we go..!!
while run:
    performMath()
    
