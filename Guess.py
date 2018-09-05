#Nicolas Tracewell
#ntracewe@ucsc.edu
#programming assignment 3
#The program chooses a random number between 1 and 10 and gives the user three guesses to get it right, giving hints with each guess.




import random
x = random.randint(1,10)
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.\n")
y = int(input("Enter your first guess: "))
if x==y:
    print("You win!\n")
if x<y:
    print("Your guess is too high.\n")
    a = int(input("Enter your second guess: "))
    if x==a:
        print("You win!\n")
    if x<a:
        print("Your guess is too high.\n")
        b=int(input("Enter your third guess: "))
        if x==b:
            print("You win!\n")
        if x<b:
            print("Your guess is too high.\n")
            print("You lose. The number was %d." % (x))
        if x>b:
            print("Your guess is too low.\n")
            print("You lose. The number was %d." % (x))
    if x>a:
        print("Your guess is too low.\n")
        c=int(input("Enter your third guess: "))
        if x==c:
            print("You win!\n")
        if x<c:
            print("Your guess is too high.\n")
            print("You lose. The number was %d." % (x))
        if x>c:
            print("Your guess is too low.\n")
            print("You lose. The number was %d." % (x))
if x>y:
    print("Your guess is too low.\n")
    d = int(input("Enter your second guess: "))
    if x==d:
        print("You win!\n")
    if x<d:
        print("Your guess is too high.\n")
        e=int(input("Enter your third guess: "))
        if x==e:
            print("You win!\n")
        if x<e:
            print("Your guess is too high.\n")
            print("You lose. The number was %d." % (x))
        if x>e:
            print("Your guess is too low.\n")
            print("You lose. The number was %d." % (x))
    if x>d:
        print("Your guess is too low.\n")
        f=int(input("Enter your third guess: "))
        if x==f:
            print("You win!\n")
        if x<f:
            print("Your guess is too high.\n")
            print("You lose. The number was %d." % (x))
        if x>f:
            print("Your guess is too low.\n")
            print("You lose. The number was %d." % (x))