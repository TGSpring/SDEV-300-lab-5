"""
Tyler Spring
lab 5
SDEV 300
This is lab 5. The purpose of this program is prompt the user to
select from a list of options which csv file they
wish to work with. After that it prompts the user again to select
a column of said csv file.
Once that is selected it returns values for the column such as count,
 mean, standard deviation, min, max, and displays a Histogram in the file
 of which it is being run.
 """

import sys

import pandas as pand
import matplotlib.pyplot as hist

print("***************** Welcome to the Python Data Analysis App**********")


def popdata(ans):
    """
The pop data function. Is called in the main menu of this program.
Takes the selected input from the main menu, reads in the PopChange csv,
and prompts the user to select a column of the file or exit the column.
The validation for this is done with a simple while true loop, and I now refuse to do any
other type of validation iteration given how easy this is.
    :rtype: object
    """
    # File is read in and assigned to pop_doc
    # The next menu and validation are implemented showing the columns, output,
    # and/or option to exit.
    pop_doc = pand.read_csv("PopChange.csv")
    while True:
        pop_ans = input("\n"
                        "You have entered Population Data.\n"
                        "Select the Column you want to analyze: \n"
                        "a. Pop Apr 1\n"
                        "b. Pop Jul 1\n"
                        "c. Change Pop\n"
                        "d. Exit Column")
        if pop_ans == 'a':
            print(pop_ans, "\n"
                           "You selected Pop Apr 1\n"
                           "The statistics for this column are:")
            column = pop_doc['Pop Apr 1']
            break
        elif pop_ans == 'b':
            print(pop_ans, "\n"
                           "You selected Pop Jul 1\n"
                           "The statistics for this column are:")
            column = pop_doc['Pop Jul 1']
            break
        elif pop_ans == 'c':
            print(pop_ans, "\n"
                           "You selected Change Pop")
            column = pop_doc['Change Pop']
            break
        elif pop_ans == 'd':
            print(pop_ans, "\n"
                           "You selected to exit this column")
            driver()
        else:
            print("Invalid reEnter")
        # Prints output of returned values for the columns from the column array made.

    print("Count = ", {column.count()}, "\n",
          "Mean = ", {column.mean()}, "\n",
          "Standard Deviation = ", {column.std()}, "\n",
          "Min = ", {column.min()}, "\n",
          "Max =  ", {column.max()})
    # Where histogram is created and created in the file that all the documents are located.
    # CHECK THE FOLDER FOR THIS OUTPUT.
    print("The Histogram of this column is now displayed")
    hist.hist(column, 20, density=True, facecolor='b', alpha=0.75)
    hist.grid(True)
    fig = hist
    fig.savefig(f'popchange-{ans}.png')


def house(ans):
    """
The house function. Is called in the main menu of this program.
Takes the selected input from the main menu, reads in the Housing csv,
and prompts the user to select a column of the file or exit the column.
    :rtype: object
    """
    # File is read in and assigned to house_doc
    # The next menu and validation are implemented showing the columns, output,
    # and/or option to exit.
    house_doc = pand.read_csv("Housing.csv")
    while True:
        house_ans = input("\n"
                          "You have entered Housing Data.\n"
                          "Select the Column you want to analyze: \n"
                          "a. age\n"
                          "b. bedRms\n"
                          "c. built\n"
                          "d. rooms\n"
                          "e. utility\n"
                          "f. exit column")
        if house_ans == 'a':
            print(house_ans, "\n"
                             "You selected age\n"
                             "The statistics for this column are:")
            column = house_doc['AGE']
            break
        elif house_ans == 'b':
            print(house_ans, "\n"
                             "You selected bedRms\n"
                             "The statistics for this column are:")
            column = house_doc['BEDRMS']
            break
        elif house_ans == 'c':
            print(house_ans, "\n"
                             "You selected built")
            column = house_doc['BUILT']
            break
        elif house_ans == 'd':
            print(house_ans, "\n"
                             "You selected rooms")
            column = house_doc['ROOMS']
            break
        elif house_ans == 'e':
            print(house_ans, "\n"
                             "You selected utility")
            column = house_doc['UTILITY']
            break
        elif house_ans == 'f':
            print(house_ans, "\n"
                             "You selected to exit this column")
            driver()
        else:
            print("Invalid ReEnter")
        # Prints output of returned values for the columns from the column array made.
    print("Count = ", {column.count()}, "\n",
          "Mean = ", {column.mean()}, "\n",
          "Standard Deviation = ", {column.std()}, "\n",
          "Min = ", {column.min()}, "\n",
          "Max =  ", {column.max()})
    # Where histogram is created and created in the file that all the documents are located.
    # CHECK THE FOLDER FOR THIS OUTPUT.
    print("The Histogram of this column is now displayed")
    hist.hist(column, 20, density=True, facecolor='b', alpha=0.75)
    hist.grid(True)
    fig1 = hist
    fig1.savefig(f'housing data-{ans}.png')


def driver():
    while True:
        """This is the main menu/driver for the program.
        Here is where the user is first prompted to select one of the two
        csv files or exit the program. The validation is done by a while loop and this
        will also be where the user returns to if they decide to exit one of the selected csv documents
        they have previously selected."""

        ans = input("Select the file you want to analyze: \n"
                    "1. Population Data \n"
                    "2. Housing Data \n"
                    "3. Exit the Program")
        if ans == '1':
            popdata(ans)
        elif ans == '2':
            house(ans)
        elif ans == '3':
            print(ans, "\n", "*************** Thanks for using the Data Analysis App********** ")
            sys.exit()
        else:
            print("Invalid reEnter.")


driver()
