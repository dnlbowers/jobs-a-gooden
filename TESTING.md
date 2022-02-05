
## Bugs and Fixes
* Issue - On the epic  called "initial deployment"  the final user story was to deploy to heroku. When deploying I was getting an application error 
when loading the app on heroku.
* Cause - Checking the logs via the heroku console I could see it was having issues when looking my .env file. This was purposely not a tracked file 
to protect sensitive data such as the SECRET KEY and other privileged information which should never be stored publicly on GitHub. 
* Solution - As a result I had to add a conditional statement to the import of the .env file containing the config vars required to run this application
from my local machine. The basis of this conditional was, if the file exists then run the app using the contained config variables, if the file does not exist it would skip the import process
completely and in this case take the config vars entered on the heroku app settings instead.