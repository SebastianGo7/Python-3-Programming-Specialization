
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
