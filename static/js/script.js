//Global constant references for elements in the DOM

// Warning Modal references
const warningModalRef = document.getElementById('warningModal');
const closeWarningModalRef = document.querySelectorAll('.cancel-warning');
const acceptWarningRef = document.querySelector('.accept-warning');
const warnModalBodyRef = document.getElementById('warning-message');
const acceptWarningBtnRef = document.querySelector('.accept-warning');


// Note related element references
const deleteNoteBtnRef = document.querySelectorAll('.delete-note-btn');
const noteItemRef = document.querySelectorAll('.accordion-item');
const notesAccordionRef = document.getElementById('notes-accordion');

// Job related element references
const jobPreviewRef = document.querySelectorAll(".job-preview");
const deleteJobBtnRef = document.querySelectorAll('.job-del-button');
const pinToggleRef = document.querySelectorAll('.pin');

// reference to the page URL
const pinnedUrlRef = window.location.href.includes("pinboard");
const fullSpecUrlRef = window.location.href.includes("fulldetails");

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

    deleteNoteEvents()
    deleteJobEvents()
    loadPinJobEvents()
    warningModalEvents()

//----------------------------------------------------------Pin job related functionality

    /**
    * Communicates with the back end and Updates the database
    * Without the need to refresh the page.
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
            // Checks if the user in on the saved jobs page
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
     *  Removes job preview card from listViews
     */
    const removeJobPreview = (jobId) => {
        jobPreviewRef.forEach(job => {
            let pinnedJob = job.getAttribute('data-job-preview')

            if (pinnedJob === jobId) {
                $(job).hide(); //.animate({width: 'toggle'}, {duration: 1000});
                window.location.reload()
            }
        })
    }

//----------------------------------------------------------delete Notes related functionality

    /**
     * Communicates with the backend toggling the status on pinned job
     * and updates the database accordingly
     */
    function deleteNote(noteId) {
        fetch(`/${noteId}/deletenote/`, {
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
                removeNote(noteId);
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

    /**
     * Makes fetch request to delete a job post
     * and updates the database accordingly
     */
    function deleteJob(jobId) {
        fetch(`/fulldetails/${jobId}/delete`, {
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
                removeJobPreview(jobId)
            }
        })
        .catch(error => console.log(`ERROR: ${error}`));
    }

//---------------------------------------------------------- Event listeners

    /**
     * Event Listeners for note deletion buttons
     */
    function deleteNoteEvents() {

        deleteNoteBtnRef.forEach( delBtn => {
            delBtn.addEventListener('click', () => {
                const noteId = delBtn.dataset.id;
                warningModal(true, noteId, 'deleteNote');
            })
        })
    }

     /**
     * Event Listeners for job deletion buttons
     */
    function deleteJobEvents() {
        deleteJobBtnRef.forEach( delBtn => {
            delBtn.addEventListener('click', () => {
                const jobId = delBtn.dataset.id;
                warningModal(true, jobId, 'deleteJob');
            })
        })
    }

    /**
     * Triggers JS functionality relating to pinning and unpinning jobs
     */
    function loadPinJobEvents() {
        //Adds event listeners to the pin job toggle switches
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
                    warningModal(true, id, 'unpinJob');
                    console.log("toggle off")
                }
                
            });
        });
    }

     /**
     * Event Listeners for warning modal buttons
     */
    function warningModalEvents() {
        closeWarningModalRef.forEach( closeModalBtn => {
            closeModalBtn.addEventListener('click', () => {
                pinToggleRef.forEach( pin => {
                    let id = pin.dataset.id;
                    let btnTxt = acceptWarningBtnRef.innerHTML;

                    if ( id === acceptWarningRef.dataset.id && btnTxt === 'Unpin Job'){
                        pin.click();
                    };
                })
                warningModal(false, null, 'clear');
            })
        });

        acceptWarningRef.addEventListener('click', () => {
            let id = acceptWarningRef.dataset.id;
            let btnTxt = acceptWarningBtnRef.innerHTML; 
            if (typeof(id) === 'string' && btnTxt === 'Unpin Job') {
                togglePinnedJob(false, id);
            } else if (btnTxt === 'Delete Note') {
                deleteNote(id);
            } else if (btnTxt === 'Delete Job') {
                deleteJob(id);
            }
            
            warningModal(false, id);
        });
    }

    /**
     * Shows/hides Modal to warn user
     * assigns/removes Job ID to confirm button
     */
    function warningModal(display, Id, reason='clear') {
        populateWarning(reason)
        if (display) {
            warningModalRef.classList.remove('d-none');
            warningModalRef.classList.add('show');
            acceptWarningRef.setAttribute('data-id', Id);
        } else {
            warningModalRef.classList.add('d-none');
            warningModalRef.classList.remove('show');
            acceptWarningRef.removeAttribute('data-id'); 
        }
    }

    function populateWarning(reason){
        if (reason === 'clear'){
            clearWarningModal()
        }else if (reason === 'unpinJob'){
            unpinJobWarning()
        }else if (reason === 'deleteNote'){
            deleteNoteWarning()
        }else if (reason === 'deleteJob'){
            deleteJobWarning()
        }
    }

    function clearWarningModal() {
        warnModalBodyRef.innerHTML='';
        acceptWarningBtnRef.innerHTML=''
    }
    
    function unpinJobWarning(){
        warnModalBodyRef.innerHTML=`
            <p>By unpinning this post you will be deleting all its associated notes.</p>
            <p>Your insights will still be visible form the insights page.</p>
            <p>Are you Sure you Wish to Unpin this Job post?</p>
        `;
        acceptWarningBtnRef.innerHTML='Unpin Job';
    }

    function deleteNoteWarning() {
        warnModalBodyRef.innerHTML = `
            <p>Deleting this note/insight is irreversible.</p>
            <p>Once deletion is confirmed this information wil be lost forever.</p>
            <p>Are you Sure you Wish to delete?</p>
        `;
        acceptWarningBtnRef.innerHTML='Delete Note'
        
    }

    function deleteJobWarning() {
        warnModalBodyRef.innerHTML = `
        <p>Deleting this Job is irreversible.</p>
        <p>Once deletion is confirmed this information wil be lost forever,</p>
        <p>along with all related notes (insights will be safe safely stored on the insights page).</p>
        <p>Are you Sure you Wish to delete?</p>
    `;
    acceptWarningBtnRef.innerHTML='Delete Job';

    }


});