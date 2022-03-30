window.addEventListener('DOMContentLoaded', (event) => {

    // Ensure checkboxes can be checked & unchecked
    setupCheckBoxClickListeners();
    
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
        });
    });
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
    const projectCheckBoxes = [...document.getElementsByClassName('form-check-input')];
    const projectsAttachedIDs = projectCheckBoxes.filter(returnProjectIDIfChecked);

    console.log(projectsAttachedIDs)

    // Create AJAX Request & csrf token
    // let request = new XMLHttpRequest();
    // const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // request.onreadystatechange = function() {
    //     if (this.readyState == 4 && this.status == 200) {
    //         location.reload();
    //     }
    // }

    // request.open("POST", `/suite/projects/update/projects_attached/${folioID}/`, true);
    // request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    // request.send(`{"projects":${JSON.stringify(projectIDs)}}`);
}

function returnProjectIDIfChecked(projectCheckBox){
    return projectCheckBox.hasAttribute("checked") ? projectCheckBox.id : false;
}