/**
 * JavaScript file that is used for interactivity
 * regarding the project snippets found within
 * the suite application
 */
window.addEventListener('DOMContentLoaded', () => {
    setupCheckBoxClickListeners();
    assessTheAmountOfProjectCheckboxesChecked();
    setupUpdateProjectsInFolioFunctionality();
});

/**
 * Provided checkboxes are present on page,
 * add a change listener for each checkbox
 * that toggles it's checked status and
 * updates the displayed amount of checked projects
 */
function setupCheckBoxClickListeners(){
    const projectCheckBoxes = [...document.getElementsByClassName('form-check-input')];
    projectCheckBoxes.forEach(projectCheckBox => {
        projectCheckBox.addEventListener('change', (event) => {
            event.target.toggleAttribute("checked");
            assessTheAmountOfProjectCheckboxesChecked();
        });
    });
}

/**
 * Makes sure that no more than 4 projects
 * are checked at one time
 */
function assessTheAmountOfProjectCheckboxesChecked(){
    const MAX_AMOUNT_OF_PROJECTS_ALLOWED = 4;
    const projectCheckBoxes = [...document.getElementsByClassName('form-check-input')];
    const checkedProjectCheckboxes = projectCheckBoxes.filter(checkbox => checkbox.hasAttribute('checked'));
    const uncheckedCheckBoxes = projectCheckBoxes.filter(checkbox => !checkbox.hasAttribute('checked'));

    updateNumberOfProjectsSelected(checkedProjectCheckboxes.length);

    if (checkedProjectCheckboxes.length >= MAX_AMOUNT_OF_PROJECTS_ALLOWED){
        disableUncheckedProjectCheckboxes(uncheckedCheckBoxes);
    } else {
        const disabledCheckboxes = projectCheckBoxes.filter(checkbox => checkbox.hasAttribute('disabled'));
        enableDisabledProjectCheckboxes(disabledCheckboxes);
    }
}

/**
 * Updates the element that displays how many projects
 * are selected and defaults to 0 if none are checked
 * @param {number} checkedProjectsAmount 
 */
function updateNumberOfProjectsSelected(checkedProjectsAmount = 0){
    const elementDisplayed = document.getElementById('selectedNumberOfProjects');
    elementDisplayed.textContent = checkedProjectsAmount;
}

/**
 * Disables each checkbox within
 * the list that's send to it
 * @param {[HTMLInputElement]} uncheckedCheckBoxes 
 */
function disableUncheckedProjectCheckboxes(uncheckedCheckBoxes){
    for (let checkbox of uncheckedCheckBoxes) {
        checkbox.disabled = true;
    }
}

/**
 * Enables each checkbox within
 * the list that's send to it
 * @param {[HTMLInputElement]} disabledCheckboxes 
 */
function enableDisabledProjectCheckboxes(disabledCheckboxes){
    for (let checkbox of disabledCheckboxes) {
        checkbox.disabled = false;
    }
}

/**
 * Adds an event listener to the
 * save changes button on the page
 */
function setupUpdateProjectsInFolioFunctionality(){
    const saveChangesButton = document.getElementById("updateProjectsInFolioBtn");
    saveChangesButton.addEventListener('click', updateProjectsInFolio);
}

/**
 * Sends an AJAX request to update the projects
 * attached to the folio viewed on page by grabbing
 * all checkboxes that represent projects and extracts
 * project related data from them
 */
function updateProjectsInFolio(){
    const folioID = window.location.pathname.split('/')[3];
    const checkboxes = [...document.getElementsByClassName('form-check-input')];

    const projectCheckboxes = checkboxes.filter(checkbox => !checkbox.id.includes("image-clear_id"));

    let listOfProjects = [];
    for (let projectCheckBox of projectCheckboxes){
        listOfProjects.push(returnProjectObject(projectCheckBox));
    }

    let request = new XMLHttpRequest();
    const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            location.reload();
        }
    };

    request.open("POST", `/suite/projects/update/projects_attached/${folioID}/`, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    request.send(`{"projects":${JSON.stringify(listOfProjects)}}`);
}

/**
 * Extracts and returns project related data
 * from a checkbox sent to it
 * @param {HTMLInputElement} projectCheckbox 
 * @returns object containing id and is_attached status
 */
function returnProjectObject(projectCheckbox){
    return {
        id: projectCheckbox.id,
        is_attached: projectCheckbox.hasAttribute("checked")
    };
}