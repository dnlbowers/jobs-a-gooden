//Global constant references for elements in the DOM
// Warning Modal references
const warningModalRef = document.getElementById('warningModal');
const closeWarningModalRef = document.querySelectorAll('.cancel-warning');
const acceptWarningRef = document.querySelector('.accept-warning');
const warnModalBodyRef = document.getElementById('warning-message');
const acceptWarningBtnRef = document.querySelector('.accept-warning');

// Note/insight related element references
const deleteNoteBtnRef = document.querySelectorAll('.delete-note-btn');
const noteItemRef = document.querySelectorAll('.accordion-item');
const notesAccordionRef = document.getElementById('notes-accordion');
const insightItemRef = document.querySelectorAll('.insight-container');
const insightTimelineRef = document.getElementById('timeline')

// Job related element references
const jobPreviewRef = document.querySelectorAll(".job-preview");
const deleteJobBtnRef = document.querySelectorAll('.job-del-button');
const pinToggleRef = document.querySelectorAll('.pin');

// reference to the page URL
const pinnedUrlRef = window.location.href.includes("pinboard");
const fullSpecUrlRef = window.location.href.includes("fulldetails");
const paginatedUrlRef = window.location.href.includes("page");
const insightUrlRef = window.location.href.includes("insights");


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

    // fetch headers constant
    const headersRef = new Headers({
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': csrftoken,
        'X-Requested-With': 'XMLHttpRequest',
        })
    
    //Load event listeners
    deleteNoteEvents()
    deleteJobEvents()
    loadPinJobEvents()
    if (warningModalRef){
        warningModalEvents()
    } 

//----------------------------------------------------------Pin job related functionality

    /**
    * Communicates with the back end and Updates the database
    * Without the need to refresh the page.
    */
    function togglePinnedJob(status, id) {
        fetch(`/pinned/${id}/`, {
            method: 'POST',
            headers: headersRef,
            body: `status=${status}`,
            credentials: 'same-origin',
        })
        .then(response => response.text())
        .then(data => {
            console.log(status)
            // Checks if the user in on the saved jobs page
            if (data == 200  && pinnedUrlRef){
                if (!status) {
                    removeJobPreview(id);
                }
            } else if (data == 200) { 
                if (status) {
                    if(fullSpecUrlRef) {
                        $('#notes-section').show();
                        return window.location.reload(true);
                    }
                } else {
                    if(fullSpecUrlRef) {
                        $('#notes-section').hide();
                        return window.location.reload(true);
                    }
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
            console.log(job)
            let pinnedJob = job.getAttribute('data-job-preview')

            if (pinnedJob === jobId) {
                
                if(jobPreviewRef.length === 1) {
                    previousPageRedirect();
                    return window.location.reload(true);
                } else {
                    $(job).hide();
                    return window.location.reload(true)
                }
            }
        })
    }

    //----------------------------------------------------------Pagination
    
    /**
     * Take the page number from the url minus 1
     * before redirecting the user to the previous page
     */
    const previousPageRedirect = () => {
        
        let page = window.location.href.substr(-1)-1;
        if (!isNaN(page)) {
            if (page != 0){
                page - 1;
                let previousPage = window.location.href.slice(0, -1) + page;
                return window.location.replace(previousPage)
            }
        }
    }

//----------------------------------------------------------delete Notes related functionality

    /**
     * Communicates with the backend toggling the status on pinned job
     * and updates the database accordingly
     */
    function deleteNote(noteId) {
        fetch(`/${noteId}/deletenote/`, {
            method: 'POST',
            headers: headersRef,
            body: ``,
            credentials: 'same-origin',
        })
        .then(response => response.text())
        .then(data => {
            console.log("data", data);
            if (data == 200) {
                if (fullSpecUrlRef) {
                    removeNote(noteId);
                } else if (insightUrlRef) {
                    removeInsight(noteId);
                }    
            }

        })
        .catch(error => console.log(`ERROR: ${error}`));
    }
    
    /**
     * Loops through the note accordion and when the data attribute id
     * matches the noteId parameter the relevant child containing the note
     * is removed
     */
    const removeNote = (noteId) => {
        noteItemRef.forEach(note => {

            let noteSection = note.getAttribute('data-note-item')
            
            if (noteSection === noteId) {
                notesAccordionRef.removeChild(note);
            }
        })
    }

    /**
     * Loops through the insights timeline and when the data attribute id
     * matches the noteId parameter the relevant child containing the insight
     * is removed
     */
    const removeInsight = (noteId) => {
        insightItemRef.forEach(insight => {
            let insightSection = insight.getAttribute('data-insight-item')

            if (insightSection === noteId) {
                insightTimelineRef.removeChild(insight);
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
            headers: headersRef,
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

                if (status){
                    togglePinnedJob(status, id);
                } else {
                    warningModal(true, id, 'unpinJob');
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
                        // if unpin job cancelled slides the toggle back to pinned position
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
            } else if (btnTxt === 'Delete Entry') {
                deleteNote(id);
                if (insightUrlRef){
                    if (insightItemRef.length === 1){
                        previousPageRedirect();
                    }                        
                }
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

    /**
     * Populates the modal according to the passed parameter(str)
     */
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

    /**
     * Clears modal and acceptance button inner html 
     */
    function clearWarningModal() {
        warnModalBodyRef.innerHTML='';
        acceptWarningBtnRef.innerHTML=''
    }
    
    /**
     * Inputs content form modal when unpinning a job
     */
    function unpinJobWarning(){
        warnModalBodyRef.innerHTML=`
            <p>By unpinning this post you will be deleting all its associated notes.</p>
            <p>Your insights will still be visible form the insights page.</p>
            <p>Are you Sure you Wish to Unpin this Job post?</p>
        `;
        acceptWarningBtnRef.innerHTML='Unpin Job';
    }

    /**
     * Inputs content form modal when deleting a note
     */
    function deleteNoteWarning() {
        warnModalBodyRef.innerHTML = `
            <p>Deleting this note/insight is irreversible.</p>
            <p>Once deletion is confirmed this information wil be lost forever.</p>
            <p>Are you Sure you Wish to delete?</p>
        `;
        acceptWarningBtnRef.innerHTML='Delete Entry';
        
    }

    /**
     * Inputs content form modal when deleting a job
     */
    function deleteJobWarning() {
        warnModalBodyRef.innerHTML = `
        <p><strong>Have you checked the admin panel to see if a user has this job pinned?</strong></p>
        <p>Deleting this Job is irreversible.</p>
        <p>Once deletion is confirmed this information wil be lost forever,</p>
        <p>along with all related notes for all users (insights will be safe safely stored on their insights page).</p>
        <p> Are you Sure you Wish to delete?</p>
    `;
    acceptWarningBtnRef.innerHTML='Delete Job';
    }
});