### Created by Max Marder

import math
import random

instr ="""
Now that we've talked about numerical simulations, you can write a program 
to analyze the probability that two people in a group of people share a 
common birthday (month + day).

Q1. 
In a group of five people, what's the approximate probability that two of them
share a birthday?

Q2. 
In a group of fifteen people, what's the approximate probability that two of 
them share a birthday?

Q3. 
How big does the group have to be in order for the probability to be > 50%?
"""

# Statistical Solution
def nPr(n,r):
    f = math.factorial
    return f(n)/f(n-r)

def StatBirthdays(n):
    year = 365
    birthProb = (1-(nPr(year,n)/(year**n)))*100
    return birthProb

# Mathematical Simulation
def SimBirthdays(numPeople, numTrials):
    simCount = 0
    percentage = 0.0

    for i in range(numTrials):
        birthdayList = []
        for i in range(numPeople):
            newBDay = random.randrange(365)
            birthdayList.append(newBDay)
        simCount += (len(birthdayList) - len(set(birthdayList)))
        
    percentage = float((simCount/numTrials)*100)
    return percentage

def ProbSimBirthdays(targetPercentage, numTrials):
    i = 0
    percent = 0.0
    while(percent < 50):
        percent = SimBirthdays(i, numTrials)
        i+=1
    return i


# Main
if __name__ == '__main__':
    print(instr)

    # 1. group of 5
    print("A1.")
    print("Probabalistic results for a group of 5 people: ","%.2f" %StatBirthdays(5), "%", sep="")
    print("Simulation results for a group of 5 people (10000 Trials): ","%.2f" %SimBirthdays(5, 10000), "%", sep="")
    print("")
    
    # 2. group of 15
    print("A2.")
    print("Probabalistic results for a group of 5 people: ", "%.2f" %StatBirthdays(15), "%", sep="")
    print("Simulation results for a group of 15 people (10000 Trials): ","%.2f" %SimBirthdays(15, 10000), "%", sep="")
    print("")

    # 3. probability > 50%
    print("A3.")
    i=0
    while(StatBirthdays(i)<50):
        i+=1
    print("Probabalistic group size to reach 50% probability: ", i, " people", sep="")
    print("Simulated group size to reach 50% probability: ",ProbSimBirthdays(50, 10000), " people", sep="")