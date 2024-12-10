import api 
import cli_prints

user_selection = "" 
year_input = ""
race_population = api.RacePopulationAPI()

print("\nWelcome to the US Race Population command line! This program givs you information about the population of\n"
        "various race groups within the US. The information is pulled from the US Census Bureau in 2010 and in 2020.\n"
        "What follows are prompts for whatever information you are looking for.\n")

print("Type 'quit' at anytime to exit\n")

while (True):

      while (True):
            try:
                  user_selection = input("Enter a number for the data you want to look at:\n"
                                    "(1) Get RACE or TOTAL population (of the US or a State)\n"
                                    "(2) Compare RACE or TOTAL populations (Different or Same State/Year)\n"
                                    "(3) Filter dataset based on RACE or TOTAL population (US or a State)\n")
                  
                  if (str(user_selection).lower() == "quit"):
                        exit()
                  
                  user_selection = int(user_selection)

                  if (user_selection > 0 and user_selection < 4):
                        break
                  else:
                        print("Please enter a valid input\n")
            except ValueError:
                  print("Please enter a valid input\n")
             
      if user_selection == 1:
            while (True):
                  try:
                        user_selection_one = input("\nYou selected \"Get RACE or TOTAL population of the US or a State)\"!\nWhat would you like to look at? \n"
                                          "(1) Total population of US\n"
                                          "(2) Total population of a state\n"
                                          "(3) Population of a race in the US\n"
                                          "(4) Population of a race in a state\n")
                                          
                        if (str(user_selection_one).lower() == "quit"):
                              exit()
                        user_selection_one = int(user_selection_one)
                        
                        if (user_selection_one > 0 and user_selection_one < 5):
                              break
                        else:
                              print("Please enter a valid input\n")

                  except ValueError:
                        print("Please enter a valid input\n")

            while (True):
                  try:            
                        year = input("Would you like to look at 2010 or 2020? Type 2010 or 2020:\n")

                        if (str(year).lower() == "quit"):
                              exit()

                        year = int(year)

                        if (year == 2020 or year == 2010):
                              break
                        else:
                              print("Please enter a valid input\n")

                  except ValueError:
                        print("Please enter a valid input\n")

            if user_selection_one == 1:
                  name = race_population.column_int_to_string(0,0)
                  total_us_population = race_population.get_national_total_population(year, name)
                  print("The total population of the US is", total_us_population, "\n")

            elif user_selection_one == 2:
                  cli_prints.printAllStates()
                  while (True):
                        try:
                              state_input = input("What state would you like to look at?\n")
                              if (str(state_input).lower() == "quit"):
                                    exit()
                              state_input = int(state_input)

                              if (state_input > 0 and state_input < 53):
                                    break
                              else:
                                    print("Please enter a valid input\n")
                        
                        except ValueError:
                              print("Please enter a valid input\n")
                              
                  state_name = race_population.row_int_to_string(state_input)
                  race_name = race_population.column_int_to_string(0, 0)
                  total_state_population = race_population.get_state_total_population(year, state_name, race_name)
                  print("The total population of the", state_name,"is", total_state_population, "\n")

            elif user_selection_one == 3:
                  while(True):
                        cli_prints.printCombinationOptions()
                        try:
                              combination = input("Enter a number for the combination you are interested in:\n")

                              if (str(combination).lower() == "quit"):
                                    exit()

                              combination = int(combination)

                              if (combination > -1 and combination <4):
                                    break
                              else:
                                    print("Please enter a valid input\n")

                        except ValueError:
                              print("Please enter a valid input\n")

                  race_column = ""
            
                  while True:
                        try:
                              if combination == 0:
                                    race_column = combination = 0
                                    break

                              elif combination == 1:
                                    cli_prints.printCombinationsOne()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 7):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 2:
                                    cli_prints.printCombinationsTwo()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 16):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 3:
                                    cli_prints.printCombinationsThree()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 21):
                                          break
                                    else:
                                          print("Please enter a valid input\n")
                              
                        except ValueError:
                              print("Please give a valid input\n")
                  race_name = race_population.column_int_to_string(race_column, combination)
                  total_race_population = race_population.get_national_total_population(year, race_name)
                  print("The total population of", race_name, "in the US is", total_race_population, "\n")
            
            elif user_selection_one == 4:
                  while (True):
                        cli_prints.printAllStates()
                        try:
                              state = input("Enter a number for a state of interest:\n")
                                       
                              if (str(state).lower() == "quit"):
                                    exit()

                              state = int(state)

                              if (state > 0 and state < 53):
                                    break
                              else:
                                    print("Please enter a valid input\n")
                              
                        except ValueError:
                              print("Please give a valid input\n")

                  while(True):
                        cli_prints.printCombinationOptions()
                        try:
                              combination = input("Enter a number for the combination you are interested in:\n")

                              if (str(combination).lower() == "quit"):
                                    exit()

                              combination = int(combination)

                              if (combination > -1 and combination <4):
                                    break
                              else:
                                    print("Please enter a valid input\n")

                        except ValueError:
                              print("Please enter a valid input\n")

                  race_column = ""
            
                  while True:
                        try:
                              if combination == 0:
                                    race_column = combination = 0
                                    break

                              elif combination == 1:
                                    cli_prints.printCombinationsOne()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 7):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 2:
                                    cli_prints.printCombinationsTwo()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 16):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 3:
                                    cli_prints.printCombinationsThree()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 21):
                                          break
                                    else:
                                          print("Please enter a valid input\n")
                              
                        except ValueError:
                              print("Please give a valid input\n")
                              
                  
                  
                  state_name = race_population.row_int_to_string(state)
                  race_name = race_population.column_int_to_string(race_column, combination)
                  total_state_race_population = race_population.get_state_total_population(year, state_name, race_name)
                  print("The total population of", race_name, "in the", state_name, "is", total_state_race_population, "\n")
            else:
                  print("Not a valid option")
                  
         
      elif user_selection == 2:
            while(True):
                  try:
                        user_selection_two = input("You selected \"Compare RACE or TOTAL populations (Different or Same State/Year)\".\nWhat would you like to look at? \n"
                              "(1) Compare TOTAL or RACE population in the same year or different year\n"
                              "(2) Compare population from different states in the same year or different year\n"
                              "(3) Compare population from the same state in 2010 to 2020\n")
                        
                        if (str(user_selection_two).lower() == "quit"):
                              exit()

                        user_selection_two = int(user_selection_two)

                        if (user_selection_two > 0 and user_selection_two < 4):
                              break
                        else:
                              print("Please enter a valid input\n")

                  except ValueError:
                        print("Please give a valid input.\n")
                  
            if user_selection_two == 1:

                  while(True):
                        cli_prints.printCombinationOptions()
                        try:
                              combination = input("Enter a number for the combination you are interested in:\n")

                              if (str(combination).lower() == "quit"):
                                    exit()

                              combination = int(combination)

                              if (combination > -1 and combination <4):
                                    break
                              else:
                                    print("Please enter a valid input\n")

                        except ValueError:
                              print("Please enter a valid input\n")

                  race_column = ""
            
                  while True:
                        try:
                              if combination == 0:
                                    race_column = combination = 0
                                    break

                              elif combination == 1:
                                    cli_prints.printCombinationsOne()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 7):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 2:
                                    cli_prints.printCombinationsTwo()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 16):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 3:
                                    cli_prints.printCombinationsThree()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 21):
                                          break
                                    else:
                                          print("Please enter a valid input\n")
                              
                        except ValueError:
                              print("Please give a valid input\n")

                  

                  race_name = race_population.column_int_to_string(race_column, combination)
                  difference = race_population.compare_total_population(race_name)
                  
                  if difference > 0:
                        print("The", race_name, "Population in 2020 was greater than in 2010 by a margin of", difference)
                  elif difference == 0:
                        print("The", race_name, "population has remained the same in the last decade")
                  else:
                        print("The", race_name, "Population in 2010 was greater than in 2020 by a margin of", abs(difference))

            elif user_selection_two == 2:
                  while True: 
                        try:
                              year_option = input("Look at data in (1) the same year or (2) in 2010 and 2020? Enter (1) or (2)\n")
                              
                              if (str(year_option).lower() == "quit"):
                                    exit()
                              
                              year_option = int(year_option)

                              if (year_option > 0 and year_option < 3):
                                    break
                              else:
                                    print("Please enter a valid input\n")

                        except ValueError:
                              print("Please give a valid input.\n")
                                    
                  while True: 
                        cli_prints.printAllStates()
                        try:
                              state_one = input("Select your first state of interest\n")
                              state_two = input("Select your second state of interest\n")
                              
                              if (str(state_one).lower() == "quit" or str(state_two).lower() == "quit"):
                                    exit()
                              
                              state_one = int(state_one)
                              state_two = int(state_two)

                              if (state_one > 0 and state_one < 53 and state_two > 0 and state_two < 53 ):
                                    break
                              else:
                                    print("Please enter a valid input\n")

                              break
                        except ValueError:
                              print("Please give a valid input.\n")
                  

                  state_one_name = race_population.row_int_to_string(state_one)        
                  state_two_name = race_population.row_int_to_string(state_two)

                  if year_option == 1:
                        while True:
                              try:
                                    year_input = input("Would you like to look at data in the year 2010 or 2020? Enter 2010 or 2020\n")

                                    if (str(year_input).lower() == "quit"): 
                                          exit()

                                    year_input = int(year_input)

                                    if (year_input == 2010 or year_input == 2020):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                                    break
                              except ValueError:
                                    pass

                        while(True):
                              cli_prints.printCombinationOptions()
                              try:
                                    combination = input("Enter a number for the combination you are interested in:\n")

                                    if (str(combination).lower() == "quit"):
                                          exit()

                                    combination = int(combination)

                                    if (combination > -1 and combination <4):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              except ValueError:
                                    print("Please enter a valid input\n")

                        race_column = ""
                  
                        while True:
                              try:
                                    if combination == 0:
                                          race_column = combination = 0
                                          break

                                    elif combination == 1:
                                          cli_prints.printCombinationsOne()
                                          race_column = input("Enter a number for your race of interest:\n")

                                          if (str(race_column).lower() == "quit"):
                                                exit()
                                          
                                          race_column = int(race_column)

                                          if (race_column > 0 and race_column < 7):
                                                break
                                          else:
                                                print("Please enter a valid input\n")

                                    elif combination == 2:
                                          cli_prints.printCombinationsTwo()
                                          race_column = input("Enter a number for your race of interest:\n")

                                          if (str(race_column).lower() == "quit"):
                                                exit()
                                          
                                          race_column = int(race_column)

                                          if (race_column > 0 and race_column < 16):
                                                break
                                          else:
                                                print("Please enter a valid input\n")

                                    elif combination == 3:
                                          cli_prints.printCombinationsThree()
                                          race_column = input("Enter a number for your race of interest:\n")

                                          if (str(race_column).lower() == "quit"):
                                                exit()
                                          
                                          race_column = int(race_column)

                                          if (race_column > 0 and race_column < 21):
                                                break
                                          else:
                                                print("Please enter a valid input\n")
                                    
                              except ValueError:
                                    print("Please give a valid input\n")
                        
                        race_name = race_population.column_int_to_string(race_column, combination)
                        difference = race_population.compare_by_same_year(year_input, state_one_name, state_two_name, race_name)

                        if difference > 0:
                              print("In", year_input, state_one_name, "had a greater", race_name, "population than", state_two_name, "with a margin of", difference)
                        elif difference == 0:
                              print("The population of", race_name, "in", state_one_name, "and", state_two_name, "is not any different.\n")
                        else:
                              print("In", year_input, state_two_name, "had a greater", race_name, "Population than", state_one_name, "with a margin of", abs(difference))
                  
                  elif year_option == 2:
                        
                        while True:
                              cli_prints.printCombinationOptions()
                              try:
                                    combination = input()

                                    if (str(combination).lower() == "quit"): 
                                          exit()

                                    combination = int(combination)
                                    
                                    if combination == 0:
                                          difference = race_population.compare_total_population("Total")
                                    elif combination == 1:
                                          cli_prints.printCombinationsOne()
                                    elif combination == 2: 
                                          cli_prints.printCombinationsTwo()
                                    elif combination == 3:
                                          cli_prints.printCombinationsThree()
                                    
                                    if combination != 0:
                                          race_column = input("Enter a number for your race of interest:\n")

                                    if (str(combination).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)
                                    
                                    break
                              except ValueError:
                                    print("Please give a valid input.\n")
                        
                        race_name = race_population.column_int_to_string(race_column, combination)

                        difference = race_population.compare_state_by_different_year(state_one_name, state_two_name, race_name)

                        if difference > 0:
                              print("In 2010", state_one_name, "had a greater", race_name, "population than 2020 with a margin of", difference)
                        elif difference == 0:
                              print("The population of", race_name, "in", state_one_name, "and", state_two_name, "is not any different.\n")
                        else:
                              print("In 2020", state_two_name, "had a greater", race_name, "Population than 2010 with a margin of", abs(difference))

                        
            elif user_selection_two == 3:
                  
                  while True:
                        try:
                              cli_prints.printAllStates()
                              state = input("You selected \"Compare population from the same state in 2010 to 2020\". Enter a number for a stat of interest:\n")

                              if (str(state).lower() == "quit"):
                                    exit()
                                    
                              state = int(state)

                              if (state > 0 and state < 53):
                                    break
                              else:
                                    print("Please enter a valid input\n")
                        except ValueError:
                              print("Please give a valid input.\n")
                  
                  state_name = race_population.row_int_to_string(state) 
                  difference = race_population.compare_state_by_different_year(state_name, state_name, 'Total')

                  if difference > 0:
                        print("In 2020", state_name, "had a greater population than in 2010 with a margin of", difference)
                  elif difference == 0:
                        print("The population of", state_name, "is not any different.\n")
                  else:
                        print("In 2010", state_name, "had a greater population than in 2020 with a margin of", abs(difference))

            else:
                  print("Not a valid option")                 

                                
      else:
            while True:
                  try:
                        while True:
                              user_selection_three = input("You selected \"Filter dataset based on RACE or TOTAL population (US or a State)\". \n"
                                          "(1) Filter total population of the US by state population or race population\n"
                                          "(2) Filter total population of a state by race\n")
                              
                              if (str(user_selection_three).lower() == "quit"):
                                    exit()

                              user_selection_three = int(user_selection_three)

                              if (user_selection_three > 0 and user_selection_three < 3):
                                    break
                              else:
                                    print("Please give a valid input\n")
                        
                        while True:
                              year = input("Would you like to look at data for 2010 or 2020? Enter 2010 or 2020:\n")

                              if (str(year).lower() == "quit"):
                                    exit()

                              year = int(year)

                              if (year == 2010 or year == 2020):
                                    break
                              else:
                                    print("Please give a valid input\n")
                        
                        while True:
                              ascending = input("What order do you want the dataset: (1) Ascending or (2) Descending\n")
                              if (str(ascending).lower() == "quit"):
                                    exit()
                              ascending = int(ascending)

                              if (ascending == 1 or ascending == 2):
                                    break
                              else:
                                    print("Please give a valid input\n")

                        while True:
                              length = input("How many states do you want to see printed out in filtered data\n")
                              if (str(length).lower() == "quit"):
                                    exit()
                              length = int(length)

                              if (length > 0):
                                    break
                              else:
                                    print("Please give a valid input\n")

                        break
                  except ValueError:
                        print("Please give a valid input.\n")
            
            if user_selection_three == 1:
                  while(True):
                        cli_prints.printCombinationOptions()
                        try:
                              combination = input("Enter a number for the combination you are interested in:\n")

                              if (str(combination).lower() == "quit"):
                                    exit()

                              combination = int(combination)

                              if (combination > -1 and combination <4):
                                    break
                              else:
                                    print("Please enter a valid input\n")

                        except ValueError:
                              print("Please enter a valid input\n")

                  race_column = ""
            
                  while True:
                        try:
                              if combination == 0:
                                    race_column = combination = 0
                                    break

                              elif combination == 1:
                                    cli_prints.printCombinationsOne()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 7):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 2:
                                    cli_prints.printCombinationsTwo()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 16):
                                          break
                                    else:
                                          print("Please enter a valid input\n")

                              elif combination == 3:
                                    cli_prints.printCombinationsThree()
                                    race_column = input("Enter a number for your race of interest:\n")

                                    if (str(race_column).lower() == "quit"):
                                          exit()
                                    
                                    race_column = int(race_column)

                                    if (race_column > 0 and race_column < 21):
                                          break
                                    else:
                                          print("Please enter a valid input\n")
                              
                        except ValueError:
                              print("Please give a valid input\n")
                  if ascending == 1:
                        ascending = True
                  else:
                        ascending = False
                  race_name = race_population.column_int_to_string(race_column, combination)
                  data_set = race_population.filter_states_by_population(year, race_name, ascending)
                  race_population.print_filtered_states(data_set, race_name, length)

            elif user_selection_three == 2:
                  while (True):
                        try:
                              cli_prints.printAllStates()
                              state_number = input("Enter a number for a state of interest:\n")

                              if (str(state_number).lower() == "quit"):
                                    exit()
                              state_number = int(state_number)

                              if (state_number > 0 or state_number < 53):
                                    break
                              else:
                                    print("Please give a valid input.\n")
                        except ValueError:
                              print("Please give a valid input.\n")
                        
                  state_name = race_population.row_int_to_string(state_number)
                  data_set = race_population.filter_race_populations_by_states(year, state_name, ascending)
                  race_population.print_filtered_races(data_set, state_name, length)

            else:
                  print("Gotcha")  