import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.pi)
# random.random()0.000000-0.999999..... aber 1 nicht inkludiert

random_float = random.random()
print(random_float)

random_float * 5
# 0.00000....-4.999999..... 0-5 aber 5 nicht inkludiert

# wäre bei lovescore programm möglich gewesen

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")

# Münze werfen
value = random.randint(0, 1)
if value == 0:
    print("Tails")
else:
    print("Head")

# Listenübung
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#mit eckigen Klammern ein Datenelement nach der Reihenfolge der Liste aussuchen, startend bei 0. Datenstrukturen starten normalerweise immer bei 0.
print(states_of_america[1])
#wenn man Elemente rausholen will den index in eckige klammern setzen. Kann man auch wie Variable verwenden. z.B x=states_of_america[2] äquivalent zu string subscription y= string[position von 0 weg]
states_of_america[2]
# negativer wert auch möglich, dann wird am Ende begonnen
states_of_america[-1] #ist gleich letztes Element der Liste. Man beginnt deshalb von -1 zu zählen am Ende weil es -0 nicht gibt in der Mathematik
#Man kann einzelne Elemente mit dem Index auch ansprechen und verändern. Z.B.:
states_of_america[1] = "Pencilvania"         #wenn z.B. falsch geschrieben o.Ä.

#man kann Dinge auch am Ende der Liste hinzufügen (einzelnes Element):

states_of_america.append("Philippland")
#oder ganze Liste mit

states_of_america.extend(["1land", "2land", ....])

print(states_of_america)


#Übung: Wer bezahlt das Essen ? (random)
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_of_list = len(names)-1
#print(count_of_list)  Werte überprüfen
winner = random.randint(0,count_of_list)  # auch möglich: die -1 in die random Funktion also: winner = random.randint(0,count_of_list-1) und nur len(names)
#print(winner) Werte überprüfen
print(names[winner]+ " is going to buy the meal today!")

#oder python dokumentation zur random Funktion  winner = random.choice(names)  statt dem ganzen code oben.

#Nested lists

states_of_america_new = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(len(states_of_america_new))
num_of_states = len(states_of_america_new)
print(states_of_america_new[num_of_states-1]) # -1 weil es sonst zu out of range error kommt. es sind zwar 50 Elemente in der Liste aber Zählung beginnt bei 0 (index). Daher 0-49 und das Element mit dem index 50 gibt es nicht.

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]


fruits =["Strawberries", "Nectarines", "Apples","Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes","Celery","Potatoes"]

dirty_dozen_nested=[fruits,vegetables]
print(dirty_dozen_nested)

#Code Exercise TreasureMap:
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])-1
vertical = int(position[1])-1

map[vertical][horizontal]="X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


#import random          (wenn es vorher noch nicht importiert wurde)
#RockPaperScissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇



hands = [rock, paper, scissors]


player = int(input("Welcome to rock, paper, scissors! Please make your choice: 0=rock, 1=paper, 2=scissors\n"))
if 0 <= player <= 2:
    print(hands[player])

    print("Now it is the turn of your enemy:")
    enemy = random.randint(0,2)
    print(f"The computer chose {enemy}\n{hands[enemy]}")

    if player == enemy:
        print("It's a tie!")
    elif player == 0 and enemy == 2:
        print("You win!")
    elif player == 1 and enemy == 0:
        print("You win!")
    elif player == 2 and enemy == 1:
        print("You win!")
    else:
        print("You lose!")

else:
    print("You typed in an invalid 