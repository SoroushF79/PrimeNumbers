def check(a):
    while True:
        if a <= 1:
            print("a is not greater than 1. Try again.")
            prog()
        else:
            break
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
def Histo():
    global Questio
    Questio = input("Would you like to see the histogram of the prime numbers in your interval? ")
    if (Questio.lower() == "yes") or (Questio.lower() == "y"):
        plt.hist(my_list, bins="auto")
    elif (Questio.lower() == "no") or (Questio.lower() == "n"):
        print("OK")
    else:
        print("I did not understand that.")
        Histo(Questio)
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
def checkrel(a, b):
    while True:
        if a >= b:
            print("Not valid. a ≥ b. Use different endpoints.")
            prog()
        else:
            break
def prog():
    Prompt = "Choose an interval a and b, such that 1 < a < b: "
    global a
    global b
    global p
    global mean
    global sd
    print(Prompt)
    a = input("a: ")
    b = input("b: ")
    check(int(a))
    checkrel(int(a), int(b))
    p = 0
    for x in range(int(a), int(b) +1):
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
my_list = [] 
prog()
ND()
Histo()
sys.exit()
