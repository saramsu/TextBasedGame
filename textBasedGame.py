#Possible answers
AnswerA = ["A", "a"]
AnswerB = ["B", "b"]
AnswerC = ["C", "c"]

#The story starts with the section named "one"
def one():
    print("Hi there! Welcome to the adventure")
    name = input('Enter your preferred name:')
    print("Welcome to the adventure + name+!")
    print("\n You have been driven during the entire night"
    "and suddenly a girl with long and disheveled hair asks you to carry"
    "her to the nearest village. What are you going to do?")

print(""" 
        A pick up the girl.
        B You pass by and don\'t pick up the girl.
        C You tell her that you don\'t know where you are and ask her to help you.
""")
choice = input (">>> ") #First choice
if choice in AnswerA:
    option_HelpHer()
elif choice in AnswerB:
    option_DonotStop()
    print('Behind you the girl transforms into a woolf and starts seeking you, running very fast trying to chatch you.')
elif choice in AnswerC:
    option_GoAlong()

def option_HelpHer():
    print("\n Now that she gets in the car starts looking at you very strange"
"and her eyes are lighting. You are very nervous." "You remember a movie where"
"the eyes of the vampire look exactly the same as this girl. You will:")
print("""
    A Offer her a garlic sandwich you had in your pocket.
    B You try to avoid those ideas, and start a conversation with her.
    C You ask her to get off the car immediately.
""")
choice = input (">>> ") #Second choice
if choice in AnswerA:
    print ("The girl seems to be grateful and starts eting the sandwich eagerly"
    "you look at her and she has already eaten the sandwich and is crestfallen,"
    "as if she were repentant or meditative. As soon as you arrive to the next village"
    "She starts crying and confess you that all the people in her village are cursed,"
    "and they transform into wolves during the night, she was the bait for you to be their"
    "dinner. And shows you a shortcut. You adopted her and now she is half your pet, half your"
    "daughter." 
    "☻ The end."
elif choice in AnswerB:
    "You finally arrive to the village and all the villager are surrounding you."
    "The gir trnasforms into a woolf and now there is no loophole, you will be their dinner."
    "The end."
elif choice in AnswerC:
    "You see her angry expression, and how she has stated to transform into a wolfgirl."
    "You will:"



def option_HelpHer():
    print("\n Now that she gets in the car starts looking at you very strange"
"and her eyes are lighting. You are very nervous." "You remember a movie where"
"the eyes of the vampire look exactly the same as this girl. You will:")
print("""
    A Offer her a garlic sandwich you had in your pocket.
    B You try to avoid those ideas, and start a conversation with her.
    C You ask her to get off the car immediately.
""") 
choice = input (">>> ") #Third choice
if choice in AnswerA:

elif choice in AnswerB:
    

elif choice in AnswerC:


def option_DonotStop():
    print("\n Now that she gets in the car starts looking at you very strange"
"and her eyes are lighting. You are very nervous." "You remember a movie where"
"the eyes of the vampire look exactly the same as this girl. You will:")
print("""
    A Offer her a garlic sandwich you had in your pocket.
    B You try to avoid those ideas, and start a conversation with her.
    C You ask her to get off the car immediately.
""")
choice = input (">>> ") #forth choice
if choice in AnswerA:

elif choice in AnswerB:
    

elif choice in AnswerC:

def  option_GoAlong():
    print("\n Now that she gets in the car starts looking at you very strange"
"and her eyes are lighting. You are very nervous." "You remember a movie where"
"the eyes of the vampire look exactly the same as this girl. You will:")
print("""
    A Offer her a garlic sandwich you had in your pocket.
    B You try to avoid those ideas, and start a conversation with her.
    C You ask her to get off the car immediately.
""")
choice = input (">>> ") #fifth choice
if choice in AnswerA:

elif choice in AnswerB:
    

elif choice in AnswerC:



