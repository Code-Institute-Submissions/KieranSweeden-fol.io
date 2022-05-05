window.addEventListener('DOMContentLoaded', () => {
    setupLicenseAmountBtn();
});

/**
 * Prepares the license amount
 * button when called
 */
function setupLicenseAmountBtn(){
    const licenseAmountInput = document.getElementById('id_no_of_licenses_purchased');
    if (licenseAmountInput) {
        licenseAmountInput.addEventListener('change', ({target}) => updatePrice(target.value));
        updatePrice(licenseAmountInput.value);
        licenseAmountInput.addEventListener('keyup', ({target}) => updatePrice(target.value));
        updatePrice(licenseAmountInput.value);
    }
}

/**
 * Updates price shown within license purchase screen
 * @param {number} licenseAmountSelected 
 */
function updatePrice(licenseAmountSelected){
    const LICENSE_PRICE = 2.99;
    const totalPriceShown = document.getElementById('licenseGrandTotal');

    updateSubmitPurchaseDisabledState(licenseAmountSelected);
    totalPriceShown.textContent = (LICENSE_PRICE * licenseAmountSelected).toFixed(2);
}

/**
 * Disables submit purchase button if number provided is less than 0
 * @param {number} licenseAmountSelected 
 */
function updateSubmitPurchaseDisabledState(licenseAmountSelected){
    const submitPurchaseBtn = document.getElementById('submitPurchase');
    if (licenseAmountSelected < 1){
        submitPurchaseBtn.disabled = true;
    } else {
        submitPurchaseBtn.disabled = false;
    }
}