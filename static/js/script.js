//Global constant references for elements in the DOM
const pinToggleRef = document.querySelectorAll('#flexSwitchCheckDefault')


document.addEventListener("DOMContentLoaded", () => {
    /**
     * Adds event listeners to the pin job toggle switches
     * And triggers is_pinned field in the database to be updated.
     */
    pinToggleRef.forEach( pin => {
        pin.addEventListener('change', () => {
            if(pin.checked){
                
                console.log("checked and pinned")
            } else {
                
                console.log("unchecked and unpinned")
            };
        })
       
    });

});