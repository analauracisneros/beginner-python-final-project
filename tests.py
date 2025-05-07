from functions import *
from extra_credit import *
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
print("Testing print_movies_dict(movieDatabase, title_only = True, show_ID = True)")
print_movies_dict(movieDatabase, title_only = True, show_ID = True)

print("^"*55)
print("\nTesting print_movies_dict(movieDatabase, title_only = True, show_ID = False)")
print_movies_dict(movieDatabase, title_only = True, show_ID = False)

print("^"*55)
print("\nTesting print_movies_dict(movieDatabase, title_only = True)")
print_movies_dict(movieDatabase, title_only = True)

assert delete_movie(movieDatabase, 1) == -1

assert delete_movie({}, 1) == 0

assert delete_movie(movieDatabase, '1') == {'title': 'Eternal Sunshine of the Spotless Mind', 'genre': 'Sci-Fi', 'date_seen': '', 'rating': ''}
#Zybooks said to create assert statements based on specified situations, I'm not too sure what those are (I did ask on Piazza) so I made my own assert statements
assert is_valid_date('1408/03/03') == True
assert is_valid_date('2133/08/15') == True
assert is_valid_date('1270/04/07') == True
assert is_valid_date('2023/05') == False
assert is_valid_date('2023/05/06/07') == False
assert is_valid_date('') == True
assert is_valid_date('2023/02/29') == False
assert is_valid_day(['04', '10', '2406']) == True
assert is_valid_day(['01', '26', '1122']) == True
assert is_valid_day(['08', '03', '2262']) == True
assert is_valid_day(['12', '56', '2488']) == False
assert is_valid_day(['04', '48', '1051']) == False
assert is_valid_day(['09', '46', '1093']) == False
assert days_in_feb('2000') == 29
assert days_in_feb('1999') == 28
assert days_in_feb('1700') == 28
assert days_in_feb('1994') == 29
assert is_valid_month(['05', '14', '1508']) == True
assert is_valid_month(['01', '24', '1032']) == True
assert is_valid_month(['08', '04', '1742']) == True
assert is_valid_month(['08', '04', '1742']) == False
assert is_valid_month(['08', '04', '1742']) == False
assert is_valid_month([25, '14', '1326']) == False
assert is_valid_month(['25', '14', '1326']) == False
assert is_valid_year(['24', '16', 'ssss']) == False
assert is_valid_genre('Sport', ('Sport', 'SciFi', 'Foreign', 'Fantasy')) == True
assert is_valid_genre('Foreign', ('Sport', 'SciFi', 'Foreign', 'Fantasy')) == True
assert is_valid_genre('  Comedy   ', ('Comedy', 'Action', 'Drama')) == True
assert is_valid_genre('Action', ('Sport', 'SciFi', 'Foreign', 'Fantasy')) == False
assert is_valid_year(['24', '15', 2000]) == False
assert is_valid_year(['24', '15', '2000']) == True
assert is_valid_genre('   Comedy    ', ("Comedy", "Action")) == True
assert is_valid_genre('Drama', ("Comedy", "Action")) == False
assert is_valid_genre('Drama', ('Sport', 'SciFi', 'Foreign', 'Fantasy')) == False
assert is_valid_genre('', ('Sport', 'SciFi', 'Foreign', 'Fantasy')) == False
assert check_valid_field('title', 'ABC', ('Comedy', 'Action', 'Drama')) == "valid"
assert check_valid_field('genre', '', ('', 'Comedy', 'Action', 'Drama')) == "valid
assert check_valid_field('genre', 'Sport', ('Sport', 'Comedy', 'Action', 'Drama')) == "valid"
assert check_valid_field('date_seen', '2025/01/01', ('Comedy', 'Action', 'Drama')) == "valid"
assert check_valid_field('title', 'K', ('Comedy', 'Action', 'Drama')) == "title"
assert check_valid_field('genre', 'romcom', ('Comedy', 'Action', 'Drama')) == "genre"
assert check_valid_field('date_seen', '2025/15/15', ('Comedy', 'Action', 'Drama')) == "date_seen"
assert check_valid_field('date', '0000/00/00', ('Comedy', 'Action', 'Drama')) == "date"
assert get_new_movie({'title': 'Barbie', 'genre': '', 'date_seen': '', 'rating': ''}) == {'title': 'Barbie', 'genre': '', 'date_seen': '', 'rating': ''}
assert get_new_movie({'title': 'This is the title of my movie'}) == {'title': 'This is the title of my movie'}
assert get_new_movie({'title': 'Amelie', 'genre': 'Foreign', 'date_seen': '', 'rating': ''}, ('Sport', 'SciFi', 'Foreign', 'Fantasy')) == {'title': 'Amelie', 'genre': 'Foreign', 'date_seen': '', 'rating': ''}
assert generate_ID({1: 'movie1'}) == 2
assert generate_ID({123: 'movie2'}) == 124
assert generate_ID({'10': 'my movie'}) == "Error, non-integer IDs"
assert generate_ID({}) == 1
assert get_movie({10: {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}, 12: {'title': 'Inception', 'genre': 'Adventure', 'date_seen': '', 'rating': ''}, 13: {'title': 'Forrest Gump', 'genre': 'Drama', 'date_seen': '2020/05/25', 'rating': '5'}, 14: {'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 25: {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}}, '25') == {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}
assert get_movie({10: {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}, 12: {'title': 'Inception', 'genre': 'Adventure', 'date_seen': '', 'rating': ''}, 13: {'title': 'Forrest Gump', 'genre': 'Drama', 'date_seen': '2020/05/25', 'rating': '5'}, 14: {'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 25: {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}}, '10') == {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}
assert get_movie({10: {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}, 12: {'title': 'Inception', 'genre': 'Adventure', 'date_seen': '', 'rating': ''}, 13: {'title': 'Forrest Gump', 'genre': 'Drama', 'date_seen': '2020/05/25', 'rating': '5'}, 14: {'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 25: {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}}, '13') == {'title': 'Forrest Gump', 'genre': 'Drama', 'date_seen': '2020/05/25', 'rating': '5'} 
assert get_movie({10: {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}, 12: {'title': 'Inception', 'genre': 'Adventure', 'date_seen': '', 'rating': ''}, 13: {'title': 'Forrest Gump', 'genre': 'Drama', 'date_seen': '2020/05/25', 'rating': '5'}, 14: {'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 25: {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}}, '-1') == -1
assert get_movie({}, '0') == 0
assert get_movie({10: {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}, 12: {'title': 'Inception', 'genre': 'Adventure', 'date_seen': '', 'rating': ''}, 13: {'title': 'Forrest Gump', 'genre': 'Drama', 'date_seen': '2020/05/25', 'rating': '5'}, 14: {'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 25: {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}}, 10) == -1
assert update_movie({'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': '5'}, 'rating', '', ('',)) == {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'date_seen': '', 'rating': ''}
assert update_movie({'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}, 'date_seen', '', ('',)) == {'title': 'Interstellar', 'genre': '', 'date_seen': '', 'rating': ''}
assert update_movie({'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 'genre', '', ('',)) == {'title': 'The Lord of the Rings: The Return of the King', 'genre': '', 'date_seen': '2020/04/01', 'rating': '3'}
assert update_movie({'title': 'The Lord of the Rings: The Return of the King', 'genre': 'Sci-Fi', 'date_seen': '2020/04/01', 'rating': '3'}, 'fandom', '', ('',)) == "fandom"


                     
