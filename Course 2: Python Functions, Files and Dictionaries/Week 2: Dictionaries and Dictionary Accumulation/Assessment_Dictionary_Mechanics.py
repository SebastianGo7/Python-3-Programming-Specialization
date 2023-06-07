
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 2: Chapter Dictionaries and Dictionary Accumulation
# Assessment: Dictionary Mechanics

# 1
# A dictionary including country names as keys and the number of
# medals the countries had so far as the key's values is created
# according to a description of medals of certain past Olympic Games.

medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45,
               'Russia': 30, 'Germany': 17}

# 2
# A key-value pair is added to a given dictionary according to given
# information.

swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5,
            'Dirado': 4}

swimmers['Phelps'] = 23
print(swimmers)

# 3
# A key-value pair is added to a given dictionary according to given
# information.

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4,
                  'cricket': 2}
sports_periods['hockey'] = 3

# 4
# A given dictionary is updated with given new information.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27,
         "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds['Spain'] = golds['Spain'] + 2

# 5
# A list of the keys of a given dictionary is created.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27,
         "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())

# 6
# Specific desired data from a given dictionary is fetched and
# assigned to a variable.

medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45,
               'Russia': 30, 'Germany': 17, 'Italy': 22, 'France': 22,
               'Japan': 26, 'Australia': 22, 'South Korea': 14,
               'Hungary': 12, 'Netherlands': 10, 'Spain': 5,
               'New Zealand': 8, 'Canada': 13, 'Kazakhstan': 8,
               'Colombia': 4, 'Switzerland': 5, 'Belgium': 4,
               'Thailand': 4, 'Croatia': 3, 'Iran': 3, 'Jamaica': 3,
               'South Africa': 7, 'Sweden': 6, 'Denmark': 7,
               'North Korea': 6, 'Kenya': 4, 'Brazil': 7, 'Belarus': 4,
               'Cuba': 5, 'Poland': 4, 'Romania': 4, 'Slovenia': 3,
               'Argentina': 2, 'Bahrain': 2, 'Slovakia': 2,
               'Vietnam': 2, 'Czech Republic': 6, 'Uzbekistan': 5}

belarus = medal_count['Belarus']

# 7
# Specific desired data from a given dictionary is fetched and
# assigned to a variable.

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10,
              "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece":
                   111, "Mongolia": 24, "Brazil": 108, "Croatia":
                   34, "Algeria": 15, "Switzerland": 323,
               "Yugoslavia": 87, "China": 526, "Egypt": 26,
               "Norway": 477, "Spain": 133, "Australia": 480,
               "Slovakia": 29, "Canada": 22, "New Zealand": 100,
               "Denmark": 180, "Chile": 13, "Argentina": 70,
               "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England":
                   806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}

chile_golds = total_golds['Chile']

# 8
# Specific desired data from a given dictionary is fetched and
# assigned to a variable.

US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6,
             "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3,
             "Cycling - Road": 1, "Fencing": 4, "Diving": 2,
             "Archery": 2, "Cycling - Track": 1, "Equestrian": 2,
             "Golf": 1, "Weightlifting": 1}

fencing_value = US_medals['Fencing']

