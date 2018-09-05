#Nicolas Tracewell
#ntracewe@ucsc.edu
#programming assignment 5
#This program guesses the number you're thinking of based on given parameters.
        
print("Enter two numbers, low then high.")
low = int(input("low: "))
high = int(input("high: "))
if low>high:
    print("\nPlease enter the smaller followed by the larger number.")
    low = int(input("low: "))
    high = int(input("high: "))
counter = 0
guess = int((low+high)/2)
Guesses = []
while low<=high:
    if counter == 0:
        if low == high:
            print("Your answer is %d. I found it in 0 guesses." % (low))
            break
    Inconsistent = False
    Done = False
    if counter != 0:
        for i in range(0, len(Guesses)):
            if guess == Guesses[i]:
                print("Your answers have not been consistent.")
                Inconsistent = True
                break
    if Inconsistent == True:
        break
    if counter == 0:
        print("Think of a number in the range %d to %d." % (low, high))
    print("\nIs your number Less than, Greater than, or Equal to %d?" % (guess))
    hint = input("Type 'L', 'G' or 'E': ")
    Acceptable = False
    while Acceptable == False:
        if hint != "G" and hint != "g" and hint != "L" and hint != "l" and hint != "E" and hint != "e":
            hint = input("Please type 'L', 'G' or 'E': ")
        if hint == "G" or hint == "g" or hint == "L" or hint == "l" or hint == "E" or hint == "e":
            Acceptable = True
    if hint == "G" or hint == "g":
        low = int(guess)
    if hint == "L" or hint == "l":
        high = int(guess)
    if hint == "E" or hint == "e":
        if counter == 0:
            print ("Your answer is %d. I found it in 1 guess." % (guess))
            Done = True
        elif counter != 1:
                print("Your answer is %d. I found it in %d guesses." % (guess, int(counter+1)))
                Done = True
    if Done == True:
        break
    Guesses.append(guess)
    guess = int((low+high)/2)
    if hint == "G" or hint == "g":
        guess = int((low+high+1)/2)
    counter+=1
