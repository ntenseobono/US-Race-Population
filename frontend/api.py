import psycopg2
import psqlConfig as config
from psycopg2.extensions import AsIs

class RacePopulationAPI:

    def __init__(self):
        '''
        Connects to our database and holds arrays for every race every state/territory the website
        the website can display information for
        ''' 
        self.connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        self.cursor = self.connection.cursor()
        
        self.race_list = [  "Total",	"White"	, "Black" ,	"American Indian",	"Asian", 	"Native Hawaiian",	"Other", 	
                            "White; Black" ,	"White; American Indian",	"White; Asian",	"White; Native Hawaiian",	"White; Other",	
                            "Black; American Indian",	"Black; Asian",	"Black; Native Hawaiian",	"Black; Other",	
                            "American Indian; Asian",	"American Indian; Native Hawaiian", "American Indian; Other",	
                            "Asian; Native Hawaiian",	"Asian; Other",	"Native Hawaiian; Other",	
                            "White; Black; American Indian",	"White; Black; Asian",	"White; Black; Native Hawaiian",	
                            "White; Black; Other",	"White; American Indian; Asian",	"White; American Indian; Native Hawaiian",	
                            "White; American Indian; Other",	"White; Asian; Native Hawaiian",	"White; Asian; Other",	
                            "White; Native Hawaiian; Other",	"Black; American Indian; Asian",	"Black; American Indian; Native Hawaiian",	
                            "Black; American Indian; Other",	"Black; Asian; Native Hawaiian",	"Black; Asian; Other",	
                            "Black; Native Hawaiian; Other",	"American Indian; Asian; Native Hawaiian",	
                            "American Indian; Asian; Other",	"American Indian; Native Hawaiian; Other",	
                            "Asian; Native Hawaiian; Other"]

        self.state_list = [ 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                            'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
                            'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
                            'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
                            'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
                            'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                            'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico']
    
    def column_syntax(self, race: str):
        '''
        Changes the string of a race name to match it with the 
        column it refers to in the database

        Args: 
        race (str): name of a race to be modified

        Returns:
        String of the race name, matching the column it refers to in the database
        '''
        race_name = race.lower().replace(" ", "_").replace(";", "")
        return race_name
        
    def get_national_total_population(self, year: int, race: str): 
        '''
        Retrieves the total population of the US or the total population of a race in the US for a given year from the US census dataset.

        Args:
        year (int): year number corresponding to the dataset (2010 or 2020)
        race (str): the column from the dataset that corresponds to the users selected race
        
        Returns:
        A integer representing the total US population or total population of a selected race from the US census dataset.

        '''
        race = self.column_syntax(race)
        query = "SELECT SUM(%s) FROM racepopulation_%s"
        self.cursor.execute(query, (AsIs(race), year))
        result = self.cursor.fetchone()[0]
        return result


    def get_state_total_population(self, year: int, state: str, race: str):
        '''
        Retrieves the population of a state, either total population or population of a race.
        
        Args:
        year (int): year number corresponding to the dataset (2010 or 2020)
        state (str): representation of the selected state
        race (str): representation of the selected race group  
        
        Returns:
        A integer of the total population of 1 or all races in a state.

        '''
        race = self.column_syntax(race)
        query = "SELECT %s FROM racepopulation_%s WHERE Label ILIKE %s AND %s IS NOT NULL" 
        self.cursor.execute(query, ((AsIs(race)), year, state, (AsIs(race))))
        state_population = self.cursor.fetchone()[0]
        return int(state_population)                

    def compare_total_population(self, race: str): 
        '''
        Compares the total race populations of 2020 and 2010.

        Args:
        race (str): the column from the dataset that corresponds to a race

        Returns:
        The difference between both total race populations of each respective year.

        '''
        race = self.column_syntax(race)
        difference = self.get_national_total_population(2020, race) - self.get_national_total_population(2010, race)
        return difference

    def compare_by_same_year(self, year: int, state_one: str, state_two: str, column: str):
        '''
        Compares the race populations of two states from the same year (2010 or 2020). 

        Args: 
        year (int): year number corresponding to the dataset (2010 or 2020)
        state_one (str): code for the first state (2010 or 2020 depending on the same year selected)
        state_two (str): code for the second state (2010 or 2020 depending on the same year selected)
        column (str): the option the user chose for a specific race / the integer representation of a race by the array called race_list

        Returns:
        The difference in the race populations of two states.

        '''
        state_one = int(self.get_state_total_population(year, state_one, column))
        state_two = int(self.get_state_total_population(year, state_two, column))
        difference = state_two - state_one
        return difference

    def compare_state_by_different_year(self, state_one: str, state_two: str, column: str):
        '''
        Compare the race data for two states in a given year, based on the specified race or total.s

        Args:
        state_one (int): row corresponding to the first state the user wants compared from the 2010 dataset
        state_two (int): row corresponding to the second state the user wants compared from the 2020 dataset
        column (str): the column from the dataset that corresponds to a race

        Returns:
        The calculated difference between the 2020 state and the 2010 state.

        '''
        state_one = int(self.get_state_total_population(2010, state_one, column))
        state_two = int(self.get_state_total_population(2020, state_two, column))
        difference = state_two - state_one
        return difference
 
    def filter_states_by_population(self, year: int, column: str, ascending: bool, counter: int ):
        '''
        Filters the states in the dataset by population by sorting in ascending/descendin order.

        Args:
        year (int): represents the year of the chosen dataset
        column (str): the column from the dataset that corresponds to a race
        ascending (bool): determines to sort the data in ascending/descending data 

        Returns:
        The sorted data as a list of only one selected column values and state.

        '''
        race = self.column_syntax(column)
        if ascending == True:
            query = "SELECT Label,%s FROM racepopulation_%s ORDER BY %s ASC"
        else:
            query = "SELECT Label,%s FROM racepopulation_%s ORDER BY %s DESC"
        self.cursor.execute(query, (AsIs(race), year, AsIs(race)))
        sorted_data = self.cursor.fetchmany(counter)
        return sorted_data
    
    def filter_race_populations_by_states(self, year: int, state: str, ascending: bool, counter: int): 
        '''
        Filters the race populations based on the given states in ascending/descending order.

        Args:
        year (int): represents the year selected 
        state (str): reprsents the state to be selected from the dataset
        ascending (bool): determines to sort the data in ascending/descending data

        Returns:
        The sorted data as a list.
 
        '''
        
        sorted_list = []
        tupled_list = []

        query = "SELECT * FROM racepopulation_%s WHERE Label ILIKE %s"
        self.cursor.execute(query, (year, state))
        unsorted_list = self.cursor.fetchall()
        races = self.race_list[1:]
        start_count = 2
        for i in range(len(races)):
            tupled_list.append((races[i], unsorted_list[0][start_count]))
            start_count += 1
        if ascending == True:
            sorted_list = sorted(tupled_list, key = lambda x: x[1])
        else:
            sorted_list = sorted(tupled_list, key = lambda x: x[1], reverse=True)
        
        sorted_list = sorted_list[:counter]
        return sorted_list    
