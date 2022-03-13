//Global constant references for elements in the DOM
const pinFormRef = document.getElementById('pin-form')
const pinToggleRef = document.querySelectorAll('.pin')
const pinSubmitRef = document.querySelector('.pin-submit-btn')

document.addEventListener("DOMContentLoaded", () => {
    /**
     * Adds event listeners to the pin job toggle switches
     * And triggers is_pinned field in the database to be updated.
     */
    pinToggleRef.forEach( pin => {
        pin.addEventListener('click', () => {
            if(pin.checked){
                pinSubmitRef.click()
                console.log("checked and pinned")
            } else {
                pinSubmitRef.click()
                console.log("unchecked and unpinned")
            };
        })
    });

});