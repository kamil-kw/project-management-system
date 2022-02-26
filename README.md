![Hero image](images/readme_images/hero_responsive.png)

# ✔️ Project Management System 📔

## [See Live web](https://project-task.herokuapp.com/)

# Introduction

Welcome to my Fourth Full Stack Course project. This is a Project Management System.

The inspiration for this project was my side learning process of becoming a certified SCRUM master, as well as observation of project managers from my company using multiple trackers, which seemed impractical. As a SCRUM Master, one of the most needed items is to have a tool to collect and monitor workload, progress, and deadlines. The tool itself can be used in any project management world. In the current world, where Covid changed the way of doing the business and most of the things are done online, having a simple yet sufficient tool to track the progress of your team, project members and other function are essential to bringing efficiency to the company. 

The goal was to create a tool, which in the future can be adjusted according to the specific customer needs. 


<a name="tableOfContents"></a>

# Table of Contents

[**1. UX**](#ux)
* [**1.1. Strategy**](#strategy)
    * [**1.1.1 Project Goals**](#projectGoals)
    * [**1.1.2 User Stories**](#userStories)
    * [**1.1.3 KANBAN - Agile**](#kanban)

* [**1.2. Structure**](#structure)
* [**1.3. Skeleton**](#skeleton)
* [**1.4. Color Scheme**](#colorScheme)
* [**1.5. Data Base**](#dataBase)

[**2. Features**](#features)

[**3. Technologies Used**](#technologies)

[**4. Testing**](#testing)
* [**4.1 PEP8**](#pep)
* [**4.2 Manual Testing**](#manualTesting)
* [**4.3 Function tests**](#functionTest)

[**5. Development Cycle**](#development)

[**6. Deployment**](#deployment)

[**7. End Product**](#endProduct)

[**8. Known Bugs**](#knownBugs)
* [**8.1 Fixed bugs**](#fixedBugs)
* [**8.1 Remaining Bugs**](#remainBugs)

[**9. Credits**](#credits)

[Back to Table Of Content](#tableOfContents)

<a name="ux"></a>

# **1. UX**

As the next step on my path of becoming a software developer from zero to hero 😊, I'm presenting a Project Manager Tool. As mentioned in my last projects my ultimate goal is to change my career path and become a full-time developer. Here I will be showing my newly acquired skills, which are Django and DataBase. As part of my portfolio collection, which can be shown to my potential future employers, and potentially to be used by myself. I have decided to build a product that can support the day to day workload of Project Managers or SCRUM masters. The product is simple to use and intuitive, the navigation around the page is clear and gives users the ability to search and filter through things like date or status. The product can be adjusted in the future for specific customer needs, as well as certain features can be added if the business needs them. The current tool includes elements such as project name, task, due date, and owner. The tool can hold multiple projects, meaning the project manager or SCRUM master can have an overview of all actions open against each project they are working on. Having all in one space optimizes time and effort for task management.


[Back to Table Of Content](#tableOfContents)

<a name="strategy"></a>

# **1.1 Strategy**

<a name="projectGoals"></a>

#  **1.1.1 Project Goals**

A project goal was to create a set PM tool belt where project tasks can be monitored, this page has the potential to build more tools in upcoming project #5, where additional features like Gantt Chart, Critical Path, Delay Calculator, and Task Time Calculator could be added. Currently, the tool has abilities to store tasks against multiple projects, owners, and due dates. Users can select either a specific project or choose the owner of the task.
 
The reason for this web page is to create a tool that I can use as a potential PM SCRUM master in the future also to create a product that can be sellable. Therefore, in my thought process, I aimed to create a good basis in project #4 and expand on that in the future


<a name="userStories"></a>

## **1.1.2 User Stories - Agile**

![User Stories](images/readme_images/user_stories.png)

<a name="kanban"></a>

## **1.1.3 KANBAN Dashboard - Agile**

![KANBAN Dashboard](images/readme_images/KANBAN.png)

<a name="structure"></a>

# **1.2. Structure**

## **Wireframes**

### **Landing page**
<hr>

![Landing page](images/readme_images/testing/wireframes_landing.png)

### **Sign up page**
<hr>

![Sign up page](images/readme_images/testing/wireframes_signup.png)

### **Login page**
<hr>

![Login page](images/readme_images/testing/wireframes_login.png)

### **Task List**
<hr>

![Task List](images/readme_images/testing/welcome_task_list.png)

### **Add Task**
<hr>

![Add Task](images/readme_images/testing/wireframes_add_task.png)

### **Project List**
<hr>

![Project List](images/readme_images/testing/wireframes_project_list.png)
<hr>

### **Add Project**

![Add Project](images/readme_images/testing/wireframes_add_project.png)
<hr>

<a name="skeleton"></a>

# **1.3. Skeleton**

### **Diagram**
<hr>

### **Diagram signup-login-logout**
<hr>

![Diagram signup-login-logout](images/readme_images/flow_login_logout.png)

### **Diagram CRUD**
<hr>

![Diagram CRUD](images/readme_images/Flow_CRUD.png)

### **Diagram filter**
<hr>

![Diagram filter](images/readme_images/flow_filter.png)


[Back to Table Of Content](#tableOfContents)

<a name="colorScheme"></a>

# **1.4. Color Scheme**

* Color of body was: rgba(33, 37, 41, 1) the bs-gray-900 bootsrap pallet
* Image colors: mix of rgba(32, 149, 175, 1) rgba(41, 75, 113, 1) and rgba(30, 150, 113, 1)
* Font color: aliceblue


[Back to Table Of Content](#tableOfContents)

<a name="features"></a>


<a name="dataBase"></a>

# **1.5. Database Design**

### **Database structure**
<hr>

![Database Design](images/readme_images/testing/database.png)

### **Security**
<hr>

For security reasons, Database connection details are set up in an env.py. For production, these are stored in Heroku.


[Back to Table Of Content](#tableOfContents)

# **2. Features**

[Back to Table Of Content](#tableOfContents)

<a name="technologies"></a>

* Responsive design
* Navigation Menu (Site Wide)
* Postgress databases to store information and user login/profile information
* CRUD Functionality
* Filter list details functionality
* Filter due date range
* Hiding filter once not in use
* Pagination
* Login functionality
* Logout functionality
* Register functionality


### **Importance and Difficulty table**
<hr>

![Hero image](images/readme_images/importance_difficulty.png)

# **3. Technologies Used**

During creation journey I did use:

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * Chrome dev tool used to debug and test code while building
* [Github](http://github.com)
    * For storing project
* [Gitpod](https://gitpod.io/workspaces)
    * Code written in gitpod workspace
* [W3School](https://www.w3schools.com/)
    * For problem solving and code searching
* [Stack Overflow](https://stackoverflow.com/)
    * For problem solving and code searching
* [PEP8 validator](http://pep8online.com/)
    * For checking python convention
* [Heroku](https://id.heroku.com/login)
    * To deploy project into live environment
* [Cloudinary](https://cloudinary.com/)
    * To store static files
* [Markdown](https://en.wikipedia.org/wiki/Markdown)
    * To create project documentation
* [Python OS](https://getbootstrap.com/)
    * asgiref==3.5.0
    * backports.zoneinfo==0.2.1
    * cloudinary==1.28.1
    * coverage==6.3.1
    * dj-database-url==0.5.0
    * dj3-cloudinary-storage==0.0.6
    * Django==3.2
    * django-allauth==0.48.0
    * django-bootstrap-datepicker-plus==4.0.0
    * django-filter==21.1
    * gunicorn==20.1.0
    * oauthlib==3.2.0
    * psycopg2==2.9.3
    * PyJWT==2.3.0
    * python3-openid==3.2.0
    * pytz==2021.3
    * requests-oauthlib==1.3.1
    * sqlparse==0.4.2
* [Django](https://docs.djangoproject.com/en/4.0/)
    * This project was created using the Django framework, the back-end logic and the means to run/view the Website.
* [Bootstrap](https://docs.python.org/3/library/os.html)
    * To provide styles to page
* [balsamiq Wireframes](https://balsamiq.com/wireframes/)
    * To build wireframes
* [Font Awesome](https://fontawesome.com/)
    * Special Icons for links
* [Google Fonts](https://fonts.google.com/)
    * Google fonts are used in the project to import the Merienda font for the nav title.
* [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README

[Back to Table Of Content](#tableOfContents)

<a name="testing"></a>

# **4. Testing**

<a name="pep"></a>

## **4.1 Validators**

### **PEP8**

Code pass PEP8 without critical errors

### **W3C HTML**

Code pass W3C HTML without errors

### **W3C CSS**

Code pass W3C CSS without errors



[Back to Table Of Content](#tableOfContents)

<a name="manualTesting"></a>

## **4.2 Manual testing**

### **Sign Up test**
<hr>

### **Sign up Page wrong user or password**

![Landing page menu](images/readme_images/testing/signup_wrong_password.png)

### **Sign up Page email exist**

![Login Page email exist](images/readme_images/testing/register_user_mail_exist.png)

### **Sign up Page user exist**

![Sign up Page user exist](images/readme_images/testing/register_user_exist.png)

### **Sign up Page password too short**

![Sign up Page password too short](images/readme_images/testing/register_password_short.png)

[Back to Table Of Content](#tableOfContents)

### **Login test**
<hr>

### **Login Page wrong user or password**

![Login Page wrong user or password](images/readme_images/testing/login_page_wrong_login.png)

![Project List](images/readme_images/testing/project_list.png)

[Back to Table Of Content](#tableOfContents)
### **Project List**
<hr>

### **Add Project**

![Add Project](images/readme_images/testing/add_project.png)

### **Update Project**

![Update Project](images/readme_images/testing/update_project.png)

### **Delete Project**

![Delete Project](images/readme_images/testing/delete_project.png)

[Back to Table Of Content](#tableOfContents)
### **Task List**
<hr>

### **Toggle button**

![Login Page wrong user or password](images/readme_images/testing/toggle_task.png)

### **Edit Task**

![Edit Task](images/readme_images/testing/edit_task.png)

### **Pagination**

![Edit Task](images/readme_images/testing/pagination_page_1.png)

![Edit Task](images/readme_images/testing/pagination_page_2.png)

[Back to Table Of Content](#tableOfContents)
### **Filter Area**
<hr>

### **Done dropdown**

![Edit Task](images/readme_images/testing/filter_dropdown.png)

### **Project Filter**

![Project Filter](images/readme_images/testing/filter_project.png)

### **Date Range Filter**

![Date Range Filter](images/readme_images/testing/filter_date_range.png)

### **Owner Filter**

![Owner Filter](images/readme_images/testing/filter_owner.png)

[Back to Table Of Content](#tableOfContents)
### **Link opener**
<hr>

### **Link Facebook**

![Link Facebook](images/readme_images/testing/link_facebook.png)

### **Link Twitter**

![Link Facebook](images/readme_images/testing/link_twitter.png)

### **Link Youtube**

![Link Facebook](images/readme_images/testing/link_youtube.png)

### **Link LinkedIn**

![Link Facebook](images/readme_images/testing/link_linkedin.png)

### **Link Dribbble**

![Link Facebook](images/readme_images/testing/link_dribbble.png)


[Back to Table Of Content](#tableOfContents)


<a name="functionTest"></a>

## **4.3 Function tests**

Due to time constraints, the fully automatic test wasn't completed

### **Automatic Test**
<hr>

### **First Automatic Test**

![First Automatic Test](images/readme_images/testing/first_test.png)

### **Second Automatic Test**
* Due to time limits additional tests are not implemented 

![Second Automatic Test](images/readme_images/testing/test_automatic.png)


[Back to Table Of Content](#tableOfContents)

<a name="development"></a>



# **5. Development Cycle**


Page was built based on diagrams, user stories, and wireframes. In the first days of this project, I was focused on installing packets and building the connection with a database & Cloudinary. Once I built the connection with the database I did deploy the project to Heroku to avoid potential errors with the deployed version.
 
CRUD functionality over task list was the next phase of this implementation, to ensure the user is capable of manipulating data by adding, updating, deleting, and marking as completed to have full control over the information.
 
Adding Automatic test for CRUD functionality.
 
Adding Calendar picker to due date field to avoid potential issues with typing date in the different way as is expected by form, as well as improve UX by delivering visual ability to locate the chosen date on the calendar itself.
 
As per the Agile approach, the next feature appearing during the next iteration cycle was an issue with building a separate way to store Projects in the form of the list. This enabled users to have the ability to standardize project naming conventions and keep control over the data and future task creation.
 
To ensure the project data has CRUD functionality, I decided to build it in the class view model, which gave me an opportunity to learn this approach in a real situation.
 
The filter option was implemented to reduce displayed data and to give a better end user experience. To avoid an overwhelming number of displayed data the pagination was implemented.
 
Final bug fix run, where issues like registration error, query set conflicts were addressed.
 
The last stage of the process was styling the page in CSS and creating a ReadMe file.


[Back to Table Of Content](#tableOfContents)

<a name="deployment"></a>

# **6. Deployment**

### **Development Environment**
<hr>

1. Create requirements.txt pip3 freeze --local > requirements.txt
2. Create Procfile.
3. Commit and push changes to Github.
4. Move to the Heroku part of a deployment.

### **To deploy my final project to the cloud I used Heroku. To do this I had to**
<hr>

1. Push the latest code to GitHub.
2. Go to Heroku
3. Select new in the top right corner.
4. Create a new app.
5. Enter the app name and select Europe as the region.
6. Connect to GitHub.
7. Search for repo-name.
8. Select connect to the relevant repo you want to deploy.
9. Select the settings tab.
10. Add buildpack
11. Select Python, then save changes.
12. Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
13. Navigate to the deploy tab
14. Scroll down to Manual Deploy and select deploy branch.

### **Heroku Postgres Database**
<hr>

1. Go to the Resources tab in Heroku.
2. Select Heroku Postgres from the Add-ons search bar
3. Choose the Hobby Dev-Free plan.
4. Click submit the order form.
5. Go back to Gitpod bash terminal and install
    * pip3 install dj_databse_url
    * pip3 install psycopg2-binary 
6. Seve in the requirements file by: 
    * pip3 freeze > requirements.txt



[Deployed version](TBA)

[Back to Table Of Content](#tableOfContents)

<a name="endProduct"></a>

# **7. End Product**

## **End Product screens**
<hr>

### **Landing Page**
<hr>

![Landing page](images/readme_images/testing/welcome_page.png)

### **Sign up page**
<hr>

![Sign up page](images/readme_images/testing/signup.png)

### **Login Page**
<hr>

![Login Page](images/readme_images/testing/login_page.png)


### **User not authenticated Page Menu**
<hr>

![User not authenticated Page Menu](images/readme_images/testing/landing_page_menu.png)

### **User authenticated Home Page Menu**
<hr>

![User authenticated Home Page Menu](images/readme_images/testing/home_page_menu.png)


### **Project List**
<hr>

![Project List](images/readme_images/testing/project_list.png)

### **Add Project**
<hr>

![Add Project](images/readme_images/testing/add_project.png)

### **Update Project**
<hr>

![Update Project](images/readme_images/testing/update_project.png)

### **Delete Project**
<hr>

![Delete Project](images/readme_images/testing/delete_project.png)

### **Home Page**
<hr>

![Home Page](images/readme_images/testing/home_page.png)

### **Edit Task**
<hr>

![Edit Task](images/readme_images/testing/edit_task.png)

### **Sign out**
<hr>

![Sign out](images/readme_images/testing/sign_out.png)



[See testing photos](#functionTest) for more end product photo.


[Back to Table Of Content](#tableOfContents)

<a name="knownBugs"></a>

# **8. Known bugs**

<a name="fixedBugs"></a>

## **8.1 Fixed bugs**
<hr>


During development I did face multiple bugs:

### **301 Redirect Error**
<hr>

Error

![301 redirect Error](images/readme_images/bugs/E1_301redirect_Error.png)

Fix 

![301 redirect Error](images/readme_images/bugs/E1_solution_True.png)

   
### **Issue with page rendering**
<hr>
    * Page wasn't rendering due to lack of implementing url by using jinja template

Fix

![301 redirect Error](images/readme_images/bugs/E3_jinja_url.png)

* Extending base.html template to allauth html files
    * Issue with a file structure and which was not able to pull details from base.html

Fix

Moved the base.html to the main templates folder

![301 redirect Error](images/readme_images/bugs/E4_location.png)

Updated the other templates accordingly

![301 redirect Error](images/readme_images/bugs/E4_template.png)

### **Templates DIR typo**
<hr>

* Typed DRI instead of DIR

Fix

![301 redirect Error](images/readme_images/bugs/E5_DIR_typo.png)

* Display CSS setting in the Heroku deployed version (Alan, John)
<hr>

* Issue related with not using a correct folders structure, link to the static files was incorrectly written

* Link to style sheet should be in the < head >

Fix

![301 redirect Error](images/readme_images/bugs/E6_link_to_css.png)

### **Setting.py, setting debug to:**
<hr>

SECURITY WARNING: don't run with debug turned on in production!

DEBUG = "DEVELOPMENT" in os.environ

* env.py set os.environ["DEVELOPMENT"] = "True"

* import to urls.py 

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path(......
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


### **Conflict between filter and paginations**
<hr>

* Caused by using the same query set – fixed by separating queries

Fix

![301 redirect Error](images/readme_images/bugs/E7_queryset.png)


<a name="remainBugs"></a>
   
## **8.2 Remaining Bugs**
<hr>

### **Delay with updating project list, waiting time approx. 5 min - the solution was discovered a few hours before the project deadline, however, due to complexity and potential impact to the overall project deadline, the decision was made to do not introduce the fix.**


[Back to Table Of Content](#tableOfContents)

<a name="credits"></a>

# **9. Credits**

* Heroku deployment instructions from Code Institute
* Hello Django and Django blog from code institute
* [Django Blog by Codemy](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy)
* Stack overflow to support debugging
* CI Tutor Support for Help with
   * Issue with page rendering (Ger)
   * Extending base.html template to allauth html files
   * Display CSS setting in the Heroku deployed version (Alan, John)
* GitHub Python Template [Code Institute](https://codeinstitute.net/)
* [Bootstrap documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
* [Django documentation](https://docs.djangoproject.com/en/4.0/)
* Conflict Between pagination and filter deep understanding [Filtering and Pagination with Django](https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/)

* Coding Buddy @Matt_5P for mental support and help with issues during the process
