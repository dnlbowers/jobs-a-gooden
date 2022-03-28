//Global constant references for elements in the DOM
const pinToggleRef = document.querySelectorAll('.pin');
const deleteNoteBtnRef = document.querySelectorAll('.delete-note-btn');
const noteSectionRef = document.querySelectorAll('.accordion-item');
const notesAccordionRef = document.getElementById('notes-accordion')
const notesSectionRef = document.getElementById('notes-section')

document.addEventListener("DOMContentLoaded", () => {
    /**
     * Retrieves cookie and saves the contained csrf token to a variable for later use
     * Code Taken from Django docs https://docs.djangoproject.com/en/3.2/ref/csrf/
     */
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    /**
     * Adds event listeners to the pin job toggle switches
     */
    pinToggleRef.forEach( pin => {
        pin.addEventListener('change', event => {
            // gets the status of the toggle switch
            const status = event.target.checked;
            const id = pin.dataset.id;
            // make fetch request to update the database
            togglePinnedJob(status, id);
            if(event.target.checked){ 
                $(notesSectionRef).show(1000)
                console.log("show")
            } else {
                $(notesSectionRef).hide(1000)
                console.log("hide")
            }
        });
    });

    /**
     * Adds event listeners to the delete notes button
     */
    deleteNoteBtnRef.forEach( delBtn => {
        delBtn.addEventListener('click', () => {
            // const clicked = event.type;
            const note_id = delBtn.dataset.id;
            console.log(note_id)
            deleteNote(note_id);
        })
    })

    /**
     * Makes fetch request toggling the status on pinned job
     */
    function togglePinnedJob(status, id) {
        fetch(`../pinned/${id}/`, {
            method: 'POST',
            headers: new Headers({
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest',
                }),
            body: `status=${status}`,
            credentials: 'same-origin',
        })
        .then(response => response.text())
        .then(data => {
            console.log(data); 
        })
        .catch(error => console.log(`ERROR: ${error}`));
    }

        /**
     * Makes fetch request toggling the status on pinned job
     */
        function deleteNote(id) {
            fetch(`/delete/${id}/`, {
                method: 'POST',
                headers: new Headers({
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken,
                    'X-Requested-With': 'XMLHttpRequest',
                    }),
                body: ``,
                credentials: 'same-origin',
            })
            .then(response => response.text())
            .then(data => {
                console.log("data", data);
                if (data == 200) {
                    removeNote(id);
                }
            })
            .catch(error => console.log(`ERROR: ${error}`));
        }

        
        const removeNote = (noteId) => {
            console.log(noteId)
            console.log(noteSectionRef)
            noteSectionRef.forEach(note => {
                let noteSection = note.getAttribute('data-note-item')
                
                if (noteSection === noteId) {
                    notesAccordionRef.removeChild(note)
                }
            })
        }
});