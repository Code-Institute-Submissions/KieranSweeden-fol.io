// Base JavaScript file for all pages
window.addEventListener('DOMContentLoaded', (event) => {
    
    timeoutMessagesIfPresent();

    addHelpSectionClickListener();
});


function addHelpSectionClickListener(){
    const helpSectionBtn = document.getElementById('helpSectionBtn');
    if (helpSectionBtn){
        helpSectionBtn.addEventListener('click', () => {
            toggleHelpSectionDisplayState(helpSectionBtn);
        });
    }
}

function toggleHelpSectionDisplayState(helpSectionBtn){
    const helpSection = document.getElementById('helpSection');
    helpSection.classList.contains('hide') ? helpSection.className = 'show' : helpSection.className = 'hide';
}

/**
 * If messages exist on page, automatically hide
 * the messages after 5 seconds.
 */
function timeoutMessagesIfPresent(){
    const messages = [...document.getElementsByClassName('card-message')];
    if (!messages?.length) return;

    for (let message of messages) {
        setTimeout(hideMessage, 5000, message);
        addCloseClickListener(message);
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
    closeButton.addEventListener('click', () => {hideMessage(message)})
}