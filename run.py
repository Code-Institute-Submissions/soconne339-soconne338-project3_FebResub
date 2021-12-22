def requestName():
    # This function will request the user's name
    name = input("What's your name? \n")
    if name:
        print("Hello " + name + "`\n")


def item_selection(items, title_message, input_message):
    # The purpose of this function is to create a dictionary that each of the
    # stories can reference from. This avoids having to repeat code inside each
    # of the story functions. 
    print(title_message)
    valid_input = False

    for (i, item) in enumerate(items, start=0):
        print(i, item)
    while not valid_input:
        input_value = input(input_message)
        try:     
            num = int(input_message)
            item = items[num]
            valid_input = True
        except (ValueError, IndexError):
            print("Invalid Input\n")
            valid_input = False
        return item


def hero_story():
    names = ['Brian', 'John', 'Alan', 'Robert', 'Tom', 'George']
    transport = ['car', 'bicycle', 'walking', 'motorbike']
    locations = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Greystones']
    animals = ['dog', 'cat', 'hamster', 'rabbit']

    name = item_selection(names, "Names", "Please choose a name:")
    transport = item_selection(transport, "Transport", "Please choose a transport option")
    location = item_selection(locations, "Locations", "Please choose a location")
    animal = item_selection(animals, "animals", 'Please choose an animal')




    print("----------------------------")
    print("    |@@@@|     |####| ")
    print("    |@@@@|     |####| ")
    print("    |@@@@|     |####| ")
    print("    \@@@@|     |####/ ")
    print("     \@@@|     |###/ ")
    print("      `@@|_____|##' ")
    print("           (O)      ")
    print("        .-'''''-.   ")
    print("      .'  * * *  `. ")
    print("     :  *       *  :")
    print("    : ~ G O L D ~   : ")
    print("    : ~ A W A R D ~ : ")
    print("     :  *       *  :  ")
    print("       * * * * * *     ")
    print("        `-.....-'     ")
    story = "..............................................................\n"
    story += "..............................................................\n" 
    story += f"Once upon a time there was a boy called {name}.\n"
    story += f"{name} lived in {location} with his parents.\n"
    story += f"Everyday {name} would travel to school by {transport}.\n "
    story += f"One day {name} was going to school when he saw a large black {animal} running into the traffic.\n"
    story += f"{name} immediately jumped and saved the {animal}. Everyone cheered. {name} was a hero."
    print(story)
    morestories = input("Do you want another story ? \n")
    if morestories == "yes":
        mainFunction()
    else:
        exit()


def christmas_story():
    names = ['Emily', 'Saoirse', 'Grace', 'Hannah', 'Sheena', 'Abigail']
    familymembers = ['brother', 'sister', 'mother', 'father']
    moods = ['excited', 'nervous' , 'happy', 'anxious']
    gifts = ['toys', 'presents', 'goodies']
    
    name = item_selection(names, "Names", "Please choose a name")
    family = item_selection(familymembers, "Family members", "Please choose a family member")
    gift = item_selection(gifts, "gifts", "Please choose a gift")
    mood = item_selection(moods, "Moods", "Please choose a mood")     
    print(" .       .        _+_        .                  .             .")
    print("                  /|\ ")
    print("        .           *     .       .            .                   . ")
    print(".                i/|\i                                   .               .")
    print("      .    .     // \\*              ")
    print("                */( )\\      .                  .")
    print("        .      i/*/ \ \i             ")
    print(" .             / /* *\+\             ")
    print("      .       */// + \*\\*                   .")
    print("             i/  /^  ^\  \i    .               ... . ...")
    print(".        .   / /+/ ()^ *\ \                 ........ .")
    print("            i//*/_^- -  \*\i              ...  ..  ..               .")
    print("    .       / // * ^ \ * \ \             ..")
    print("          i/ /*  ^  * ^ + \ \i          ..     ___            _________")
    print("          / / // / | \ \  \ *\         >U___^_[[_]|  ______  |_|_|_|_|_|")
    print("   ____(|)____    |||                  [__________|=|______|=|_|_|_|_|_|=")
    print("  |_____|_____|   |||                   oo OOOO oo   oo  oo   o-o   o-o ")
    print(" -|     |     |-.-|||.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- ")
    print("  |_____|_____| ")
    print("**************************************************************************")
    print("**************************************************************************")
    print("**************************************************************************")
    print("**************************************************************************")
    print("**************************************************************************")
    print("**************************************************************************")
    print("**************************************************************************")
    print("**************************************************************************")
    story = "..............................................................\n"
    story += "..............................................................\n" 
    story += f"It was the night before Christmas and {name} was really {mood}.\n"
    story += f"She would finally get to see her {family} after so long.\n"
    story += f"{name} didn't care about {gift} from Santa Claus. She was just so happy to be able to have her {family} on Christmas day \n "
    story += f"Christmas day arrived and {name} woke up early. She was {mood} when she heard the door open and in walked her {family} \n"
    story += f"Emily ran into her {family}s arms and embraced them with the biggest hug ever.\n"
    story += "It was the best Christmas ever!"
    print(story)
    morestories = input("Do you want another story ? \n")

    if morestories == "yes":
        mainFunction()
    else:
        exit() 


def sporting_achievement():
    # List of variables
    sports = ['football', 'rugby', 'gaelic football', 'hurling']
    injuries = ['leg', 'hamstring', 'arm', 'ankle']
    cities = ['Belfast', 'Wexford', 'Waterford', 'Sligo']
    adjectives = ['fantastic', 'amazing', 'incredible', 'brilliant']
    # Define our variables for the story
    sport = item_selection(sports, "Sports", "Please choose a sport")
    injury = item_selection(injuries, "Injuries", "Please choose an injury")
    city = item_selection(cities, "Cities", "Please choose a city")
    adjective = item_selection(adjectives, "Adjectives", "Please choose an adjective")
    # Printed story

    story = "..............................................................\n"
    story += "..............................................................\n" 
    story += f" It was the day of the great {sport} final. The whole of {city} were at the stadium \n"
    story += " with 10 mins to go, both teams were level. The atmosphere was tense  \n"
    story += f" The {sport} attacker was fouled just before they scored. Because of this they had a {injury} injury \n"
    story += " The penalty was awarded and everyone was tense \n"
    story += " The home team won the match and everyone in the stadium went electric. \n" 
    story += f" It was such a {adjective} match! "
    print(story)
    morestories = input("Do you want another story ? \n")

    if morestories == "yes":
        mainFunction()
    else:
        exit() 


def joke_selection(): 
    jokes = ['doctor...doctor', 'knock knock', 'chicken crossing the road', 'Funny Limericks']

    def doctor_joke():
        print("Doctor, Doctor! I feel like a pack of cards")
        print("Sit over there and I 'll deal with you later")
        print("************************")
        print("Doctor, Doctor! I feel invisible ")
        print("Who's next! ")
        print("************************")
        print("Doctor, Doctor! I feel like a wigwam")
        print("You need to take it easy, you're too tense")

    def knockjoke():
        print("Knock Knock! ")
        print("Who's there")
        print("Nobel Who?")
        print("Nobel... that's why i knocked on the door!")
    
    def chickenjoke():
        print("Why did the chicken cross the road? ")
        print("To get to the otherside")
        print("************************")
        print("Why did the turkey cross the road?")
        print("To prove he wasn't chicken")
        print("************************")
        print("Why did the sheep cross the road?")
        print("It was the chicken's day off")

    def limerickjoke():
        print("There once was a farmer from leeds ")
        print("Who swallowed a packet of seeds")        
        print("It soon came to pass")
        print("He was covered in grass")
        print("But has all the tomatoes he needs")

    for (i, item) in enumerate(jokes, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)
    jokeChoice = int(input("What Joke type would you like to hear from the list? "))

    if jokeChoice == 0:
        doctorJoke()

    elif jokeChoice == 1:
        knockjoke()

    elif jokeChoice == 2:
        chickenjoke()

    elif jokeChoice == 3: 
        limerickjoke()            
    
    else: 
        print("Invalid Selection")
        jokeSelection()

    morejokes = input("Would you like another joke? yes/no? ")

    if morejokes == "yes":
        jokeSelection()
    else:
        morestories = input("Would you to read something else? yes/no")

        if(morestories == "yes" ):
            mainFunction()
        else:
            exit()



    



def mainFunction():

    
    
    print("Welcome to the story vault ")
    print("Please choose a story from the list below \n")

    print("1. Story about a hero character")
    print("2. Story about a christmas reunion")
    print("3. Story about a great sporting match")
    print("4. A funny joke to cheer you up")
    print("5. Exit")

    

    
    choice = int(input("Please choose a story option: 1, 2, 3, 4.............. \n"))
    

        

    

    if(choice == 1):
        heroStory()

    elif (choice == 2):
        christmasStory()

    elif (choice == 3): 

        sportingAchievement()

    elif (choice == 4):
        jokeSelection()

    elif (choice == 5):
        exit()
    
    elif ( type(choice) != int):

        print("Invalid Selection")
        mainFunction()

    else: 
        print("invalid selection")
        mainFunction()    

requestName()
mainFunction()






    
