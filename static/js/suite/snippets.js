window.addEventListener('DOMContentLoaded', (event) => {
    // Ensure checkboxes can be checked & unchecked
    setupCheckBoxClickListeners();


    // Setup the functionality to save changes made
    setupSaveSnippetChangesFunctionality();
});

function setupCheckBoxClickListeners(){
    // Get all snippet checkboxes on page
    const snippetCheckBoxes = getSnippetCheckboxes();

    // Apply click listener to snippet checkboxes on page
    snippetCheckBoxes.forEach(snippetCheckBox => {
        snippetCheckBox.addEventListener('change', (event) => {
            event.target.toggleAttribute("checked");
        });
    });
}

function setupSaveSnippetChangesFunctionality(){
    // Grab save changes button
    const saveChangesButton = document.getElementById("updateSnippetsBtn");

    // Apply event listener
    saveChangesButton.addEventListener('click', gatherListOfSnippetObjectsReadyToBeSent);
}

function gatherListOfSnippetObjectsReadyToBeSent(){
    // Grab snippet checkboxes
    const snippetCheckBoxes = getSnippetCheckboxes();

    // Create a list of snippet objects containing their IDs & a status on if they're attached
    let listOfSnippetObjects = [];
    for (let snippetCheckbox of snippetCheckBoxes){
        listOfSnippetObjects.push(returnSnippetObjectWithIdAndAttachedStatus(snippetCheckbox))
    }

    sendSnippetChangesToServer(listOfSnippetObjects);
}

function returnSnippetObjectWithIdAndAttachedStatus(snippetCheckBox){
    return {
        id: snippetCheckBox.id,
        is_attached: snippetCheckBox.hasAttribute("checked")
    }
}

function sendSnippetChangesToServer(listOfSnippets){
    // Create AJAX Request & csrf token
    let request = new XMLHttpRequest();
    const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Attach function for when request has been successfully made
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            location.reload();
        }
    }

    let snippetRequestKeyword = getSnippetKeywordForRequests(getSnippetType());

    const folioID = window.location.pathname.split('/')[3];
    // Prepare request to be sent with headers & send
    request.open("POST", `/suite/${snippetRequestKeyword}/update/${snippetRequestKeyword}_attached/${folioID}/`, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);

    request.send(`{${JSON.stringify(snippetRequestKeyword)}:${JSON.stringify(listOfSnippets)}}`);
}

function getSnippetCheckboxes(){
    return [...document.getElementsByClassName('form-check-input')];
}

function getSnippetKeywordForRequests(snippetType){
    let snippetRequestKeyword;
    if (snippetType === "project"){
        snippetRequestKeyword = "projects";
    } else if (snippetType === "skill"){
        snippetRequestKeyword = "skills";
    } else if (snippetType === "profile"){
        snippetRequestKeyword = snippetType;
    }
    return snippetRequestKeyword;
}

function getSnippetType(){
    const currentURLPath = window.location.pathname;
    const evaluateURLPath = (snippetType) => {
        if (currentURLPath.includes(snippetType)){
            return currentURLPath;
        }
    }

    let snippetType;
    switch (currentURLPath) {
        case evaluateURLPath('project'):
            snippetType = "project"
            break;
        case evaluateURLPath('skill'):
            snippetType = "skill"
            break;
        case evaluateURLPath('profile'):
            snippetType = "profile"
            break;
    }

    return snippetType;
}