
from functions import *


options_dict = {"L": "List movies",
                "T": "List movie titles",
                'D': 'Delete a movie',
                'A': 'Add a movie',
                'U': 'Update a movie',
                'Q': 'Quit this program',
                } 
opt = None

movieDatabase = {
1: {
        "title": "Eternal Sunshine of the Spotless Mind",
        "genre": "Sci-Fi",
        "date_seen": "",
        "rating": ""
    },
2: {
        "title": "About Time",
        "genre": "Drama",
        "date_seen": "2016/2/14",
        "rating": "5"
    },
3: {
        "title": "The Matrix",
        "genre": "Action",
        "date_seen": "1999/12/01",
        "rating": "5"
    }
}
all_movie_genres = ("", "Action", "Adventure", "Cartoon", "Comedy", "Drama", "Fantasy", "Sci-Fi", "Romance", "Thriller")
while True:
    print("What would you like to do?")
    print_options(options_dict) 
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() 

    if opt not in options_dict:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected {opt} to {options_dict[opt]}.") 

    if opt == 'L':
        print_movies_dict(movieDatabase)
        
    elif opt == 'T':
        print_movies_dict(movieDatabase, title_only = True)

    elif opt == 'D':
        delete_helper(movieDatabase)

    elif opt == 'A':
        add_helper(movieDatabase, all_movie_genres)
        
    elif opt == 'U':
        update_helper(movieDatabase, all_movie_genres)
        
    if opt == 'Q': 
        print("Goodbye!\n")
        break



    
    input("::: Press Enter to continue")

print("Have a nice day!")
