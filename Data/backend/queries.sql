/* List the total population of the US by adding all the states population */
SELECT SUM("Total")
FROM racepopulation;

/*Get the white population of the selected state Idaho */
SELECT White FROM racepopulation WHERE Label ILIKE /*pass in parameter*/ AND White IS NOT NULL;

/* Get all the racial population in the state of Alabama */
SELECT * FROM racepopulation WHERE Label ILIKE 'Alabama';

SELECT * FROM c_states;

/* retrieves "White Alone" race group row under all 3 states*/
SELECT * FROM c_states WHERE Label ILIKE '%White Alone%';


/* retrieves "Black or African American alone" rows only under California */
SELECT California FROM c_states WHERE Label ILIKE '%Black or African American alone%' AND California IS NOT NULL;


/* retrieves "American Indian and Alaska Native alone" rows only under Connecticut"*/
SELECT Connecticut FROM c_states WHERE Label ILIKE '%American Indian and Alaska Native alone%' AND Connecticut IS NOT NULL;