#This stores the user input as the variable name and then prints hello and then the variable called name
def hello():
    print("What's your name?") # Asks the user for her/his name
    name = input() # stores the user input to a variable
    print("Hello, " + str(name)) # Prints hello and then the string version of the input

hello() # calls our function
