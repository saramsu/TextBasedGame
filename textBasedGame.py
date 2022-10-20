import time
from typing_extensions import Required 

#Possible answers
AnswerA = ["A", "a"]
AnswerB = ["B", "b"]
AnswerC = ["C", "c"]

Required = ("Please only write the letter without additional characters."
        "Just A or a, for example.")

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
elif choice in AnswerC:
    option_GoAlong()
else: 
    print(required)
    one()

def option_HelpHer():
    print("\n Now that she gets in the car starts looking at you very strange"
"and her eyes are lighting. You are very nervous." "You remember a movie where"
"the eyes of the vampire look exactly the same as hers. You will:")
print("""
    A Offer her a garlic sandwich you had in your pocket.
    B You try to avoid those ideas, and start a conversation with her.
    C You ask her to get off the car immediately.
""")
choice = input (">>> ") #Second choice
if choice in AnswerA:
    print ("The girl seems to be grateful and starts eting the sandwich eagerly"
    "you look at her and she has already eaten the sandwich and is crestfallen,"
    "as if she were repentant or meditative. When you are close to arrive to the village"
    "She starts crying and confess you that all the people in her village are cursed,"
    "and they transform into wolves during the night, she was the bait for you to be their"
    "dinner. And shows you a shortcut. You adopted her and now she is half your pet, half your"
    "daughter." 
    "The end.")
elif choice in AnswerB:
    "You finally arrive to the village and all the villagers are surrounding you."
    "The girl trnasforms into a woolf and now there is no loophole, you will be their dinner."
    "The end."
elif choice in AnswerC:
    "You see her angry expression, and how she has started to transform into a wolfgirl."
    "You Decide to leave the car. Y/N?"
    choice = input(">>> ")
    if choice in yes:
        print ("Now that the girl is trapped in the car, you will just wait a couple of"
        "hours till dawn, when the girl can not transform into a woolf and you will have you car"
        "again to go home. You will never take this path again for the rest of your life." 
        "The end.☻")
    if choice in no:
        print ("figths with her till the dawn, and now that she can not turn into a woolf"
        "you get her out off the car and return home a little hurt. You will never"
        "take this path again for the rest of your life"
        "The end.")


def option_DonotStop():
    print("Behind you the girl transforms into a woolf and starts seeking you," 
    "running very fast trying to chatch you."
    "As soon as you realize this you speed up untill arrive to the nearest village."
    "Y/N?")
    if choice in yes:
        print ("All the villagers are awaiting for you and now you will be their dinner."
        "The end.")
    if choice in no:
        print ("You go back home and now that you want to tell someone... nobody believes you"
        "but now that you are safe, you decide to write your story. Y/N")
        if choice in yes: 
            print("Your book becomes a bestseller and now you are millionaire."
            "The end.♥")
        if choice in no:
            print("After a couple of months of nightmers with this event, you go to therapy"
            "and your therapist recommends tou you to write your story. You follow this advice."
            "The book becomes a best seller and you are millionaire now."
            "The end.")

def option_GoAlong():
    print ("You finally arrive to the village and all the villagers are surrounding you."
    "The girl trnasforms into a woolf and now there is no loophole, you will be their dinner."
    "The end."
    "Do you want to play again? Y/N?")
    if choice in yes:
        one()
    if choice in no:
        print("See you later! Thanks for playing ☺.")

   






