/**
 * JavaScript file that is used for interactivity
 * regarding skill & profile snippets found within
 * the suite application
 */
window.addEventListener('DOMContentLoaded', () => {
    setupCheckBoxClickListeners();
    setupSaveSnippetChangesFunctionality();
    updateSnippetsSelectedCounter();
});

/**
 * Updates the element that displays
 * the amount of snippets that have been selected
 */
function updateSnippetsSelectedCounter(){
    const snippetCheckBoxes = getSnippetCheckboxes();
    const snippetsSelectedCounter = document.getElementById('snippetsSelectedCounter');
    const selectedSnippets = snippetCheckBoxes.filter((snippetCheckbox) => snippetCheckbox.checked === true);
    snippetsSelectedCounter.textContent = selectedSnippets.length;
}

/**
 * Adds change listeners to snippet
 * checkboxes so their states can be updated
 * and update the element displaying amount
 * of snippets selected
 */
function setupCheckBoxClickListeners(){
    const snippetCheckBoxes = getSnippetCheckboxes();
    if (snippetCheckBoxes) {
        snippetCheckBoxes.forEach(snippetCheckBox => {
            snippetCheckBox.addEventListener('change', (event) => {
                event.target.toggleAttribute("checked");
                updateSnippetsSelectedCounter();
            });
        });
    }
}

/**
 * Adds click listener to the save changes button
 * that appears on the page, making sure a list 
 * of snippets are gathered when clicked
 */
function setupSaveSnippetChangesFunctionality(){
    const saveChangesButton = document.getElementById("updateSnippetsBtn");
    saveChangesButton.addEventListener('click', gatherListOfSnippetObjectsReadyToBeSent);
}

/**
 * Creates a list array that contains all
 * snippet checkboxes on the page
 */
function gatherListOfSnippetObjectsReadyToBeSent(){
    const snippetCheckBoxes = getSnippetCheckboxes();

    let listOfSnippetObjects = [];
    for (let snippetCheckbox of snippetCheckBoxes){
        listOfSnippetObjects.push(returnSnippetObjectWithIdAndAttachedStatus(snippetCheckbox));
    }

    sendSnippetChangesToServer(listOfSnippetObjects);
}

/**
 * Extracts snippet information from a checkbox
 * and returns the info as an object
 * @param {HTMLInputElement} snippetCheckBox 
 * @returns object containing snippet id and is attached status
 */
function returnSnippetObjectWithIdAndAttachedStatus(snippetCheckBox){
    return {
        id: snippetCheckBox.id,
        is_attached: snippetCheckBox.hasAttribute("checked")
    };
}

/**
 * With the list of snippets given, this sends
 * an AJAX request to the server to update as to
 * what snippets are attached to the folio currently being viewed
 * @param {[HTMLInputElement]} listOfSnippets 
 */
function sendSnippetChangesToServer(listOfSnippets){
    let request = new XMLHttpRequest();
    const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            location.reload();
        }
    };

    let snippetRequestKeyword = getSnippetKeywordForRequests(getSnippetType());

    const folioID = window.location.pathname.split('/')[3];
    request.open("POST", `/suite/${snippetRequestKeyword}/update/${snippetRequestKeyword}_attached/${folioID}/`, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    request.send(`{${JSON.stringify(snippetRequestKeyword)}:${JSON.stringify(listOfSnippets)}}`);
}

/**
 * Gathers all of the snippet checkboxes
 * on the page and returns them within an array list
 * @returns an array of snippet checkboxes
 */
function getSnippetCheckboxes(){
    return [...document.getElementsByClassName('form-check-input')];
}

/**
 * Returns the keyword for a particular snippet type
 * @param {string} snippetType 
 * @returns keyword that's used within the server
 */
function getSnippetKeywordForRequests(snippetType){
    let snippetRequestKeyword;
    if (snippetType === "project"){
        snippetRequestKeyword = "projects";
    } else if (snippetType === "skill"){
        snippetRequestKeyword = "skills";
    } else if (snippetType === "profile"){
        snippetRequestKeyword = "profiles";
    }
    return snippetRequestKeyword;
}

/**
 * Looks at the current URL to decide
 * what snippets the application is currently
 * dealing with and returns the type as a string
 * @returns string representing a snippet type
 */
function getSnippetType(){
    const currentURLPath = window.location.pathname;
    const evaluateURLPath = (snippetType) => {
        if (currentURLPath.includes(snippetType)){
            return currentURLPath;
        }
    };

    let snippetType;
    switch (currentURLPath) {
        case evaluateURLPath('project'):
            snippetType = "project";
            break;
        case evaluateURLPath('skill'):
            snippetType = "skill";
            break;
        case evaluateURLPath('profile'):
            snippetType = "profile";
            break;
    }

    return snippetType;
}