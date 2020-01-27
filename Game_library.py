#!/usr/bin/python3
#Kendal Goevert
#1-27-2020

games = {1:['FPS', 'Halo3', 'Bungee','microsoft','xbox360','2007','10','either','30.00','yes','1/15/2008','This game blows chunks']}

def add_new():
    print("running add_new()")
    
def print_all_games():
    print("running print_all_games()")
    
def search_by_title():
    print("running search_by_title()")
    
def remove_a_Game():
    print("running remove_a_game()")

def save_database():
    print("running save_database()")
    
def quit():
    print("running quit()")
    
    

keep_going = True

while keep_going:
    print("""
    Welcome to Game Library.
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search By Title
    4) Remove a Game
    5) Save Database

    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        add_new()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search_by_title()
    elif choice == "4":
        remove_a_game
    elif choice == "5":
        save_database()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.")
    