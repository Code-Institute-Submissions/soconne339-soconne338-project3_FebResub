def request_name():
    # This function will request the user's name which will then be
    # printed before the list of stories is
    name = input("What's your name?: ")
    if name:
        print(f"Hello {name}")


def item_selection(items, title_message, input_message):
    # The purpose of this function is to create a dictionary that each of the
    # stories can reference from. This avoids having to repeat code inside each
    # of the story functions.
    print(title_message)
    valid_input = False

    for (i, item) in enumerate(items, start=1):
        print(i, item)

    while not valid_input:
        input_value = input(input_message)
        try:
            num = int(input_value)
            item = items[num-1]
            valid_input = True
        except (ValueError, IndexError):
            # throws exception so that
            # if a string or value greater than list index
            print("Invalid Input\n")
            valid_input = False
        return (item, num)


def hero_story():
    # Story 1
    # Python lists are for each of the nouns as part of the story
    names = ['Brian', 'John', 'Alan', 'Robert', 'Tom', 'George']
    transport = ['car', 'bicycle', 'walking', 'motorbike']
    locations = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Greystones']
    animals = ['dog', 'cat', 'hamster', 'rabbit']
    #
    #
    name, _ = item_selection(names, "Names", "Please choose a name: ")
    # Uses dictionary to create variable for name
    transport, _ = item_selection(transport, "Transport",
                                  "Please choose a transport option: ")
    # Uses dictionary to create variable for transport
    location, _ = item_selection(locations, "Locations",
                                 "Please choose a location: ")
    # Uses dictionary to create variable for location
    animal, _ = item_selection(animals, "animals", 'Please choose an animal: ')
    # Uses dictionary to create variable for animal
    #
    story = "..............................................................\n"
    story += "..............................................................\n"
    story += f"Once upon a time there was a boy called {name}.\n"
    story += f"{name} lived in {location} with his parents.\n"
    story += f"Everyday {name} would travel to school by {transport}.\n "
    story += f"One day {name} was going to school" + \
        f" when he saw a large black {animal}" + \
        " running into the traffic.\n"
    story += f"{name} immediately jumped and saved the {animal}." + \
        f" Everyone cheered. {name} was a hero."
    print(story)
    morestories, _ = play_again()
    if morestories == "yes":
        # conditional statement asking user
        # if they want to hear another story
        # which will call the main_function() function
        main_function()
    else:
        # If user inputs anything other than 'yes' then the program will exit
        exit()


def christmas_story():
    # Story 2
    # various lists containing the variables for the story
    names = ['Emily', 'Saoirse', 'Grace', 'Hannah', 'Sheena', 'Abigail']
    familymembers = ['brother', 'sister', 'mother', 'father']
    moods = ['excited', 'nervous', 'happy', 'anxious']
    gifts = ['toys', 'presents', 'goodies']
    #
    #
    name, _ = item_selection(names, "Names", "Please choose a name: ")
    # Uses dictionary to create name variable
    family, _ = item_selection(familymembers,
                               "Family members",
                               "Please choose a family member: ")
    # Uses dictionary to create family member variable
    gift, _ = item_selection(gifts, "gifts", "Please choose a gift: ")
    # Uses dictionary to create gift variable
    mood, _ = item_selection(moods, "Moods", "Please choose a mood: ")
    # Uses dictionary to create mood varaible
    #
    # Print story using the variables created above from the list objects

    story = "..............................................................\n"
    story += "..............................................................\n"
    story += "It was the night before Christmas" + \
        f" and {name} was really {mood}.\n"
    story += f"She would finally get to see her {family} after so long.\n"
    story += f"{name} didn't care about the {gift}." + \
        "She was just so happy to be able to" + \
        f" have her {family} on Christmas day \n "
    story += f"The day arrived and {name} woke up early." + \
        f"She was so excited when she heard the door open" + \
        f" snd in walked her {family} \n"
    story += f"Emily ran into her {family}s arms and" + \
        " embraced them with the biggest hug ever.\n"
    story += "It was the best Christmas ever!"
    print(story)

    morestories, _ = play_again()
    if morestories == "yes":   # ask user if they want another story
        main_function()   # if yes
    else:
        exit()   # if user inputs anything other than yes then exit program


def play_again():
    options = ["yes", "no"]
    return item_selection(options, "", "Do you want another story? ")


def play_again_jokes():
    options = ["yes", "no"]
    return item_selection(options, "", "Do you want another joke?")


def sporting_achievement():
    # List of variables
    sports = ['football', 'rugby', 'gaelic football', 'hurling']
    injuries = ['leg', 'hamstring', 'arm', 'ankle']
    cities = ['Belfast', 'Wexford', 'Waterford', 'Sligo']
    adjectives = ['fantastic', 'amazing', 'incredible', 'brilliant']
    # Define our variables for the story
    sport, _ = item_selection(sports, "Sports", "Please choose a sport")
    injury, _ = item_selection(injuries, "Injuries", "Please choose an injury")
    city, _ = item_selection(cities, "Cities", "Please choose a city")
    adjective, _ = item_selection(adjectives, "Adjectives",
                                  "Please choose an adjective")
    # Printed story

    story = "..............................................................\n"
    story += "..............................................................\n"
    story += f" It was the day of the great {sport} final." + \
        f" The whole of {city} were at the stadium \n"
    story += " with 10 mins to go, both teams were level." + \
        " The atmosphere was tense  \n"
    story += f" The {sport} attacker was fouled" + \
        " just before they scored." + \
        f" Because of this they had a {injury} injury \n"
    story += " The penalty was awarded and everyone was tense \n"
    story += " The home team won the match" + \
        " and everyone in the stadium went electric. \n"
    story += f" It was such a {adjective} match! "
    print(story)

    morestories, _ = play_again()
    if morestories == "yes":
        main_function()
    else:
        exit()


def joke_selection():
    # joke selection function
    # list of joke types
    jokes = ['doctor...doctor', 'knock knock',
             'chicken crossing the road', 'Funny Limericks']

    def doctor_joke():
        # function which prints the doctor, doctor joke
        print("Doctor, Doctor! I feel like a pack of cards")
        print("Sit over there and I 'll deal with you later")
        print("************************")
        print("Doctor, Doctor! I feel invisible ")
        print("Who's next! ")
        print("************************")
        print("Doctor, Doctor! I feel like a wigwam")
        print("You need to take it easy, you're too tense")

    def knock_joke():
        # function which prints the knock knock joke
        print("Knock Knock! ")
        print("Who's there")
        print("Nobel Who?")
        print("Nobel... that's why i knocked on the door!")

    def chicken_joke():
        # function which prints the chicken cross the road joke
        print("Why did the chicken cross the road? ")
        print("To get to the otherside")
        print("************************")
        print("Why did the turkey cross the road?")
        print("To prove he wasn't chicken")
        print("************************")
        print("Why did the sheep cross the road?")
        print("It was the chicken's day off")

    def limerick_joke():
        # function which prints the limerick joke
        print("There once was a farmer from leeds ")
        print("Who swallowed a packet of seeds")
        print("It soon came to pass")
        print("He was covered in grass")
        print("But has all the tomatoes he needs")

    for (i, item) in enumerate(jokes, start=0):
        print(i, item)
    jokeChoice = int(input("What Joke type would you like to hear" +
                           "from the list? "))
    # list all of the joke with the number proceeding the choice

    if jokeChoice == 0:
        doctor_joke()

    elif jokeChoice == 1:
        knock_joke()

    elif jokeChoice == 2:
        chicken_joke()

    elif jokeChoice == 3:
        limerick_joke()

    else:
        print("Invalid Selection")
        joke_selection()

    morejokes, _ = play_again_jokes()

    if morejokes == "yes":
        joke_selection()
    else:
        morestories, _ = play_again()

        if morestories == "yes":
            main_function()
        else:
            exit()


def main_function():
    # Main function which calls all the other functions
    # List of all the stories in program

    options = [
        "Story about a hero character",
        "Story about a christmas reunion",
        "Story about a great sporting match",
        "A funny joke to cheer you up",
        "Exit"
        ]

    value, story_choice = item_selection(options,
                                         "Welcome to the story vault",
                                         "Please choose a story option: ")

    if story_choice == 1:
        hero_story()
    elif story_choice == 2:
        christmas_story()
    elif story_choice == 3:
        sporting_achievement()
    elif story_choice == 4:
        joke_selection()
    elif story_choice == 5:
        exit()

request_name()
main_function()
