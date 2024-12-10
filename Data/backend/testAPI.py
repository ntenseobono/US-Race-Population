import unittest

import api

class APITester(unittest.TestCase):


    def test_twenty_ten_nat_total_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_national_total_population(2010, 'Total'), 312471327)
        '''
        Tests retrieval of 2010 Census total US population.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_nat_race_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_national_total_population(2010, 'White_Asian'), 1624556)
        '''
        Tests retrieval of 2010 Census total US population.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_state_total_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_state_total_population(2010, 'Ohio', 'Total'), 11536504) 
        '''
        Tests retrieval of 2010 Census total population of a specified state.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''
                         
    def test_twenty_ten_state_race_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_state_total_population(2010, 'Maine', 'White_Asian'), 3932) 
        '''
        Tests retrieval of 2010 Census race population of a specified state.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_compare_nat_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_total_population('Total'), 22263828) 
        '''
        Tests the comparsion between the total US population of 2020 to 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_compare_nat_race(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_total_population('Black_Native_Hawaiian'), -4733) 
        '''
        Tests the comparsion between the national population of a race of 2020 to 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_compare_same_year_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_by_same_year(2010, 'Louisiana', 'Massachusetts', 'Total'), 2014257) 
        '''
        Tests the comparison between two different states' total population in 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_compare_same_year_race(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_by_same_year(2010, 'Florida', 'South Carolina', 'White_Asian_Native_Hawaiian'), -1388) 
        '''
        Tests the comparison between two different states' population of race in 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_compare_diff_year_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_state_by_different_year('Nevada', 'Colorado', 'Total'), 3073163) 
        '''
        Tests the comparison between two different states' total population, the first state in 2020 and the second state in 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_compare_diff_year_race(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_state_by_different_year('Michigan', 'Tennessee', 'Black_Other'), 3523) 
        '''
        Tests the comparison between two different states' population of a race, the first state in 2020 and the second state in 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_filter_states_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertIs(type(race_Api.filter_states_by_population(2010, 'Total', True)), list) 
        '''
        Tests if a list of states ordered by their total populations is returned
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_ten_filter_states_race(self):
        race_Api = api.RacePopulationAPI()
        self.assertIs(type(race_Api.filter_states_by_population(2010, 'American_Indian', False)), list) 
        '''
        Tests if a list of states ordered by their populatiom of a race is returned
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''
    
    def test_twenty_ten_filter_populations_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertIs(type(race_Api.filter_race_populations_by_states(2010, 'Alabama', True)), list) 
        '''
        Tests if a list of race groups ordered by their population in a state is returned
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''



    def test_twenty_twenty_nat_total_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_national_total_population(2020, 'Total'), 312471327)
        '''
        Tests retrieval of 2020 Census total US population.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''
    def test_twenty_twenty_nat_race_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_national_total_population(2020, 'White_Asian'), 1624556)
        '''
        Tests retrieval of 2020 Census total US population.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''
    def test_twenty_twenty_state_total_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_state_total_population(2020, 'Ohio', 'Total'), 11536504) 
        '''
        Tests retrieval of 2020 Census total population of a specified state.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''           
    def test_twenty_twenty_state_race_pop(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.get_state_total_population(2020, 'Maine', 'White_Asian'), 3932) 
        '''
        Tests retrieval of 2020 Census race population of a specified state.
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_twenty_compare_same_year_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_by_same_year(2020, 'Louisiana', 'Massachusetts', 'Total'), 2014257) 
        '''
        Tests the comparison between two different states' total population in 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''
    def test_twenty_twenty_compare_same_year_race(self):
        race_Api = api.RacePopulationAPI()
        self.assertEqual(race_Api.compare_by_same_year(2020, 'Florida', 'South Carolina', 'White_Asian_Native_Hawaiian'), -1388) 
        '''
        Tests the comparison between two different states' population of race in 2010
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_twenty_filter_states_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertIs(type(race_Api.filter_states_by_population(2020, 'Total', True)), list) 
        '''
        Tests if a list of states ordered by their total populations is returned
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''

    def test_twenty_twenty_filter_states_race(self):
        race_Api = api.RacePopulationAPI()
        self.assertIs(type(race_Api.filter_states_by_population(2020, 'American_Indian', False)), list) 
        '''
        Tests if a list of states ordered by their populatiom of a race is returned
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''
    def test_twenty_twenty_filter_populations_total(self):
        race_Api = api.RacePopulationAPI()
        self.assertIs(type(race_Api.filter_race_populations_by_states(2020, 'Alabama', True)), list) 
        '''
        Tests if a list of race groups ordered by their population in a state is returned
        
        Args:
        self: used to implement assertion command.
        
        Returns:
        "." for pass, "E" for error, and "F" for fail.
        '''        
if __name__ == "__main__":
    unittest.main()