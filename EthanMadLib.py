print ("Welcome to the mad lib project.")
name = input("What is your name?")
place = input("Name a place.")
verb = input("Name a verb.")
place_two = input("Name a different place.")
noun = input("Name a noun.")
name_two = input("What is another name?")

print("%s went to %s to %s. The next day %s went to %s to get %s for %s. They became friends and lived happily ever after. Until they got mauled by a bear and died." %(name, place, verb, name, place_two, noun, name_two))

text_file = open("Output.txt", "w")
text_file.write("%s went to %s to %s. The next day %s went to %s to get %s for %s. They became friends and lived happily ever after. Until they got mauled by a bear and died." %(name, place, verb, name, place_two, noun, name_two))
text_file.close()
