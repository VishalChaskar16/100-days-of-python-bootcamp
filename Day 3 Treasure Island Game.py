###Treasure Island game

print('''
                   ,.ood888888888888boo.,
              .od888P^""            ""^Y888bo.
          .od8P''   ..oood88888888booo.    ``Y8bo.
       .odP'"  .ood8888888888888888888888boo.  "`Ybo.
     .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
    d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
  .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
 d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
.8P .88P            """"            """"            Y88. Y8.
88  888                                              888  88
88  888                                              888  88
88  888.        ..                        ..        .888  88
`8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
 Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
  `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
    Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
     `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
       `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
          `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
              `^Y888bo.,            ,.od888P^'
                   "`^^Y888888888888P^^'"
                        
      ''')

print("Welcome to Vishal Treasure Island")
print("Your mission is to find the treasure")

## Creating a variable choice1 that will take the input as 2 choices Left or Right
## Using the \ helps to escape the string in word 'You're' and sees the whole input as text
## Using the lower() function to ensure the input entered by the user is converted to lowercase to avoid error

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

## Here instead of using 'right' as Game over we kept it in else statement as blank so that even if the user gives any other response other than left or write it will still give game over as ouput 
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red one yellow one blue. Which color do you choose? ").lower()
        if choice3 == ("red"):
            print("Its a room full of fire. Game over.")
        elif choice3 == ("yellow"):
            print("Its a room full of manhunters. Game over. ")
        elif choice3 == ("blue"):
            print("You found the treasure. You Won!!!")
        else:
            print("You chose a door that doesn't exists. Game over.")

    else:
        print("You got attacked by a zombie. Game over. ")
else:
    print("You fell into a hole. Game over.")


