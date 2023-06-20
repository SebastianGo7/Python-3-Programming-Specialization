
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 3: Data Collection and Processing with Python
# Week 3: Internet APIs
# Final Course Project: OMDB and TasteDive Mashup

# 1
# The following project allows to learn how to mash up data from two
# different APIs to make movie recommendations.
# The TasteDive API returns related items for a move (or band,
# TV show, etc. as a query input.
# The OMDB API returns data including scores from various review
# sites (Rotten Tomatoes, IMBD, etc.) for a movie titles query input.
# These information is put combined. TasteDive will be used to get
# related movies for a whole list of movies. The resulting list of
# related movies is sorted according to their Rotten Tomatoes scores
# through making API calls to the OMDB API.
#
# Results for queries needed from OMDB and TasteDive are provided in
# a cached file. This can be accessed by using
# request_with_caching.get() rather than requests.get().
#
# First data is fetched from TasteDive and its API documentation is
# at https://tastedive.com/read/api.
#
# A function get_movie_from_tastedive is defined which takes a
# string that is the name of a movie or movie artist as input
# parameter. Five TasteDive results which are associated with that
# string are returned. Only movie returns are wanted, not other
# kinds of media.
#
#  Define a function, called get_movies_from_tastedive. It should
#  take one input parameter, a string that is the name
#  of a movie or music artist. The function should return the 5
#  TasteDive results that are associated with that string;
#  be sure to only get movies, not other kinds of media.
#
# The following queries are included in the cache, and only these
# limited parameters should be given in the API call (to make sure
# data is actually in the cache and no API key is necessary):

#       q               type          limit
# Black Panther         <omitted>    <omitted>
# Black Panther         <omitted>       5
# Black Panther         movies       <omitted>
# Black Panther         movies          5
# Tony Bennett          <omitted>       5
# Tony Bennett          movies          5
# Captain Marvel        movies          5
# Bridesmaids           movies          5
# Sherlock Holmes       movies          5

import requests_with_caching
import json

def get_movies_from_tastedive(str_input):
    # A TasteDive query is set and related movie results are returned.
    page = requests_with_caching.get(
        "https://tastedive.com/api/similar",
        params={"q": str_input, "type": "movies", "limit": 5})
    py_rec = json.loads(page.text)

    return py_rec

get_movies_from_tastedive("Black Panther")
# get_movies_from_tastedive("Bridesmaids"

# 2
# The completed function is copied into the following code window.
# Then a function called extract_movie_titles is written that extracts
# just the list movie titles from a dictionary which is returned by
# get_movies_from_tastedive.

import requests_with_caching
import json

def get_movies_from_tastedive(str_input):
    # A TasteDive query is set and related movie results are returned.
    page = requests_with_caching.get(
        "https://tastedive.com/api/similar",
        params={"q": str_input, "type": "movies", "limit": 5})
    py_rec = json.loads(page.text)
    return py_rec

def extract_movie_titles(dict_input):
    # Up to five TasteDive query results are stored in a list.
    names_lst = []
    for nam in dict_input["Similar"]["Results"]:
    # dictionary has one key ["Similar"] which stores all values.
        names_lst.append(nam["Name"])
    print(names_lst[:5])
    return names_lst[:5]

# 3
# The completed functions from the previous code windows are copied
# into this active code window.
# A function is written called get_related_titles which takes a list
# of movie titles as input.
# It gets five related movies for each from TasteDive, extracts
# the titles for all of them, and combines them all into a single
# list without including the same movie twice.

import requests_with_caching
import json

def get_movies_from_tastedive(str_input):
    # A TasteDive query is set and related movie results are returned.
    page = requests_with_caching.get(
        "https://tastedive.com/api/similar",
        params={"q": str_input, "type": "movies", "limit": 5})
    py_rec = json.loads(page.text)
    return py_rec

def extract_movie_titles(dict_input):
    # Up to five TasteDive query results are stored in a list.
    names_lst = []
    for nam in dict_input["Similar"]["Results"]:
        names_lst.append(nam["Name"])
    print(names_lst[:5])
    return names_lst[:5]

def get_related_titles(lst_movies):
    # Related titles from a list of movies are combined into a
    # single list without including the same movie twice.
    ret_lst = []
    extracted_lst = []
    for item in lst_movies:
        extracted_lst = extract_movie_titles(
            get_movies_from_tastedive(item))
        for movie in extracted_lst:
            if movie not in ret_lst:
                ret_lst.append(movie)
    return ret_lst

# get_related_titles(["Black Panther", "Captain Marvel"])
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

# 4
# Data is fetched from OMDB; the API's documentation is at
# https://www.omdbapi.com/
# Therefore a function called get_movie_data is defined which takes
# in one parameter which is a string that should represent the
# title of a movie to be searched. The function returns a
# dictionary with information about that movie.
#
# The function requests_with_catching.get() is used. In that way
# queries on movies that are already in the cache can be done
# without an api key. The keys t and r are used to fetch data.

import requests_with_caching
import json

def get_movie_data(str_input):
    # A dictionary with rating information about as movie is fetched
    # from the OMDB API.
    page = requests_with_caching.get("http://www.omdbapi.com/",
    params={"t":str_input, "r":"json"})
    py_rec = json.loads(page.text)
    return py_rec

get_movie_data("Baby Mama")
# get_movie_data("Venom")

# 5
# The completed function from above is copied into the following
# code window. A function called get_movie_rating, which takes an
# OMDB dictionary result for one movie and extracts the
# Rotten Tomatoes rating as an integer.
# For example, if given the OMDB dictionary for “Black Panther”,
# it would return 97. If there is no Rotten Tomatoes rating,
# 0 is returned.

import requests_with_caching
import json

def get_movie_data(str_input):
    # A dictionary with rating information about as movie is fetched
    # from the OMDB API.
    page = requests_with_caching.get("http://www.omdbapi.com/",
    params={"t":str_input, "r":"json"})
    py_rec = json.loads(page.text)
    return py_rec

def get_movie_rating(dict_input):
    # The Rotten Tomatoes rating is returned as an integer getting a
    # dictionary input; 0 is returned if there is no rating.
    rating = 0
    for counter in range(len(dict_input['Ratings'])):
        if dict_input['Ratings'][counter][
            "Source"] == "Rotten Tomatoes":
            return int(dict_input['Ratings'][1]["Value"][0:2])
    else:
        return 0

get_movie_rating(get_movie_data("Deadpool 2"))

# 6
# The functions are put together here. A function
# get_sorted_recommendations is defined which takes a list of movie
# titles as an input. A sorted list of up to five related
# movie titles for each input title is returned as output.
# The movies are sorted in descending order by their Rotten Tomatoes
# rating, as returned by the get_movie_rating function. The ties
# between output movies are broken in reverse alphabetic order.


import requests_with_caching
import json

def get_movies_from_tastedive(str_input):
    # A TasteDive query is set and related movie results are returned.
    page = requests_with_caching.get("https://tastedive.com/api/similar",
                                     params={"q": str_input,
                                             "type": "movies", "limit": 5})
    py_rec = json.loads(page.text)
    return py_rec

def extract_movie_titles(dict_input):
    # Up to five TasteDive query results are stored in a list.
    names_lst = []
    for nam in dict_input["Similar"]["Results"]:
        names_lst.append(nam["Name"])
    return names_lst[:5]

def get_related_titles(lst_movies):
    # Related titles from a list of movies are combined into a
    # single list without including the same movie twice.
    ret_lst = []
    extracted_lst = []
    for item in lst_movies:
        extracted_lst = extract_movie_titles(
            get_movies_from_tastedive(item))
        for movie in extracted_lst:
            if movie not in ret_lst:
                ret_lst.append(movie)
    return ret_lst


# Extract_movie_titles(get_movies_from_tastedive("Black Panther")):

def get_movie_data(str_input):
    # A dictionary with rating information about as movie is fetched
    # from the OMDB API.
    page = requests_with_caching.get("http://www.omdbapi.com/",
    params={"t":str_input, "r":"json"})
    py_rec = json.loads(page.text)
    return py_rec

def get_movie_rating(dict_input):
    # The Rotten Tomatoes rating is returned as an integer getting a
    # dictionary input; 0 is returned if there is no rating.
    rating = 0
    for counter in range(len(dict_input['Ratings'])):
        if dict_input['Ratings'][counter]["Source"] == "Rotten Tomatoes":
            return int(dict_input['Ratings'][1]["Value"][0:2])
    else:
        return 0


# get_movie_rating(get_movie_data("Deadpool 2"))
# get_movies_from_tastedive("Bridesmaids")

def get_sorted_recommendations(lst_movie_titles):
    # A list of movie titles is sorted by the movies' ratings. The
    # ties between output movies are broken in reverse alphabetical
    # order.

    lst_first_output = get_related_titles(lst_movie_titles)

    lst_title_and_rating = []
    for item in lst_first_output:
        # A list of all relevant movies is created.
        lst_title_and_rating.append(
            [item, get_movie_rating(get_movie_data(item))])

    print("--")
    print(lst_title_and_rating)

    lst_sorted_1 = []
    lst_sorted_2 = []
    # The list is sorted by the movies rating.
    lst_sorted_1 = sorted(lst_title_and_rating, key=(lambda k: -k[1]),
                          reverse=True)

    for counter in range(len(lst_sorted_1)):
        # The movie list is resorted to break the ties in reverse
        # alphabetical order.
        lst_sorted_2.append(
            lst_sorted_1[(-counter + len(lst_sorted_1) - 1)])
    print(lst_sorted_2)

    lst_only_Titles = []
    for movie in lst_sorted_2:
        # The titles of the sorted list are appended to a return list
        lst_only_Titles.append(movie[0])

    return lst_only_Titles

get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
# get_related_titles(["Black Panther", "Captain Marvel"])

