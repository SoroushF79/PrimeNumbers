# Input function. Makes sure that the inputs were numbers and weren't letters/symbols.
def check():
    global a
    global b
    while True:
        try:
            a = int(input("a: "))
            b = int(input("b: "))
            break
        except ValueError:
            print("Make sure a and b are positive integer numbers, not characters or non-integer numbers.")
            prog()

# ND(Normal Distribution) function. Asks if the user wants to display a normal distribution 
# of the prime numbers from their interval.          
def ND():
    global Questi
    Questi = input("Would you like to see the normal distribution of the prime numbers in your interval? ")
    if (Questi.lower() == "yes") or (Questi.lower() == "y"):
        z = np.linspace(mean - 3*sd,mean + 3*sd)
        plt.plot(z, mlab.normpdf(z, mean, sd))
        plt.show()
    elif (Questi.lower() == "no") or (Questi.lower() == "n"):
        print("OK")
    else:
        print("I did not understand that.")
        ND(Questi)

# Histogram function. Does the same thing as the ND function except with an automaticallly
# binned histogram.
def Histo():
    global Questio
    Questio = input("Would you like to see the histogram of the prime numbers in your interval? ")
    if (Questio.lower() == "yes") or (Questio.lower() == "y"):
        plt.hist(my_list, bins="auto")
        plt.show()
    elif (Questio.lower() == "no") or (Questio.lower() == "n"):
        print("OK")
    else:
        print("I did not understand that.")
        Histo(Questio)

# Asks if the user actually wants to see the prime numbers from their interval. Displayed 
# in a list (my_list).
def finish():
    global Quest
    Quest = input("Would you like to see all the prime numbers from your interval? ")
    if (Quest.lower() == "yes") or (Quest.lower() == "y"):
        print("Here they are!")
        print(my_list)
    elif (Quest.lower() == "no") or (Quest.lower() == "n"):
        print("OK")
    else:
        print("I did not understand that.")
        finish(Quest)

# Makes sure that a was greater than or equal to b.
def checkrel(a, b):
    while True:
        if a >= b:
            print("Not valid. a ≥ b. Use different endpoints.")
            prog()
        else:
            break
        
# Makes sure that a is greater than 1.
def gre():
    while True:
        if a > 1:
            break
        else:
            print("Make sure a is greater than 1.")
        
# "Actual" program
def prog():
    Prompt = "Choose an interval a and b, such that 1 < a < b and a and b are integers: "
    global p
    global mean
    global sd
    print(Prompt)
    check()
    gre()
    checkrel(a, b)
    p = 0
    for x in range(int(a), int(b) + 1):
        for y in range(2, int(x ** 0.5) + 1):
            if x % y == 0:
                break
        else:
            my_list.append(x)
            p = p + 1
    
    print(("The number of prime numbers in your given interval is %d.") % (p))
    mean = float(statistics.mean(my_list))
    median = statistics.median(my_list)
    sd = float(statistics.stdev(my_list))
    print(("The mean and median of the prime numbers in your interval are %f and %d, respectively.") % (mean, median))
    print(("The standard deviaation of the prime numbers in your interval is %f.") % (sd))
    finish()
    
import sys
import statistics
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
a = 0
b = 0
my_list = [] 
prog()
ND()
Histo()
sys.exit()
