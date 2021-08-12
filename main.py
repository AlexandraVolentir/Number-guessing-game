# guessing game in python

print("Choose a number in the interval [1..100]")
print("I bet I can guess it in no more than 7 tries!")


def guess_the_number():
    positive_answer = {"y", "yes"}
    negative_answer = {"n", "no"}
    lowerbound = 1
    upperbound = 100
    guess = (1 + 100) // 2;
    found = False
    for attempt in range(1,8):
        if found == False:
           print("I guess it is " + guess + "!\nIs it [L]ow, [H]igh or [E]qual? ")
          
           ###############
           
        else:
            print("Hurray! I won the game")



