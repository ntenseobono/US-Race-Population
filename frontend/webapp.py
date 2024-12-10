'''
Our website using Flask. For the "Flask integration" deliverable, our query of interest was,
"What is the total population of African Americans in the US in 2020?". We have implemented it so that
the user get to and chose the necessary options, and retrieve that information.
'''
import api
import flask
from flask import render_template, request
import json
import sys

population_api = api.RacePopulationAPI()

app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    '''
    Renders the home page of the website.
    '''
    return render_template('home.html')

@app.route('/home')
def go_home():
    '''
    Renders the home page of the website.
    '''
    return render_template('home.html')

@app.route('/trynow')
def trynow():
    '''
    Renders the options the user can choose to obtain specific information.
    '''
    return render_template('data.html')

@app.route('/results', methods = ['GET'])
def results():
    '''
    Takes in the information given by the user to render for a results page.
    '''
    year = int(request.args.get('year'))
    state = request.args.get("selectState")
    race = get_race(request)
    
    race_name = race_html_print(race)
    
    # Determines the total-population option the user wants by seeing if a state input was passed
    if not state:
        number = population_api.get_national_total_population(year, race)
        state = 'None'
    else:
        number = population_api.get_state_total_population(year, state, race)
    
    formatted_number = "{:,}".format(number) 
    response = render_template('population_results.html', year=year, race=race_name, number=formatted_number, state=state)
    return response

def get_race(request):
    '''
    Uses user given information on a web page to extract the user's chosen race.

    Every race in the dataset is grouped by the number of unique races a person is composed of.
    Combination is used to check if the user wishes to look at information regarding people
    descending from one race, several races, or no race in particular ("total")

    Args:
    request: information given by the user from a web page

    Return:
    The specific race the user chose from the web page
    ''' 
    combination = request.args.get("raceCombination")
    if combination == 'Total':
        race = 'total'
    elif combination == 'one':
        race = request.args.get('select_race_one')
    elif combination == 'two':
        race = request.args.get('select_race_two')
    else:
        race = request.args.get('select_race_three')
    return race

@app.route('/compare_results', methods = ['GET'])
def compare_results():
    '''
    Takes in the information given by the user to render for a comparison results page.
    '''
    year = request.args.get('year')
    firstState = request.args.get("firstState")
    secondState = request.args.get("secondState") 
    race = get_race(request)
    race_name = race_html_print(race)

    # Determines the comparison option the user wants by seeing if a year input was passed
    if not year:
        # No year input given so the firstState input represents the users 2010 state and secondState represents the users 2020 input
        number = population_api.compare_state_by_different_year(firstState, secondState, race)
        first_state_number = population_api.get_state_total_population(2010, firstState, race)
        second_state_number = population_api.get_state_total_population(2020, secondState, race)
        year = 0
    else:
        year = int(year)
        number = population_api.compare_by_same_year(year, firstState, secondState, race)
        first_state_number = population_api.get_state_total_population(year, firstState, race)
        second_state_number = population_api.get_state_total_population(year, secondState, race)

    # Determines if the difference between second_state_number and first_state_number is positive or
    # negative for signaling the larger population on compare_results.html
    if number < 0:
        check_number = 'positive'
    else:
        check_number = 'negative'

    first_state_number = "{:,}".format(first_state_number)
    second_state_number = "{:,}".format(second_state_number)
    abs_number = abs(number)
    formatted_number = "{:,}".format(abs_number) 
    response = render_template('compare_results.html', year=year, race=race_name, number=formatted_number, firstState=firstState,
                               secondState=secondState, check_number=check_number, firstStatePopulation=first_state_number,
                               secondStatePopulation=second_state_number)
    return response

@app.route('/filter_results', methods = ['GET'])
def filter_results():
    '''
    Takes in the information given by the user to render for a filtered results page.
    '''
    year = int(request.args.get('year'))
    state = request.args.get("selectState")
    order = request.args.get("order")
    filter_choice = request.args.get('filter')

    if order == "Ascending":
        order = True
    else:
        order = False
    
    if filter_choice == "filterStates":
        race = get_race(request)
        number = int(request.args.get('numberStates'))
        filtered_data = population_api.filter_states_by_population(year, race, order, number)
        race = race.capitalize()
        return render_template('filter_results.html', year=year, filter=filter_choice, race=race, filtered_data=filtered_data)
        
    elif filter_choice == "filterPopulations":
        state = request.args.get("selectState")
        number = int(request.args.get('numberRaces'))
        filtered_data = population_api.filter_race_populations_by_states(year, state, order, number)
        return render_template('filter_results.html', year=year, filter=filter_choice, state=state, filtered_data=filtered_data)

def race_html_print(race: str):
    '''
    Changes the string of a race name for displaying on the website results page 

    Args: 
    race (str): name of a race to be modified

    Returns:
    The race name where semicolons are replaced by commas
    '''
    race = race.replace(";", ", ")
    return race

@app.route('/national_total')
def national_total():
    '''
    Renders the page for obtaining information on a race or the whole US population nationally.
    '''
    return render_template('national_total.html')

@app.route('/race_population')
def race_population():
    '''
    Renders the page for obtaining information on a race or the whole population in a state.
    '''
    return render_template('race_total.html')

@app.route('/filter_dataset')
def filter_dataset():
    '''
    Renders the page for obtaining information on states in order of lowest-to-highest population in total or for a race, 
    or on races in order of lowest-to-highest population in the US or a state.
    '''
    return render_template('filter_dataset.html')

@app.route('/compare_same_year')
def compare_same_year():
    '''
    Renders the page for obtaining the race population difference between two states in the same year.
    '''
    return render_template('compare_same_year.html')

@app.route('/compare_diff_year')
def compare_diff_year():
    '''
    Renders the page for obtaining the race population difference between two states in different years.
    '''
    return render_template('compare_diff_year.html')

@app.route('/about')
def about():
    '''
    Renders the "about" page.
    '''
    return render_template('about.html')

@app.route('/why')
def why():
    '''
    Renders the "why" page for the purposes of the website and project.
    '''
    return render_template('why.html')

'''
Run the program by typing 'python3 localhost [port]', where [port] is one of 
the port numbers you were sent by my earlier this term.
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

