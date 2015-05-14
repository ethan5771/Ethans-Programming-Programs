import random
list_1 = "You are"
list_2 = ["Beautiful","Amazing", "Perfect", "Kind-hearted", "Caring","Nice","Sweet","Fun","Interesting", "Exciting", "Funny","Reliable","Great","Awesome"]
list_3 = ["Smart","Hot", "Cute", "Sexy", "Joyful", "Important","Outgoing","Athletic","Loveable","Talented","Gifted","Rad","Adorable","Admirable","Fantastic"]
list_4 = ["Logical","Imaginitive", "Noble", "Keen", "Knowledgeable", "Respectful","Super","Generous","Selfless","Special","Trustworthy","Positive","Happy","Eager","Humble"]

another = True
while another == True:
    print (list_1 + " " + random.choice(list_2) + " " + random.choice(list_3) + " " + "And" + " " + random.choice(list_4))
    another1 = input("Would you like another complement")
    if another1 == "Yes" or another1 == "yes":
        another = True
    elif another1 == "no" or another1 == "No":
        another = False
    
