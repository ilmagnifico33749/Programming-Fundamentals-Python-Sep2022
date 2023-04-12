
def movie_organizer(*args):
    movie_collection = dict()
    all_movies_list = args
    for movie_details in all_movies_list:
        movie_name = movie_details[0]
        movie_genre = movie_details[1]
        if movie_genre not in movie_collection.keys():
            movie_collection[movie_genre] = [movie_name]

        else:
            movie_collection[movie_genre].append(movie_name)

    movie_collection_sorted = sorted(movie_collection.items(), key=lambda x: (-len(x[1]), x[0]), reverse=False)
    repr_movie_collection = ""
    for genre_name, movies_list in movie_collection_sorted:
        repr_movie_collection += f"{genre_name} - {len(movies_list)}\n* "
        repr_movie_collection += '\n* '.join(sorted(movies_list)) + '\n'
    return repr_movie_collection


# ###################################################
# Test_Code_1:
# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))
# ---------------------------------------------------
# Output_1:
# Sci-fi - 1
# * The Matrix
# ###################################################
# Test_Code_2:
# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))
# ---------------------------------------------------
# Output_2:
# Drama - 3
# * The Godfather
# * The Pursuit of Happiness
# * The Shawshank Redemption
# Comedy - 2
# * The Hangover
# * The Hangover Part II
# ###################################################
# Test_Code_3:
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
# ---------------------------------------------------
# Output_3:
# Action - 4
# * Avatar: The Way of Water
# * The Dark Knight
# * The Warrior
# * Top Gun
# Comedy - 4
# * 21 Jump Street
# * Duck Soup
# * Like A Boss
# * Ted
# Drama - 2
# * House Of Gucci
# * The Green Mile
# Musicals - 1
# * A Star Is Born
# ###################################################
