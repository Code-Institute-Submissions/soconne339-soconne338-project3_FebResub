def requestName():
    name = input("What's your name? \n")
    if name:
        print("Hello " + name +"`\n")



def heroStory():



    names = ['Brian', 'John', 'Alan', 'Robert', 'Tom', 'George']
    transport = ['car', 'bicycle', 'walking', 'motorbike']
    locations = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Greystones']
    animals =['dog', 'cat', 'hamster', 'rabbit']


    def nameSelection():
        print("Names")

        for (i, item) in enumerate(names, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
            print(i, item)
        
        num = int(input("Please choose a Name \n"))

        return names[num]

    def transportSelection():
        print("Transport options")

        for (i, item) in enumerate(transport, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
            print(i, item)
        
        num = int(input("Please choose a transport option \n"))

        return transport[num]    




    def locationSelection():
        
        print("Locations")

        for (i, item) in enumerate(locations, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
            print(i, item)
        
        num = int(input("Please choose a location \n"))

        return locations[num]


    def animalSelection():
        print("Animals")

        for (i, item) in enumerate(animals, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
            print(i, item)
        
        num = int(input("Please choose an Animal \n"))

        return animals[num]

    location = locationSelection()
    name = nameSelection()
    transport = transportSelection()
    animal = animalSelection()

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
        exit(); 


def christmasStory():

    names =         ['Emily', 'Saoirse', 'Grace', 'Hannah', 'Sheena', 'Abigail']
    familymembers = ['brother', 'sister', 'mother', 'father']
    moods =         ['excited', 'nervous' , 'happy', 'anxious']
    gifts =         ['toys', 'presents', 'goodies']

    def nameSelection():
            print("Names")

            for (i, item) in enumerate(names, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)
            
            num = int(input("Please choose a Name? \n"))

            return names[num]

    def familySelection():
            print("Family Members   ")

            for (i, item) in enumerate(familymembers, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)
            
            num = int(input("Please choose a family member? \n"))

            return familymembers[num]
        
    def moodSelection():
            print("Moods")

            for (i, item) in enumerate(moods, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)
            
            num = int(input("Please choose a mood? \n"))

            return moods[num]

    def giftSelection():
            print("Gifts")

            for (i, item) in enumerate(gifts, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)
            
            num = int(input("Please choose a gift? \n"))

            return gifts[num]     

        

    name = nameSelection()
    family = familySelection()
    gift = giftSelection()
    mood = moodSelection()
        
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
    story += f"It was the best Christmas ever!"


    print(story)

    morestories = input("Do you want another story ? \n")

    if morestories == "yes":
        mainFunction()

    else:
        exit(); 


def sportingAchievement():

    sports = ['football', 'rugby', 'gaelic football', 'hurling']
    injuries = ['leg', 'hamstring', 'arm', 'ankle']
    cities = ['Belfast', 'Wexford', 'Waterford', 'Sligo']
    ajectives = ['fantastic', 'amazing', 'incredible', 'brilliant']


    def sportsSelection():
        print("Sports options")

        for (i, item) in enumerate(sports, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)

        num = int(input(" Please choose a sport? \n"))

        return sports[num]        

    def injurySelection():
        print("Injury options")

        for (i, item) in enumerate(injuries, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)

        num = int(input(" Please choose an injury option? \n"))

        return injuries[num]    

    def citySelection():
        print(" Cities")
        
        for (i, item) in enumerate(cities, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)

        num = int(input(" Please choose a city? \n"))

        return cities[num]


    def adjectiveSelection():
        print(" Adjectives")
        
        for (i, item) in enumerate(ajectives, start=0):    #code gotten from https://stackoverflow.com/questions/34753872/how-do-i-display-the-the-index-of-a-list-element-in-python
                print(i, item)

        num = int(input(" Please choose a city? \n"))

        return ajectives[num]


    sport = sportsSelection()
    injury = injurySelection()
    city = citySelection()
    adjective = adjectiveSelection()

    


    story = "..............................................................\n"
    story += "..............................................................\n" 
    story += f" It was the day of the great {sport} final. The whole of {city} were at the stadium \n"
    story += f" with 10 mins to go, both teams were level. The atmosphere was tense  \n"
    story += f" The {sport} attacker was fouled just before they scored. Because of this they had a {injury} injury \n"
    story += f" The penalty was awarded and everyone was tense \n"
    story += f" The home team won the match and everyone in the stadium went electric. \n" 
    story += f" It was such a {adjective} match! "


    print(story)

    morestories = input("Do you want another story ? \n")

    if morestories == "yes":
        mainFunction()

    else:
        exit();  



def jokeSelection(): 

    jokes = ['doctor...doctor', 'knock knock', 'chicken crossing the road', 'Funny Limericks']

    def doctorJoke():

        print("DOCTOR JOKE")

    def knockjoke():

        print("Knock Joke")
    
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

        doctorjoke()

    elif jokeChoice == 1:

        knockjoke()

    elif jokeChoice == 2:

        chickenjoke()

    elif jokeChoice == 3: 

        limerickjoke()            

    
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
    print("4. Exit")

    

    
    choice = int(input("Please choose a story option: 1, 2 or 3.............. \n"))
    

        

    

    if(choice == 1):
        heroStory()

    elif (choice == 2):
        christmasStory()

    elif (choice == 3): 

        sportingAchievement()

    elif (choice == 4):

        exit()
    
    elif ( type(choice) != int):

        print("Invalid Selection")
        mainFunction()

    else: 
        print("invalid selection")
        mainFunction()    

requestName()
mainFunction()






    
