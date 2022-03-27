
## Bugs and Fixes
* Issue - On the epic  called "initial deployment"  the final user story was to deploy to heroku. When deploying I was getting an application error 
when loading the app on heroku.
* Cause - Checking the logs via the heroku console I could see it was having issues when looking my .env file. This was purposely not a tracked file 
to protect sensitive data such as the SECRET KEY and other privileged information which should never be stored publicly on GitHub. 
* Solution - As a result I had to add a conditional statement to the import of the .env file containing the config vars required to run this application
from my local machine. The basis of this conditional was, if the file exists then run the app using the contained config variables, if the file does not exist it would skip the import process
completely and in this case take the config vars entered on the heroku app settings instead.

* Issue - When I pushed my code to GitHub it detected from the requirements.txt that Django 3.2 was installed, however without the latest security patches.
* Cause - I used the Code institute recommended pip install Django==3.2 gunicorn command to install django during the initial deployment This installation did not include the latest security patches.
* Solution - I upgraded to the latest patch of this Django version with "pip install --upgrade django==3.2.12" and the error disappeared.

* Issue - early on in the project I was finding API all required O-auth which was not working with the taught fetch method. I found reed employment had an API which used basic authentication however when using it from my local host it was getting blocked.
* Cause - Lack of understanding in API's requiring Oauth authentication.
* Solution - Since this was very early on in the project I decided to not spend a a lot of time on it. I was able to pull the data using the endpoint and api key in the browser address bar and saved that data to a Json file. This would serve as test data to build the site and I would come back to the API issue at a later stage.

* Issue - I was having a lot of trouble inserting my card component from within the job_search app into the required job-list page.
* Cause - At first I thought it was a file path issue however after much research I found [this article](https://www.geeksforgeeks.org/include-django-template-tags/) showing quotation marks being used with the include property.
* Solution - Adding the quotation marks around the correct relative filepath resolved the issue.

* Issue - Linking my custom base.html in the allauth template wasn't working no matter what filepath I was using.
* Cause - Due to my file structure using base.html only in the extends property wasn't enough, after a lot of dead end research I looked at the allauth views file to see where it was looking for the templates and saw it was checking the settings file.
* Solution - By adding os.path.join(BASE_DIR, 'templates', 'packages/allauth') I was able to redirect the project to look here for my all auth templates and enabling me to keep my packages separate to my customer code.

* Issue - Errors on postgres database migrations.
* Cause - Whilst coming to terms with how to use the model portion of django I recreated the models multiple times, this caused various errors when migrating changes to the database.
* Solution - I deleted the postgres database form heroku and my migration files and added a new Postgres server to heroku. I then re-ran the migration commands to start the database over from scratch. Once migrated I also needed to re add the job data for testing purposes and recreate the super user.

* Issue - Without touching my code in between coding sessions When trying to run the server locally I was having an error message saying it could not connect to my heroku postgres server database. 
* Cause - Due to an [Heroku maintenance](docs/images/heroku-maintenance.jpg) my DATABASE_URL had changed causing my local .env file to be out of date. 
* Solution - Updating the DATABASE_URL resolved the issue with running the server locally. This

* Issue - Pinned jobs not showing in the job list as pinned but showing as pinned in the full job spec.
* Causes - I was trying to use a form with a hidden submit button and using JS to hit the button on click of the pin job toggle. This caused issues in that I could not retrieve the data from the generic list view on the job list page. As such I was unable see which posts were pinned unless on the full job post itself.
* Solution - This was abandoned and I decided to use Javascript to handle the post request as opposed to the form. This caused the issue to resolve how ever gave rise to the below bug

* Issue - Pinned jobs displayed correctly on on all pages but could not be edited from the full job spec page.
* Cause - When attempting to toggle the job is_pinned status from the full job details page it was adding /pinned/{job.id} to the end of the url already containing the job id, causing a 404 error.
* Solution - adding "../" to the start of the fetch url in the javascript file allowed the toggle to always start from the root url when updating the pinned job status. 

* Issue - Bootstrap accordion wasn't closing a section when opening a new one.
* Cause - When tailoring the boot strap code I failed to match the accordion ID with the data-bs-parent.
* Solution - Once these two attributes were set to the same ID then the accordion opened and close as expected on section at a time.

* Issue - Notes left where were not user specific and all notes could be seen by all users.
* Cause - There was no variable defined in the view which allowed me to use the logged in user as part of the conditional in the template.
* Solution - By setting the author variable in the the view.py I was able to match the requesting user user id in the Notes model so to show the user their own notes.

* Issue - If refreshing after submitting a note then a duplicate note is added to the database.
* Cause - Page was refreshing but not redirecting upon for submission
* Solution - By adding ```return HttpResponseRedirect(reverse('note_made', args=[id]))``` after the form save which points to a new URL path upon submit, this fixed the issue of resubmitting the same form inputs twice.

* Issue - Pagination not working when displaying the job preview cards on the pinned posts page.
* cause - I initially created a functional view to display pinned posts this did not allow for pagination.
* Solution - By using the generic class ListView with using get_queryset to add the additional information required to render this feature using a generic class view.    

**Issues to fix **
* Issue - Notes and pinned post remained until page refresh even when deleted/unpinned
  
* Issue - When pinning a post from the full view one has to refresh before seeing the note feature.


