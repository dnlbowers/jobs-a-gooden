//Global constant references for elements in the DOM

// Job pinning related element elements
const pinToggleRef = document.querySelectorAll('.pin');
const unpinModalRef = document.getElementById('unpinned-modal');
const closeUnpinModalRef = document.querySelectorAll('.cancel-unpin');
const confirmUnpinRef = document.querySelector('.confirm-unpin')

// Note related element references
const deleteNoteBtnRef = document.querySelectorAll('.delete-note-btn');
const noteItemRef = document.querySelectorAll('.accordion-item');
const notesAccordionRef = document.getElementById('notes-accordion')

// Job related element references
const jobPreviewRef = document.querySelectorAll(".job-preview")
const deleteJobBtnRef = document.querySelectorAll('.job-del-button')

// reference to the page URL
const pinnedUrlRef = window.location.href.includes("pinboard")
const fullSpecUrlRef = window.location.href.includes("fulldetails")

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
            let status = event.target.checked;
            let id = pin.dataset.id;
            // make fetch request to update the database
            if (status){
                console.log("toggle on")
                togglePinnedJob(status, id);
            } else {
                showUnpinWarning(id);
                console.log("toggle off")
            }
            
        });
    });

    closeUnpinModalRef.forEach( closeModalBtn => {
        closeModalBtn.addEventListener('click', () => {
            pinToggleRef.forEach( pin => {
                if (pin.dataset.id === confirmUnpinRef.dataset.id){
                    console.log('triggered');
                    pin.checked;
                }
            })
            closeUnpinWarning();
            
        })
    })

    confirmUnpinRef.addEventListener('click', () => {
        let id = confirmUnpinRef.dataset.id;
        console.log(id)
        togglePinnedJob(false, id);
        closeUnpinWarning();
    })


    /**
     * Adds event listeners to the delete notes button
     */
    deleteNoteBtnRef.forEach( delBtn => {
        delBtn.addEventListener('click', () => {
            // const clicked = event.type;
            const noteId = delBtn.dataset.id;
            deleteNote(noteId);
        })
    })

    deleteJobBtnRef.forEach( delBtn => {
        delBtn.addEventListener('click', () => {
            const jobId = delBtn.dataset.id;
            deleteJob(jobId);
        })
    })

    /**
     * Makes fetch request toggling the status on pinned job
     * and updates the database accordingly
     */
    function togglePinnedJob(status, id) {
        fetch(`/pinned/${id}/`, {
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
            console.log(status)
            if (data == 200  && pinnedUrlRef){
                if (status == false) {
                    removeJobPreview(id);
                }

            } else if (data == 200) {
                if (status == true) {
                    $('#notes-section').show(); //.animate({width: 'toggle'}, {duration: 1000});
                } else {
                    $('#notes-section').hide(); //.animate({width: 'toggle'}, {duration: 1000});
                } 
            }
            console.log(data); 
        })
        .catch(error => console.log(`ERROR: ${error}`));
    }

    /**
     * Makes fetch request toggling the status on pinned job
     * and updates the database accordingly
     */
    function deleteNote(id) {
        fetch(`/${id}/deletenote/`, {
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

    /**
     * Makes fetch request to delete job
     * and updates the database accordingly
     */
    function deleteJob(id) {
        fetch(`/fulldetails/${id}/delete`, {
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
            if (fullSpecUrlRef && data == 200){
                window.location.replace('/');
            } else if (data == 200) {
                removeJobPreview(id)
            }
        })
        .catch(error => console.log(`ERROR: ${error}`));
    }

    
    const removeNote = (noteId) => {
        console.log(noteId)
        console.log(noteItemRef)
        noteItemRef.forEach(note => {

            let noteSection = note.getAttribute('data-note-item')
            
            if (noteSection === noteId) {
                notesAccordionRef.removeChild(note)
            }
        })
    }

    const removeJobPreview = (jobId) => {
        jobPreviewRef.forEach(job => {
            let pinnedJob = job.getAttribute('data-job-preview')

            if (pinnedJob === jobId) {
                $(job).hide(); //.animate({width: 'toggle'}, {duration: 1000});
                window.location.reload()
            }
        })
    }

    function showUnpinWarning(jobId) {
        unpinModalRef.classList.remove('d-none');
        unpinModalRef.classList.add('show');
        confirmUnpinRef.setAttribute('data-id', jobId);
    }

    function closeUnpinWarning() {
        unpinModalRef.classList.add('d-none');
        unpinModalRef.classList.remove('show');
        confirmUnpinRef.removeAttribute('data-id');
    }

    //const removeDeleteJob = (jobId) => {

    //}
});