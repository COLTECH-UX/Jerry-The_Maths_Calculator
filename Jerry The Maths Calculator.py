Name = input("Enter Your Name Here: ")
if Name == "Jerry":
    print("Wow!!! Hi there my Name Sake, how are you doing Bro ? " + "Oh my God I can't believe that the user have "
          "the same name with me Man, I am so honored right now to be seeing You " + """
    So there Name Sake, I'm a Maths calculator. Do You wanna know more about me ?   
    """)
    print(""" Please Enter The Letters km/KM Below To Continue. 
        Or Enter The Word no/NO To Skip Straight To My Functions ASAP
    """)
else:
    print("Hi there " + Name + ".My Name is Jerry, I'm a maths calculator. Do you wanna know more about me ?")
    print(""" Then Please Enter The Letters km/KM Below To Continue. 
    Or Enter The Word no/NO To Skip Straight To My Functions ASAP
    """)

Command = input("> ").lower()
if Command == "km":
    print("Well " + Name + """ I'm glad you asked that you asked me that question. Like I said before
I'm a maths calculator, that is programmed to solve and answer all your basic calculations in mathematics(i.e Addition, 
Subtraction, Division & Multiplication)."""
    "Well then, let us start shall we ? To continue please enter the given signs below that is beside " +
    "the functions each" """
So do you want to;
Add(+)  
Subtract(-)
Multiply(*)
Divide(/)
Quit(Q/q)           
""")
if Command == "no":
    print("So " + Name + """
Do you want to;
    Add(+)
    Subtract(-)
    Multiply(*)
    Divide(/)
    Quit(Q/q) 
""")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

while True:
    Choice = input("> ")
    if Choice in ('+', '-', '*', '/'):
        Num1 = int(input("Enter The First Number Here: "))
        Num2 = int(input("Enter The Second Number Here: "))
    if Choice == '+':
        print(Num1, "+", Num2, "=", add(Num1, Num2))

    if Choice == "-":
        print(Num1, "-", Num2, "=", subtract(Num1, Num2))

    elif Choice == '*':
        print(Num1, "*", Num2, "=", multiply(Num1, Num2))

    elif Choice == '/':
        print(Num1, "/", Num2, "=", divide(Num1, Num2))
    elif Choice == 'Q':
        break



