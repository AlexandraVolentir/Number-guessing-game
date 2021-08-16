# guessing game in python

def guess_the_number():
    
    print("Choose a number in the interval [1..100]")
    print("I bet I can guess it in no more than 7 tries!")
    positive_answer = {"y", "yes"}
    negative_answer = {"n", "no"}
    lowerbound = 1
    upperbound = 100
    guess = (1 + 100) // 2
    found, won = False, False
    i = 0
  
    start_game = input("Are you ready? y/n: ")
    if (start_game in positive_answer):
        for attempt in range(1,8):
            if not won:
                traversed = False
                i += 1
                while not traversed:  
                    print(i)
                    if found == False:
                       answer = list(input("I guess it is " + str(guess) + "!\nIs it [L]ow, [H]igh or [E]qual? ").lower().strip())
                       if(answer == ["l"] or answer == ["low"]):
                           lowerbound = guess
                           guess = (lowerbound + upperbound)//2
                           traversed = True
                           continue
                       elif(answer == ["h"] or answer == ["high"]):
                           upperbound = guess
                           guess = (lowerbound + upperbound)//2
                           traversed = True
                           continue
                       elif(answer == ["e"] or answer == ["equal"]):
                            print("Hurray! I won the game in " + str(i) + " guesses. Yupp!!")
                            traversed = True
                            won = True
                            break
                       else:
                           continue
            else:
                break
    elif start_game in negative_answer:
        print("Goodbye!")
    else:
        print("Unvalid unswer. Bye!")
    if won == False and i == 7:
        print("\nSomething smells fishy don't you think so?")
        
guess_the_number()
