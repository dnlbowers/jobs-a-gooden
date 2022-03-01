//Global constant references for elements in the DOM
const pinToggleRef = document.querySelectorAll('#flexSwitchCheckDefault')


document.addEventListener("DOMContentLoaded", () => {
    pinToggleRef.forEach( pin => {
        pin.addEventListener('click', () => {
            if(pin.checked){
                console.log("checked and pinned")
            } else {
                console.log("unchecked and unpinned")
            };
        })
       
    });

});