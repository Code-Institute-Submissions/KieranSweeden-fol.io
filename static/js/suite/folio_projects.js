window.addEventListener('DOMContentLoaded', (event) => {
    
    // Setup the abiltiy to update projects
    setupUpdateProjectsInFolioFunctionality();

});

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
    const projectIDs = projectCheckBoxes.map(projectCheckBox => projectCheckBox.id);

    // Create AJAX Request & csrf token
    let request = new XMLHttpRequest();
    const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            location.reload();
        }
    }

    request.open("POST", `/suite/projects/update/projects_attached/${folioID}/`, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    request.send(`{"projects":${JSON.stringify(projectIDs)}}`);
}