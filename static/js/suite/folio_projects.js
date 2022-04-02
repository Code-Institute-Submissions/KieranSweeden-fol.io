window.addEventListener('DOMContentLoaded', (event) => {

    // Ensure checkboxes can be checked & unchecked
    setupCheckBoxClickListeners();

    // Assess amount of checkboxes checked
    assessTheAmountOfProjectCheckboxesChecked();
    
    // Setup the abilty to update projects
    setupUpdateProjectsInFolioFunctionality();

});

function setupCheckBoxClickListeners(){

    // Get all project checkboxes on page
    const projectCheckBoxes = [...document.getElementsByClassName('form-check-input')];

    // Apply click listener to checkboxes
    projectCheckBoxes.forEach(projectCheckBox => {
        projectCheckBox.addEventListener('change', (event) => {
            event.target.toggleAttribute("checked");
            assessTheAmountOfProjectCheckboxesChecked();
        });
    });
}

function assessTheAmountOfProjectCheckboxesChecked(){
    // Init max amount of projects & grab checkboxes on page
    const MAX_AMOUNT_OF_PROJECTS_ALLOWED = 4;
    const projectCheckBoxes = [...document.getElementsByClassName('form-check-input')];
    const checkedProjectCheckboxes = projectCheckBoxes.filter(checkbox => checkbox.hasAttribute('checked'));
    const uncheckedCheckBoxes = projectCheckBoxes.filter(checkbox => !checkbox.hasAttribute('checked'));

    // Update number of projects selected on page
    updateNumberOfProjectsSelected(checkedProjectCheckboxes.length);

    if (checkedProjectCheckboxes.length >= MAX_AMOUNT_OF_PROJECTS_ALLOWED){
        disableUncheckedProjectCheckboxes(uncheckedCheckBoxes);
    } else {
        const disabledCheckboxes = projectCheckBoxes.filter(checkbox => checkbox.hasAttribute('disabled'));
        enableDisabledProjectCheckboxes(disabledCheckboxes);
    }

}

function updateNumberOfProjectsSelected(checkedProjectsAmount = 0){
    // Grab element on page
    const elementDisplayed = document.getElementById('selectedNumberOfProjects');

    // Update value
    elementDisplayed.textContent = checkedProjectsAmount;
}

function disableUncheckedProjectCheckboxes(uncheckedCheckBoxes){
    for (checkbox of uncheckedCheckBoxes) {
        checkbox.disabled = true;
    }
}

function enableDisabledProjectCheckboxes(disabledCheckboxes){
    for (checkbox of disabledCheckboxes) {
        checkbox.disabled = false;
    }
}

function setupUpdateProjectsInFolioFunctionality(){
    // Grab save button
    const saveChangesButton = document.getElementById("updateProjectsInFolioBtn");

    // Apply event listener
    saveChangesButton.addEventListener('click', updateProjectsInFolio);
}

function updateProjectsInFolio(){
    
    // Grab folio from URL & project ID's from checkboxes
    const folioID = window.location.pathname.split('/')[3];
    const projectCheckboxes = [...document.getElementsByClassName('form-check-input')];

    // Create a list of project objects containing their IDs & a status on if they're attached
    let listOfProjects = [];
    for (let projectCheckBox of projectCheckboxes){
        listOfProjects.push(returnProjectObject(projectCheckBox))
    }

    // Create AJAX Request & csrf token
    let request = new XMLHttpRequest();
    const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Attach function for when request has been successfully made
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            location.reload();
        }
    }

    // Prepare request to be sent with headers & send
    request.open("POST", `/suite/projects/update/projects_attached/${folioID}/`, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    request.send(`{"projects":${JSON.stringify(listOfProjects)}}`);
}

function returnProjectObject(projectCheckbox){
    return {
        id: projectCheckbox.id,
        is_attached: projectCheckbox.hasAttribute("checked")
    }
}