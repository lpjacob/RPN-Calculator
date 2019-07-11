"""
Program to perform simple calculations using Reverse Polish Notation
by ljacob1@canterbury.kent.sch.uk
Purpose: to demonstrate stack operation, RPN and string handling in procedural code,
multiplication using a recursive function, default parameters in Python
Limitations: WIP - not currently fully tested
"""

"""global variables"""
stack = [] # empty list as stack
headPointer = 0 #pointer to head of stack
maxHeight = 5 #constant to set max stack size
operatorsUsed=("+","-","*","/") #tuple holding operators the program can work with

def stackPush(item):
    """push item on to stack if not full, increments pointer"""
    global stack, headPointer
    if headPointer < maxHeight:
        stack.append(item)
        headPointer +=1
        print("Stack holds",stack)
    else:
        print("stack full")
        
def stackPop():
    """returns and removes top item from stack, decrements pointer"""
    global stack, headPointer
    removedItem = None #local variable
    if headPointer >=1:
        headPointer -=1
        removedItem = stack.pop(headPointer)  
    else:
        print("stack empty")
    return removedItem

def add(operand1, operand2):
    """return sum of operands"""
    return operand1 + operand2

def subtract(operand1, operand2):
    """return difference of operands"""
    return operand1 - operand2

def multiply(operand1, operand2, total=0, counter=0):
    """Recursive function to return product of operands"""
    if counter < operand2:
        total = total + operand1
        counter+=1
        return multiply(operand1, operand2, total, counter)
    else:
        return total

def division(operand1, operand2):
    """return quotient of operands -simulates floor division"""
    return operand1/operand2
    

def equations(operator):
    """perform equation using stack values, depending on operator passed in
    result is pushed back on the stack and returned """
    global operatorsUsed
    operand1 =None #local variables
    operand2 =None
    result = None
    
    #check the operator is useable
    if operator not in operatorsUsed:
        print ("Operator",operator, "not recognised. Give up!")
    else: #if it is,pop 2 values from stack
        operand1 = stackPop()
        operand2 = stackPop()
        if operand1 == None or operand2 == None:
            print("not enough items on stack")
        else:
            if operator == "+":
                result=add(operand1,operand2)
            elif operator == "-":
                result=subtract(operand1,operand2)
            elif operator == "*":
                result=multiply(operand1,operand2)
            elif operator == "/":
                result=division(operand1,operand2)
            else:
                print("Invalid operator") 
            
    return result     
    

def parseInput(inputString):
    """takes the input string and pushes numbers on stack
    if an operator is found is will call equation function
    returns the result of the equation if not none"""
    result = None #local variable
    operator = None
    
    inputString = inputString.replace(" ", "") #strip spaces from input
    inputList = inputString.split(",") #create a list where commas are found
    tempString="" #holds characters that will get pushed to stack
    for i in range(0,len(inputList)):
        if inputList[i].isnumeric():#deal with any items that are just operands
            stackPush(float(inputList[i]))#if value is a number, cast to float and push on stack
        else:
            for character in inputList[i]:
                if character.isnumeric():
                    tempString = tempString+character #concatenate characters
                else:
                    operator = character
                    break
            if len(tempString)>0:    
                stackPush(float(tempString))# if any numbers found, cast to float and push on stack
            if operator != None:
                result = equations(character)# send the the operator to the equations function
            if result != None:
                stackPush(float(result)) #push result to
    return result
                   
        


def menu():
    """contains the inputs and outputs"""
    
    print("""
            Welcome to the RPN Calculator
            Please enter sums in Postfix notation
            -------------------------------------
                 Example 2,2+ will return 4
            -------------------------------------""")
    while True:
        inputString = "" #local variables
        outputString ="The result of "
        inputString = input("please enter equation and press enter")
        print("You entered", inputString)
        result = parseInput(inputString)#call string parser to add to stack
        outputString = outputString + inputString + " is " + str(result)
        print(outputString)

if __name__ =="__main__":
    menu()
