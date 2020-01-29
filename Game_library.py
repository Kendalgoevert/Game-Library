#!/usr/bin/python3
#Kendal Goevert
#1-27-2020

import pickle
games = {1:['FPS', 'Halo3', 'Bungee','microsoft','xbox360','2007','10','either','30.00','yes','1/15/2008','This game blows chunks'],
         2:['FPS', 'Halo2','bungee','microsoft','xbox360','2006','1','either','30.00','yes','1/15/2007','This game is bad']}

def save():
    data_file = open("game_library", "wb")
    pickle.dump(games, data_file)
    data_file.close()    

def add_new():
    print("running add_new()")
    
def print_all_games():
    print("running print_all_games()")
    
    key_list = games.keys()
    
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Devoloper: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("Platform: ", games[key][4])
        print("Year Released: ",games[key][5])
        print("Your Rating: ",games[key][6])
        print("Solo or Multi: ",games[key][7])
        print("Price: ",games[key][8])
        print("Have you played: ",games[key][9])
        print("Date Bought: ",games[key][10])
        print("Notes: ",games[key][11])
        print("----------------------")    
    
def search_by_title():
    print("running search_by_title()")
    found_one = False
    name = input("  What is the name of the game? ")
    for key in games.keys():
        if name == games[key][1]:
            found_one = True
            print()
            print("Genre: ", games[key][0])
            print("Title: ", games[key][1])
            print("Devoloper: ", games[key][2])
            print("Publisher: ", games[key][3])
            print("Platform: ", games[key][4])
            print("Year Released: ",games[key][5])
            print("Your Rating: ",games[key][6])
            print("Solo or Multi: ",games[key][7])
            print("Price: ",games[key][8])
            print("Have you played: ",games[key][9])
            print("Date Bought: ",games[key][10])
            print("Notes: ",games[key][11])
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n")        
    
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
        print_all_games()
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
    