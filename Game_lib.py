import pickle
games = {1:['FPS', 'Halo3', 'Bungee','microsoft','xbox360','2007','10','either','30.00','yes','1/15/2008','This game blows chunks'],
         2:['FPS', 'Halo2','bungee','microsoft','xbox360','2006','1','either','30.00','yes','1/15/2007','This game is bad']}

def save():
    data_file = open("game_library", "wb")
    pickle.dump(games, data_file)
    data_file.close()    

def add_new():
    new_key = len(games) + 1
    new_entry = []
    valid = False
    while not valid:
    
        
    
        games[new_key] = new_entry
        print("running add_new()")
        title = input("What is the name of the game you would like to add? ")
        if title in games:
            print("*** THAT GAME ALREADY EXISTS! ***\n")
        else:
            genre = input("   What is the genre? ")
            new_entry.append(genre)
            devoloper = input("   Who is the devoloper? ")
            new_entry.append(devoloper)
            publisher = input("   Who is the publisher? ")
            new_entry.append(publisher)
            platform = input("   What is the genre? ")
            new_entry.append(platform)
            year_released = input("   What year was it Released? ")
            new_entry.append(year_released)
            your_rating = input("   What is your rating? ") 
            new_entry.append(your_rating)
            solo_or_multi = input("   Is it solo or multi? ")
            new_entry.append(solo_or_multi)
            price = input("   Who is the devoloper? ")
            new_entry.append(price)
            have_you_played = input("   Who is the publisher? ") 
            new_entry.append(have_you_played)
            date_bought = input("   What is the date of purchase? ")
            new_entry.append(date_bought)
            games[new_key] = [genre, devoloper, publisher]
            answer = input("Is this correct? ")
            if answer.lower() in ("yes", "y"):
                valid = True            
         
        
        
    
def edit_record():   
    
    new_key = len(games) + 1
    edit_entry = []
    valid = False
    while not valid:    
       
        title = input("What is the title of the game you would like to edit? ")        
        if title in games:
            print("*** THAT GAME DOES NOT EXIST! ***\n")
        else:                                 
            genre = input("   What is the genre? ")
            new_entry.append(genre)
            devoloper = input("   Who is the devoloper? ")
            new_entry.append(devoloper)
            publisher = input("   Who is the publisher? ")
            new_entry.append(publisher)
            platform = input("   What is the genre? ")
            new_entry.append(platform)
            year_released = input("   What year was it Released? ")
            new_entry.append(year_released)
            your_rating = input("   What is your rating? ") 
            new_entry.append(your_rating)
            solo_or_multi = input("   Is it solo or multi? ")
            new_entry.append(solo_or_multi)
            price = input("   Who is the devoloper? ")
            new_entry.append(price)
            have_you_played = input("   Who is the publisher? ") 
            new_entry.append(have_you_played)
            date_bought = input("   What is the date of purchase? ")
            new_entry.append(date_bought)                          
                        
            answer = input("Is this correct? ")
            if answer.lower() in ("yes", "y"):
                valid = True                    
                games[new_key] = [genre, devoloper, publisher,platform, year_released, your_rating, solo_or_multi, price, have_you_played, date_bought, notes]
    
    
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
    name = input("  What do you want to search by? ")
    for key in games.keys():
        if name in games[key][1]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n")        


def search_by_genre():
    print("running search_by_genre()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][0]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
            
def search_by_devoloper():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][2]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
def search_by_publisher():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][3]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 


def search_by_platform():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][4]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
def search_by_year_released():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][5]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
            
def search_by_your_rating():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][6]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
def search_by_solo_or_multi():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][7]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
def search_by_price():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][8]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
def search_by_have_you_played():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][9]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
            
def search_by_date_bought():
    print("running search_by_devoloper()")
    found_one = False
    name = input("  What do you want to search for? ")
    for key in games.keys():
        if name in games[key][10]:
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
            print("----------------------")              
        if not found_one:
            print("*** NO MATCHES FOUND!***\n") 
def search():
    print('''
      Search:
       1) Genre
       2) Title
       3) Devoloper
       4) Publisher
       5) Platform
       6) Year Released
       7) Your Rating
       8) Solo or Multi
       9) Price
       10) Have you played
       11) Date Bought
   ''')
    
    choice = input("What would you like to do? ")
    if choice == "Genre":
        search_by_genre()
    elif choice == "Title":
        search_by_title()
    elif choice == "Devoloper":
        search_by_devoloper()
    elif choice == "Platform":
        search_by_platform()
    elif choice == "Year Released":
        search_by_year_released()
    elif choice == "Your Rating":
        search_by_your_rating()
    elif choice == "Solo or Multi":
        search_by_solo_or_multi()    
    elif choice == "Price":
        search_by_price()
    elif choice == "Have you played":
        search_by_have_you_played()
    elif choice == "Date Bought":
        search_by_date_bought()      
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
    

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
    1) Add Game
    2) Print All Games
    3) Search By Title
    4) Remove a Game
    5) Save Database
    6) Edit Game

    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        add_new()
    elif choice == "2":
        print_all_games()
    elif choice == "3":
        search()
    elif choice == "4":
        remove_a_game()
    elif choice == "5":
        save_database()
    elif choice == "6":
        edit_record()
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.")