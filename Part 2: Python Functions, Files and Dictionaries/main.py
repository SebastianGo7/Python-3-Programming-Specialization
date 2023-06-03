
# Part 3 Data Collection and Processing with Python


def week_1_assignment():

    # 1
    # The variable nested contains a nested list. Assign ‘snake’ to the
    #  variable output using indexing.

    nested = [['dog', 'cat', 'horse'],
              ['frog', 'turtle', 'snake', 'gecko'],
              ['hamster', 'gerbil', 'rat', 'ferret']]
    output = nested[1][2]

    # 2
    # Below, a list of lists is provided. Use in and not in tests to
    # create variables with Boolean values. See comments for further
    # instructions.

    lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10],
           ['green', 'yellow', 'purple', 'red']]

    # Test to see if 'yellow' is in the third list of lst. Save to
    # variable ``yellow``
    for item in lst[2]:
        if "yellow" in item:
            yellow = True

    # Test to see if 4 is in the second list of lst. Save to variable
    # ``four``
    for number in lst[1]:
        if number == 4:
            four = True
        else:
            four = False

    # Test to see if 'orange' is in the first element of lst. Save to
    # variable ``orange``
    for colour in lst[0]:
        if 'orange' in colour:
            orange = True

    # 3
    # Below, we’ve provided a list of lists. Use in statements to create
    # variables with Boolean values - see the ActiveCode window for
    # further directions.

    L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99],
         ['small', 'large']]

    # Test if 'hola' is in the list L. Save to variable name test1
    for item in L:
        if item == "hola":
            test1 = True
        else:
            test1 = False

    # Test if [5, 8, 7] is in the list L. Save to variable name test2
    for item in L:
        if item == [5, 8, 7]:
            test2 = True
            break
        else:
            test2 = False

    # Test if 6.6 is in the third element of list L. Save to variable
    # name test3
    for item in L:
        for subitem in item:
            if type(subitem) == float:
                if float(subitem) == 6.6:

                    test3 = True
                    break
                else:
                    test3 = False

   
