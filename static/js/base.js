/**
 * Base JavaScript file that's present within
 * all html files in the fol.io application.
 */
window.addEventListener('DOMContentLoaded', () => {
    timeoutMessagesIfPresent();
    addHelpSectionClickListener();
    enableTooltips();
});

/**
 * Using JavaScript code directly taken from the bootstrap 5
 * webpage, enable all tooltips present on the page.
 */
function enableTooltips(){
    // Code below was directly taken from https://getbootstrap.com/docs/5.0/components/tooltips/
    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * If the help section is present within the page,
 * enable to click listener so the user can open 
 * the help section.
 */
function addHelpSectionClickListener(){
    const helpSectionBtn = document.getElementById('helpSectionBtn');
    if (helpSectionBtn){
        helpSectionBtn.addEventListener('click', () => {
            toggleHelpSectionDisplayState();
        });
    }
}

/**
 * A minor helper function for readability purposes
 * that toggles the help section display state
 */
function toggleHelpSectionDisplayState(){
    const helpSection = document.getElementById('helpSection');
    if (helpSection.classList.contains('hide')){
        helpSection.className = 'show';
    } else {
        helpSection.className = 'hide';
    }
}

/**
 * If messages exist on page, automatically hide
 * the messages after 5 seconds.
 */
function timeoutMessagesIfPresent(){
    const messages = [...document.getElementsByClassName('card-message')];
    if (messages){
        for (let message of messages) {
            setTimeout(hideMessage, 5000, message);
            addCloseClickListener(message);
        }
    }
}

/**
 * Hides a message from the user
 * @param {HTMLLIElement} message - Card message list element
 */
function hideMessage(message){
    message.classList.remove("animate__fadeInRight");
    message.classList.add("animate__fadeOutRight");
    setTimeout(removeMessage, 1000, message);
}

/**
 * Removes a message from the DOM
 * @param {HTMLLIElement} message - A card message list element
 */
function removeMessage(message){
    message.remove();
}

/**
 * Adds a close button listener to close icon within message
 * @param {HTMLLIElement} message - A card message list element
 */
function addCloseClickListener(message){
    const closeButton = [...message.getElementsByClassName('btn-icon')][0];
    closeButton.addEventListener('click', () => hideMessage(message));
}