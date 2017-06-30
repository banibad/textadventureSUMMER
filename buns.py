

go_again = True

while go_again == True:

    user = input("It's Summer Break! You can press 1 and go to coding camp or press 2 to stay home all summer\n")
    if user == "1":
        rekt = input("You can press 1 to do coding all day or press 2 to choose not to focus and be bored in class\n")
        if rekt == "1":
            doggo = input("Now you're learning new things! Type OK to continue\n")
            if doggo == "OK":
                print("YOU'VE SUCCEEDED!! YOU WONNNN\n")
        elif rekt == "2":
            hair = input("Now you're learning nothing! This is bad because you're wasting your time. Type YES to continue\n")
            if hair == "YES":
                print("YOU'VE FAILED. GAME OVER\n")
    elif user == "2":
        peanut = input("Press 1 to wait all day for a ride or press 2 to take the local bus\n")
        if peanut == "1":
            notebook = input("Now you can either press 1 to get a ride really late or press 2 to go nowhere all day\n")
            if notebook == "1":
                meme = input("You messed up, and now all your friends are busy. Type OK to continue\n")
                if meme == "OK":
                    poop = input("OMEGLE TIME! YOU CAN MAKE NEW FRIENDS! Type OH NO to continue\n")
                    if poop == "OH NO":
                        print("You saw some gross stuff and now you are grossed out and sad. GAME OVER\n")
            elif notebook == "2":
                print("GAME OVER\n")
        if peanut == "2":
            death = input("Alrighty you could either find your friends by pressing 1, or press 2 and get lost...but actually REKT\n")
            if death == "1":
                gatorade = input("Aw man now your friends left early, press OK to continue\n")
                if gatorade == "OK":
                    print("Omg now the bus is delayed and you're all alone. GAME OVER\n")
            if death == "2":
                print("GAME OVER\n")


    person = input("Do you want to play again?\n")
    if person == 'no':
        print("BYEEEE\n")
        go_again = False
    else:
        print("Let's gooooo")
