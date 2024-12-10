function showDropdown() {
    //It retrieves the selected value, and based on different conditions, it sets the display CSS property of the dropdown elements to control their visibility.
    var selectBox = document.getElementById("raceCombination");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    var firstDropdown = document.getElementById("firstDropdown");
    var secondDropdown = document.getElementById("secondDropdown");
    var thirdDropdown = document.getElementById("thirdDropdown");

    if (selectedValue == "one") {
        firstDropdown.style.display = "block";
        secondDropdown.style.display = "none";
        thirdDropdown.style.display = "none";
    } else if (selectedValue == "two") {
        firstDropdown.style.display = "none";
        secondDropdown.style.display = "block";
        thirdDropdown.style.display = "none";
    } else if (selectedValue == "three") {
        firstDropdown.style.display = "none";
        secondDropdown.style.display = "none";
        thirdDropdown.style.display = "block";
    } else {
        firstDropdown.style.display = "none";
        secondDropdown.style.display = "none";
        thirdDropdown.style.display = "none";
    }
}

function filterDropdown() {
    //It retrieves the selected value, and based on different conditions, it sets the display CSS property of the dropdown elements to control their visibility.
    var filterBox = document.getElementById("filter");
    var filterValue = filterBox.options[filterBox.selectedIndex].value;
    
    var numStateBox = document.getElementById("numberStates");
    var numRaceBox = document.getElementById("numberRaces");
    
    var raceDisplay = document.getElementById("raceComDisplay");
    var combinationBox = document.getElementById("raceCombination");

    var firstDropdown = document.getElementById("firstDropdown");
    var secondDropdown = document.getElementById("secondDropdown");
    var thirdDropdown = document.getElementById("thirdDropdown");

    var fourthDropdown = document.getElementById("fourthDropdown");

    if (filterValue == "filterStates"){
        fourthDropdown.style.display = "none";
        numRaceBox.style.display = "none";
        raceDisplay.style.display = "block";
        numStateBox.style.display = "block";
        var combinationValue = combinationBox.options[combinationBox.selectedIndex].value;

        if (combinationValue == "one") {
            firstDropdown.style.display = "block";
            secondDropdown.style.display = "none";
            thirdDropdown.style.display = "none";
        } else if (combinationValue == "two") {
            firstDropdown.style.display = "none";
            secondDropdown.style.display = "block";
            thirdDropdown.style.display = "none";
        } else if (combinationValue == "three") {
            firstDropdown.style.display = "none";
            secondDropdown.style.display = "none";
            thirdDropdown.style.display = "block";
        } else {
            firstDropdown.style.display = "none";
            secondDropdown.style.display = "none";
            thirdDropdown.style.display = "none";
        }

    } else if (filterValue == "filterPopulations"){
        raceDisplay.style.display = "none";
        firstDropdown.style.display = "none";
        secondDropdown.style.display = "none";
        thirdDropdown.style.display = "none";
        numStateBox.style.display = "none";
        numRaceBox.style.display = "block";
        fourthDropdown.style.display = "block";
    } else {
        raceDisplay.style.display = "none";
        firstDropdown.style.display = "none";
        secondDropdown.style.display = "none";
        thirdDropdown.style.display = "none";
        fourthDropdown.style.display = "none";
        numStateBox.style.display = "none";
        numStateBox.style.display = "none";
    }
    
}