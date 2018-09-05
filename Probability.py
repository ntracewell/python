#Nicolas Tracewell
#ntracewe@ucsc.edu
#programming assignment 6
#This program calculates the probability of each possible sum of a dice roll when given the number of dice, the number of sides of each die, and the number of rolls to perform.

import random
rng = random.Random(237)

def throwDice(m, k):
    Dice = []
    total = 0
    for rolls in range(0, m):
        die = rng.randrange(1, k+1)
        Dice.append(die)
        total+=int(Dice[rolls])
    Totals.append(total)

number = int(input("Enter the number of dice: "))
while number < 1:
    print("The number of dice must be at least 1")
    number = int(input("Please enter the number of dice: "))
sides = int(input("\nEnter the number of sides on each die: "))
while sides < 2:
    print("The number of sides on each die must be at least 2")
    sides = int(input("Please enter the number of sides on each die: "))
trials = int(input("\nEnter the number of trials to perform: "))
while trials < 1:
    print("The number of trials must be at least 1")
    trials = int(input("Please enter the number of trials to perform: "))

Totals = []
Sum = []
Frequency = []
Relative = []
Experimental = []
counter = 0

while counter<trials:
    throwDice(number, sides)
    counter+=1
for x in range(number, sides*number+1):
    Sum.append(x)
for i in range(0, len(Sum)):
    frequency = 0
    for j in range(0, len(Totals)):
        if Sum[i] == Totals[j]:
            frequency+=1
    Frequency.append(frequency)
for f in range(0, len(Frequency)):
    Relative.append(Frequency[f]/trials)
    Experimental.append(Frequency[f]*100/trials)

print("{0:<9}{1:<14}{2:<23}{3}".format(" Sum", "Frequency", "Relative Frequency", "Experimental Probability"))
table = "{0:>4}{1:>11}{2:>18.5f}{3:>21.2f} %"
print("----------------------------------------------------------------------")
for t in range(len(Sum)):
    print(table.format(Sum[t], Frequency[t], Relative[t], Experimental[t]))
