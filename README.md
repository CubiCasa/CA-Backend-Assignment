# Welcome

Nice to meet you! We use this test at CubiCasa to evaluate all Python developer applicants before interviews. We hope you'll have fun with this assignment.

## Introduction

**Your Future Job** (YFJ) is a nonprofit service that helps high school students to choose a profession to follow.
The users of the system may be of 2 categories:
- Students: come to the system to get advice on the best matched jobs that they can follow after school
- Volunteers who come to help students by providing their data

**Stats service** is public service which investigates the labour market and can provide data regarding jobs and earnings. YFJ uses the data from stats for its computation but it doesn't own these data. The endpoint YFJ will consume from stats is _/job_earnings_ which provides a list of jobs together with average earning for each jobs

## Assignment

Your mission is to help YFJ build a RESTful Web Service that can be consumed by various frontend clients: web, mobile apps.

For that you should implement the endpoints for students and volunteers in YFJ site

1. Student can input his school performance as average scores for school subjects: Math, Physics, Chemistry, Biology, Literature, History, Geography, Phylosophy, Art and Foreign Language and get back 3 most apropriate jobs in recommendation. When student input data, the system stores his/her data for the future computation. Students can also update or delete their data at any time if they have concern regarding privacy.
The URL for student is `/{PeopleID}/advices`

2. Volunteers are people who have already landed on good jobs. They come back and use the URL `/{PeopleID}/jobs` to tell about their current job(s), so that the system can use those data to make a better recommendation to students.
Volunteer can come to system many times if he/she has changed job in various periods of life. But the prerequisite is that volunteer should input his/her school performance at least once before input data about job
The format of data to be input is like {jobs: [job1, job2, ...]}, e.g: a list of job name, nothing else.

3. Student and volunteer can come back to site at any moment and update or delete his/her data at will

**Note:**
- To maintain user's privacy, the PeopleID should not be stored as unencrypted text in the database 
- The most appropriate jobs are recommended based on student performance as well as the data about job earning from stats service.
- There is no unique solution in computing the recommended jobs, feel free to suggest one.
- You should not care about authentication or authorization, YFJ is open to wide public

## How to complete and what is expected

### Software needed to install
- https://docs.docker.com/ docker and docker-compose for working with container
- PostgresSQL client tools (such as https://www.pgadmin.org/) for manipulating database, our db service use PostgresSQL.

### How to run
1. Run all services with docker:
``docker-compose up -d``

2. Or run only db and stats services with docker and run flask for local development
``docker-compose up -d db stats``
``export FLASK_APP=app && flask run --port 9000``

To see output of Stats Service, browse to: `localhost:8000/job_earnings`

To see YFJ site, browse to:  `localhost:9000`

The above instructions are given for Linux user, please adapt to your system if you use another OS

### What we expect from you
- You do not have to make any modification to service stats or code in `stats` folder

- You work with the code in folder `yfj` to complete your assignment. 
    - While working with YFJ site you are allowed to add any libraries, made any modification to setup files, add new files, ...
    - Please update requirements.txt when adding new libraries
    - Please update migration when adding new models
    - Please make GIT commits as small as possible so we can review your development process step by step.

- You have 2 weeks to complete this assignment and submit your result to openpositions@cubicasa.com with following checklist:
    - GIT repo for your source code
    - Documentation files for your YFI RESTfull web service (Optional)
    - Screen shots to demo how your application running (Optional)



