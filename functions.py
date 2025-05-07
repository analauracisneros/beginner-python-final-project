def print_options(param_dict):
    """
    Given a dictionary with the options,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    before and after the key-value pairs.
    """
    #Only prints if argument is dictinary
    if type(param_dict) == dict:
        print('.............................................')
        for key, value in param_dict.items():
            print(f' |{key}| {value}')#Formats the key and value in dictionary for certain aesthetic
        print('.............................................')
    
def print_movie(movie_dict, title_only = False): 
    """
    param: movie_dict (dict) - holds the movie info
            Expected keys are:
            ("title", "genre", "date_seen", "rating")
    param: title_only(bool) - controls if to display
            only the movie title or the full information

    Displays the formatted movie information.
    If "genre", "date_seen", or "rating" is empty, then
    that field is not displayed.

    The order of the keys in the dictionary should not
    affect the resulting output: e.g., "rating" could
    be stored before the "genre".

    If the set of the provided movie keys do not match the
    expected keys, the function just prints the warning and
    exits the call (without returning anything):    
        ("WARNING: movie keys do not match what's expected.")
        ("Expected:", ...)
        ("Received:", ...)
    Otherwise, if the keys match, the function prints the
    movie info according to the specification.
    At the end, displays a decorator made up of 45 dots.

    returns: None
    """
    ExpectedTup = ('title', 'genre', 'date_seen', 'rating')
    #Whether dictionary is empty
    if movie_dict == {}:
        print("WARNING: movie keys do not match what's expected.")
        print("Expected: ('title', 'genre', 'date_seen', 'rating')")
        print("Received: dict_keys([])")
    else:
        if title_only == False:#Prints out title and categories
            for key, values in movie_dict.items():
                    if values != '':
                        if key == ExpectedTup[2]:
                            print(f'| Watched on {movie_dict[ExpectedTup[2]]}')#Ensures the date seen follows after non-empty strings
                        elif key == ExpectedTup[3]:
                            print(f'| Rated {movie_dict[ExpectedTup[3]]}')#Ensures the rating follows after date seen
                        else:
                            print(f'| {values}')
            print('.............................................')
        else:#Only prints out title
            print(f'| {movie_dict[ExpectedTup[0]]}')

def print_movies_dict(movie_collection, title_only = False, show_ID = False):
    """
    param: movie_collection (dict) - holds the movie database;
            maps an integer ID to each movie object (also a
            dictionary)
    param: title_only(bool) - controls if to display
            only the movie title or the full information
    param: show_ID(bool) - controls if to display the key,
            i.e., the movie ID that's stored in the collection;
            uses print(f"{...:2d}", end=" ") to position the ID

    Helper functions:
    - print_movie

    The function displays the movie information according
    to the specifications. Keeps track of how many movies
    were displayed and at the end reports this info by
    printing "Showing {...} results."

    returns:
        the count of how many movies were displayed
    """
    #Whether dictionary is empty
    if movie_collection == {}:
        print("Showing 0 results.")
    else:
        #Goes through dictionary and prints songs with certain format
        if title_only == True: #Whether user wants the title only or not
            if show_ID == True: #Whether user wants the ID or not
                for key in movie_collection.keys():
                    print(f'{key:2d}', end=' ')
                    print_movie(movie_collection[key], title_only = True)

            else:
                for key in movie_collection.keys():
                    print_movie(movie_collection[key], title_only = True)
        else:
            if show_ID == True:
                for key in movie_collection.keys():
                    print(f'{key:2d}', end=' ')
                    print_movie(movie_collection[key], title_only = False)

            else:
                for key in movie_collection.keys():
                    print_movie(movie_collection[key], title_only = False)
        #Prints the results at bottom
        print(f'Showing {len(movie_collection)} results.')
        
def delete_movie(movie_collection, key_str):
    """
    param: movie_collection (dict) - holds the movie database;
            maps an integer ID to each movie object (also a
            dictionary)
    param: key_str (str) - a string that is supposed to represent
            an integer ID that corresponds to a key in the
            collection

    returns:
    0 - if the collection is empty.
    -1 - if the provided parameter is not a string or the string
    does not hold a valid integer

    Otherwise, converts the provided string to an integer and
    returns None if the ID does not map into a key in the collection
    or returns the item (dict) that was removed from the
    provided collection.
    """
    #Whether dictionary is empty
    if movie_collection == {}:
        return 0
    elif type(key_str) != str or key_str.isdigit() == False:
        return -1
    else:
        key_int = int(key_str)#Converts to integer
        if key_int not in movie_collection:
            return None
        else:
            return movie_collection[key_int]#Returns the value of certain key
def delete_helper(movie_collection):
    """
    param: movie_collection (dict) - holds the movie database;
            maps an integer ID to each movie object (also a
            dictionary)

    Helper functions:
    - print_movies_dict
    - print_movie
    - delete_movie
    """
    if movie_collection == {}:
        print("WARNING: there is nothing to delete.")
        return 0

    print("Which movie would you like to delete?")
    print_movies_dict(movie_collection, title_only = True, show_ID = True)#Prints movies for user to choose from
    print("::: Enter the number corresponding to the movie ID")
    print("::: or enter A to delete all movies in the collection.")
    delete_opt = input("> ")
    if delete_opt == "A": ### only accept upper-case
        clearedMovies = movie_collection.clear() # Delete all movies
        print("Success! Deleted all movies!")
        return clearedMovies


    result = delete_movie(movie_collection, str(delete_opt))
    if type(result) == dict:#Checks if the function returns a dictionary
        print("Success! Deleted an entry:")
        new_movie_collect = movie_collection.pop(int(delete_opt))#Removes the option from dictionary
        print_movie(new_movie_collect)
    elif result == -1:#If not dictionary returns Error messages
        print(f"WARNING: '{delete_opt}' is an invalid option!")
    elif result == None:
        print(f"WARNING: '{delete_opt}' is not found!")
def is_valid_year(date_list): 
    """
    The function takes as a parameter a list of strings in the [MM, DD, YYYY] 
    format and returns True if the provided year is a possible year: a positive integer.
    For the purposes of this lab, ensure that the year is also greater than 1000.
    """
    if type(date_list[2]) == str:#Whether its a string
        if date_list[2].isdigit() == True and int(date_list[2]) >= 1000:#Whether its a valid integer and greater than 1000
            return True
        else:
            return False
    else:
        return False

def is_valid_month(date_list):
    """
    The function takes as a parameter a list of strings in the [MM, DD, YYYY] 
    format and returns True if the provided month number is a possible month
    in the U.S. (i.e., an integer between 1 and 12 inclusive).
    """
    if type(date_list[0]) == str: #Whether its a string
        if date_list[0].isdigit() == True: #Whether its a valid integer
            if 1 <= int(date_list[0]) <= 12: #Whether the month is in range 1 and 12
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def is_valid_day(date_list):
    """
    The function takes as a parameter a list of strings in the [MM, DD, YYYY]
    format and returns True if the provided day is a possible day for the given month.
    You can use the provided dictionary. Note that you should call is_valid_month()
    within this function to help you validate the month.
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if type(date_list[1]) == str: #Checks its a string
        if is_valid_month(date_list) == True: #Checks the month is valid
            if date_list[1].isdigit() == True:#Whether its a valid digit
                if int(date_list[0]) in num_days: #Wbhteher month in dictionary
                    if int(date_list[1]) in range(num_days[int(date_list[0])] + 1): #Whether its in the day range
                        if int(date_list[1]) > 0:
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False
        
    
def days_in_feb(str_year):
    """
    param: user year (str) - stores an string of length 4 that represents the year

    if the string ends in 00 then it had 29 days if divisible by 400 and 28 if it
    isnit

    if the string doesnt end in 00 then feb has 29 days id divisble by 4
    and 28 if it isnt
    """
    user_year = int(str_year)
    #If year ends in 00:
    if user_year % 100 == 00:
        #If value is divisible by 400 then there are 29 days
        if user_year % 400 == 0:
            return 29
        else: 
            return 28
    #If year doesn't end in 00:
    elif user_year % 4 == 0:
        #If value is divisible by 4 then there are 29 days
        return 29
    else:
        return 28
def is_valid_date(date_str):
    """
    param: date_str (str) - stores either an empty string
            or a date in the `YYYY/MM/DD` format

    If the string is not empty, checks each date component
    using the helper functions.
    Since the helper functions expect the date to be in a
    `MM/DD/YYYY` format, the function rearranges the date
    components accordingly before generating a list to use
    as an argument for the helper functions.

    Helper functions:
    - is_valid_year - only checks the year (a str, only digits,
        contains 1000 or above)
    - is_valid_month - only checks the month (accepts both
        formats: when the month has a leading 0, e.g. "02"
        as well when it does not, e.g., just "2")
    - is_valid_day - checks that the month is valid before
        checking that day is also correct (for simplicity,
        does NOT call days_in_feb()); accepts both
        formats: when the day has a leading 0, e.g. "07"
        as well when it does not, e.g., just "7"
    - days_in_feb - is called in is_valid_date() if the
        provided month is Feb to check if the given day
        is correct

    returns: True, if date_str is empty;
    returns False if the date_str does not have the 3 required
        date components (i.e., 2 slashes and non-empty strings
        between them);
    otherwise, returns a Boolean value based on the result
    of the helper functions.
    """
    #Check if string is empty or not
    if date_str == '':
        return True
    else:
        date_list = date_str.split('/')
        #Split date to input into functions
        if date_str.count('/') != 2 or date_list[0] == '' or date_list[1] == '' or date_list[2] == '':
            return False
        else:
            re_date = [0, 1, 2]
            re_date[0], re_date[1], re_date[2] = date_list[1], date_list[2], date_list[0]
            #Validation for year
            if is_valid_year(re_date) == False:
                return False
            #Validation for February
            elif re_date[0] == '02' or re_date[0] == '2':
                if int(re_date[1]) in range(1, int(days_in_feb(re_date[2]))+1):
                    return True
                else:
                    return False
            #Validation for day
            elif is_valid_day(re_date) == False:
                return False
            #Validation for month
            elif is_valid_month(re_date) == False:
                return False
            else:
                return True
def is_valid_genre(genre_str, movie_genres):
    """
    param: genre_str (str) - a string that's expected to be
            found in the movie_genres.
    param: movie_genres (tuple) - holds the valid movie genres.

    The function strips the leading/trailing whitespace to check
    if the genre_str is listed in the movie_genres.

    returns:
    False, if the string is not found.
    Otherwise, returns True.
    """
    #Stripping the string to check if its in genres
    if genre_str.strip() in movie_genres:
        return True
    else:
        return False
def check_valid_field(field, value, movie_genres):
    """
    param: field (str) - the name of a movie field to validate
    param: value (str) - the proposed value for the field
    param: movie_genres (tuple) - holds the valid movie genres;
            used for the "genre" field

    if the field is one of the expected keys, checks if the
    provided value is valid.
    Expected fields stored in the function are
    ("title", "genre", "date_seen", "rating").

    The function checks that the field is one of the
    expected keys and that the provided value is the correct value
    for the provided field:
    * `"title"`: a non-empty string with the movie's name.
        The title should be 2 or more characters.
    * `"genre"`: checked using is_valid_genre()
    * `"date_seen"`: a string storing the date in the `YYYY/MM/DD` format.
        The string can be empty if the movie is on the wishlist.
        Checked using is_valid_date()
    * `"rating"`: a string which can be empty or contain a number
        between 1-5.

    Helper functions:
    - is_valid_date
    - is_valid_genre

    returns:
    the name of the field, if the field name is not found or
    if the value for a given field is invalid;
    otherwise, returns "valid"
    """
    expected_f = ("title", "genre", "date_seen", "rating")
    #Check whether the category is in the tuple
    if field in expected_f:
        #Validation for catergory "title"
        if field == "title":
            if len(value) >= 2:
                return "valid"
            else:
                return field
        if field == "genre":
            #Validation for category "genre"
            if is_valid_genre(value, movie_genres) == True:
                return "valid"
            else:
                return field
        if field == "date_seen":
            #Validation for category "date_seen"
            if is_valid_date(value) == True or value == '':
                return "valid"
            else:
                return field
        if field == "rating":
            #Validation for category "rating"
            if value == '' or int(value) in range(1, 6):
                return "valid"
            else:
                return field
    else:
        return field
def add_helper(movie_collection, movie_genres):
    """
    param: movie_collection (dict) - holds the movie database;
            maps an integer ID to each movie object (also a
            dictionary)
    param: movie_genres (tuple) - holds the valid movie genres
            that the user can select

    Collects the necessary information from the user and
    attempts to create a new movie entry. If the provided
    information was valid, generates an ID (using the generate_ID())
    and adds the new entry/movie to the collection.
    Prints the added movie via the print_movie().
    Otherwise, prints a warning:
    "WARNING: trying to set '{...}' to an invalid option '{...}'!"

    Helper functions:
    - get_new_movie
    - print_movie
    - generate_ID

    The function does not return anything.
    """
    added_movie = {}
    movie_fields = {
        "title": "* Enter at least 2 letters for the movie title:",
        "genre": f"* Enter only one category shown below (exactly as shown):\n* {movie_genres}",
        "date_seen": f"* Enter the date when the movie was seen;\n"
                     f"* Use the YYYY/MM/DD format; Leave empty if on the wishlist:",
        "rating": f"* Enter an integer rating of the movie [1-5]; "
                    f"Leave empty if on the wishlist or not yet rated:"
    }
    print("::: Enter the movie information:")
    #Iterate through the list
    for key in movie_fields:
        print(movie_fields[key])
        #Get user input
        value = input("> ")
        #Append the input to the dictionary
        added_movie[key] = value
    result = get_new_movie(added_movie, movie_genres)
    #Check whether the function returns back a dictionary
    if type(result) == dict:
        print("Success! Adding a new movie:")
        newMID = generate_ID(movie_collection)
        #If so, add it to the move database
        movie_collection[newMID] = result
        #print out the new song
        print_movie(added_movie, False)
    else:
        print(f"WARNING: trying to set '{result}' to an invalid option '{added_movie[result]}'!")
def get_new_movie(values_dict, movie_genres = ("", "Action", "Comedy", "Drama")):
    """
    param: values_dict (dict) - a dictionary that holds
            STRING values for all keys
    param: movie_genres (tuple) - holds the valid movie genres;
            by default is set to ("", "Action", "Comedy", "Drama");
            used for the "genre" field.

    Helper functions:
    - check_valid_field 

    For each key and value in the provided dictionary, calls
    the check_valid_field() to verify that they are valid.
    Note that the function does not check if an expected key is missing
    from the values_dict, so it does not have to have all the expected
    keys in it.

    returns: a NEW dictionary that stores the values from the values_dict
        after each value was verified by the check_valid_field().
    Otherwise, returns the name of the invalid key or the key that
    stores the invalid data.
    """
    dict_movie = {}
    #Iterate through the dictionary
    for key, value in values_dict.items():
        #Check if the keys and values are valid
        if check_valid_field(key, value, movie_genres) == "valid":
            #Append to dictionary if valid
            dict_movie[key] = value
        else:
            return key
    return dict_movie
def update_helper(movie_collection, movie_genres):
    """
    param: movie_collection (dict) - holds the movie database;
            maps an integer ID to each movie object (also a
            dictionary)
    param: movie_genres (tuple) - holds the valid movie genres;
            used for the "genre" field

    Helper functions:
    - print_movies_dict
    - print_movie
    - print_options
    - get_movie
    - update_movie

    The function does not return anything.    
    """
    if movie_collection == {}:
        print("WARNING: there is nothing to update.")
    else:
        print("Which movie would you like to update?")
        print_movies_dict(movie_collection, title_only = True, show_ID = True)
        print("::: Enter the number corresponding to the movie ID:")
        movID = input("> ") # get the user input

        upCollection = get_movie(movie_collection, movID)
        if type(upCollection) == dict:
            print("Success! Found:")
            print_movie(upCollection)
            print("Which field would you like to update?")
            print_options(upCollection) # display the selected movie object: its keys and values
            print("::: Enter the field name:")
            fieldInput = input("> ") # get the key as an input
            if fieldInput not in upCollection:
                print(f"WARNING: '{fieldInput}' is an invalid option!")
            else:
                print(f"::: Enter the {fieldInput} information instead of '{upCollection[fieldInput]}':")
                if fieldInput == "genre":
                    print(f"::: Valid categories are:\n{movie_genres}")
                userCateg = input("> ") # get the data

                updateMov = update_movie(upCollection, fieldInput, userCateg, movie_genres) # send the specific movie to update
                if type(updateMov) == dict:
                    print("Success!")
                    print_movie(updateMov)
        ##          #print(movie_collection) ### DEBUGGING
                else:
                    print(f"WARNING: trying to set '{fieldInput}' to an invalid option '{userCateg}'!")

        elif upCollection == 0:
            print("WARNING: there is nothing to update.")
            return
        elif upCollection == -1:
            print(f"WARNING: '{movID}' is an invalid option!")
        else:
            print(f"WARNING: '{movID}' is not found!")

def get_movie(movie_collection, keyStr):
    """
    param: movie_collection (dict) - holds the movie database;
            maps an integer ID to each movie object (also a
            dictionary)
    param: keyStr(str) - a string that is supposed to represent
            an integer ID that corresponds to a key in the
            collection

    returns:
    0 - if the collection is empty.
    -1 - if the second parameter is not a string or the string
    does not hold a valid integer

    Otherwise, converts the provided string to an integer and
    returns None if the ID does not map into a key in the collection
    or returns the existing item (dict) that was requested.
    """
    #Check if dictionary is empty
    if movie_collection == {}:
        return 0
    #Check if the input is a string or if the contents of the string is an integer
    elif type(keyStr) != str or keyStr.isdigit() == False:
        return -1
    else:
        #Convert the string into integer
        key_int = int(keyStr)
        #Check whether the key is in the dictionary
        if key_int not in movie_collection:
            return None
        else:
            return movie_collection[key_int]
def update_movie(movie_dict, key, value, movie_genres):
    """
    param: movie_dict (dict) - a valid movie dictionary
    param: key (str) - a valid key in the dictionary
    param: value - a valid value, depending on the key
    param: movie_genres (tuple) - holds the valid movie genres;
            used for the "genre" field

    Helper function:
    - check_valid_field - verifies the validity of the key
    and the value

    returns: the key if either the key or value is invalid;
    otherwise, returns an updated dictionary.
    """
    #First hecks to see whether keys and values are valid or not
    if check_valid_field(key, value, movie_genres) != "valid":
        #If not immediately returns key
        return key
    else:
        movie_dict[key] = value
        return movie_dict
            
        
def generate_ID(collection, offset=1):
    """
    param: collection (dict) - a collection of items that works with max()
    param: offset (int) - an integer offset that's added to the first ID.

    If the collection is empty, then the first ID is the offset value.
    Otherwise, the function retrieves the max value from the collection,
    and returns its value+1.

    returns:
    The computed ID, based on the offset or the max element in the collection.
    If max value is not an integer, the function returns an error string:
    "Error, non-integer IDs"

    For example, calling the function with
    {} and 0 as the offset should return 0, since the collection is empty
    and 0 is the offset;
    {} and 1000 as the offset should return 1000.
    {500: (16.5, None)} and 1000 as the offset should return 501, since the
    collection is not empty and 500 (the dict key) is the max value.
    """
    #Check if dictionary is empty
    if collection == {}:
        return offset
    else:
        for key in collection.keys():
            #Check if they key is an int
            if type(key) != int:
                #If not pribnt error
                return "Error, non-integer IDs"
            else:
                #If it is sort the list using the max() function
                max_el = max(list(collection.keys()))
                return max_el + 1

