print("Hey there pal!")
you_like_animals = input("Do you like animals? Y/N")
if you_like_animals == "y" or you_like_animals == "Y":
    print("Good!")
    favorite_animal = input("What is your favorite out of these three? Dog, Cat, or Moose?")
    if favorite_animal == "Dog" or favorite_animal == "dog":
          print("Oh! Cool")
    elif favorite_animal == "Cat" or favorite_animal == "cat":
          print("Thats sweet!")
    elif favorite_animal == "Moose" or favorite_animal == "moose":
          print("Mine too!")
    else:
          print("Im sorry, i didn't understand that.")
elif you_like_animals == "N" or you_like_animals == "n":
    print("Oh. Thats impossible.")
    
else:
    print("I'm sorry, i didn't understand that")
you_like = input("What do you like more, School or Working?")
if you_like == "School" or you_like == "school":
    print("Nice to know.")
    your_school = input("What school do you go to?")
    if your_school == "Grove City" or your_school == "grove city":
        print("Oh me too!")
    elif your_school == "lakeview" or your_school == "Lakeview":
        print("Interesting, thats where im going next year!")
    else:
        print("Sweet!")
elif you_like == "Working" or you_like == "working":
    you_work = input("Where do you work?")
    if you_work == "Nowhere" or you_work == "nowhere":
        print("Haha same!")
    else:
        print("That's cool.")
else:
    print("You didn't make yourself clear on that one.")
you_food = input("Ok, last question. what is your favorite food?")
if you_food == "Tacos" or you_food == "tacos":
    print("Good answer, mine too.")
elif you_food == "Cake" or you_food == "cake":
    print("I loove cake.")
    fav_cake = input("What's your favorite kind of cake")
    if fav_cake == "Chocolate" or fav_cake == "chocolate":
        print ("We have a lot in common")
    elif fav_cake == "vanilla" or fav_cake == "Vanilla":
        print ("I like vanilla, but my favorite is chocolate.")
else:
    print("Sweet")
print("Thanks for talking to me!")
