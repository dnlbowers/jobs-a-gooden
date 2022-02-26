
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