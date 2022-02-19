# Jobs-A-Gooden
As a developing developer, job hunting is something I have found at the forefront of 
everyone's mind. The app aims to be a proof of concept using a single API to fetch 
current job roles and provide a method for the user to pin jobs and make notes to 
track the status of their application processes and any insights gained along the way.

[Deployed site](https://jobs-a-gooden.herokuapp.com/)

## Strategy 
On average, it takes a new developer around 20-25 interviews to land their first 
developer job, and this does not include the total amount of applications sent out 
but a job seeker.

It can be hard to keep track of job specs when a company responds, especially 
when using multiple sites to check for roles, or worse yet, several months 
have passed since you sent the application.

This app aims to streamline the process by using an  API to search for job posts 
from various companies and once applied for, the job spec would be neatly stored 
to refer back to later. 

Doing this will allow the user to know what is expected during the selection process 
and make it easier for the candidate to research the potential employer upon 
response to their application. The personal board would also allow the user to make 
notes to review their insights of the process and any company feedback.

### Opportunities:
The was a long range of features during my brain storming session for this site. I had to use a feasibility chart to narrow the down and prioritize the scope of the intended strategy. 

Opportunity | Importance | Viability/Feasibility
---|---|---
Job search | 5 | 5
User can pin jobs | 5 | 5
User specific job notes | 5 | 5
Landing page with site overview | 5 | 5
Progress tracker (Kanban board) | 3 | 1
Direct application to jobs | 2 | 1 
Manually add jobs (admin/employer) | 5 | 5
Jobs blog | 1 | 3
Tips/resources | 2 | 4
Personal insights | 5 | 5 
Employer ratings | 1 | 5 
Number of users applied | 1 | 1 
User log in | 5 | 5
Direct email to employer with CV/cover letter attachments | 2 | 1 
Community mentorship | 1 | 1
Freelance specific jobs board | 1 | 1
API to fetch jobs data | 5 | 2 
User profile | 5 | 5
----------------------------------------|----|----
Totals | 59 | 60 

Viability and feasibility in the above table is based on both time and current level of ability using different languages/frameworks. 

## Scope

Due to the imbalance in scores above there will definitely be some tradeoffs, however, I anticipate that there will need to be some trade offs due to the time set for this project. 

I have further divided this table into 3 categories to help prioritize the order of importance and clarify the MVP required to launch as a basic proof of concept whilst meeting the above objective. These three categories are:-
* UX efforts **must** address these:
    * Job search.
    * User can pin Jobs.
    * Landing pae with site overview.
    * Manually add jobs (admin/employer).
    * User specific job notes.
    * Personal insights.
    * User login.
    * User profiles.
* UX efforts **should** accommodate these:
    * Progress tracker (Kanban board).
    * Tips/resources.
    * API to fetch jobs data
* Unwise use of time to address there:
    * Direct application to jobs.
    * Jobs blog.
    * Employer ratings.
    * Number of users applied.
    * Direct email to employer with CV/cover letter attachments.
    * Community mentorship.
    * Freelance specific jobs board.

## Structure   

### Flow Charts:
![User Journeys flow chart](docs/flowcharts/user-Journey.jpg)

* What state changes need alerts? log in, log out, 404, 500, pop up for apply. 
Make a section in the features with screenshots vut reference this here.

## Skeleton
### wireframes:
![Homepage wireframes](docs/wireframes/homepage.png)
![Full job details wireframes](docs/wireframes/job-full-details.png)
![Job opening page wireframes](docs/wireframes/jobs-openings.png)
![Pinned jobs page wireframes](docs/wireframes/pinned-jobs.png)

## Surface
### Color scheme:

###Typography:

##Data Model
![Entity-Relationship-Model](docs/data-model/data-entity-relationship.jpg)
[*** REVISED Entity-Relationship-Model***](https://drawsql.app/student-444/diagrams/ci-pp4-job-search/embed)


## Credits
* Flow chart symbol meaning taken from [conceptdraw.com](https://www.conceptdraw.com/How-To-Guide/flow-chart-symbols)
* Guidance on file structure for templates folder from [learndjango.com article](https://learndjango.com/tutorials/template-structure)
* [Article on writing good user stories](https://www.industriallogic.com/blog/as-a-developer-is-not-a-user-story/)