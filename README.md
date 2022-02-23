![Hero image](images_readme/hero_image.PNG)
# ✔️ Project Management System 📔

## [See Live web](https://project-task.herokuapp.com/)

# Introduction

Welcome to my Fourth Full Stack Course project. This is a Project Management System.

The inspiration for this project was my side learning process of becoming a certified SCRUM master, as well as observation of project managers from my company using multiple trackers, which seemed impractical. As a SCRUM Master, one of the most needed items is to have an tool to collect and monitor workload, progress and deadlines. The tool itself can be used in any project management world. In current world, where Covid changed the way of doing the business and most of the things are done online, having a simple yet sufficient tool to track the progress of your team, project memebers and other function is essential to bring efficiency to the company. 

The goal was to create a tool, which in the future can be adjusted according to the specific customer needs. 


<a name="tableOfContents"></a>

# Table of Contents

[**1. UX**](#ux)
* [**1.1. Strategy**](#strategy)
    * [**1.1.1 Project Goals**](#projectGoals)
    * [**1.1.2 User Stories**](#userStories)

* [**1.2. Structure**](#structure)
* [**1.3. Skeleton**](#skeleton)
* [**1.4. Color Scheme**](#colorScheme)

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

As a next step on my path of becoming a software developer from zero to hero 😊, I'm presenting a Project Manager Tool. As mentioned in my last projects my ultimate goal is to change my career path and become a full-time developer. Here I will be showing my new acquired skill, which is Django and DataBase. As part of my portfolio collection, which can be shown to my potential future employers, and potentially be used by myself. I have decided to build a product that can support day to day workload of Project Managers or SCRUM masters. The product is simple to use and intuitive, the navigation around the page is clear and gives user ability to search and filter through things like date or status. Product can be adjusted in the future for specific customer needs, as well as certain features can be added if business needs it. The current tool includes elements as project name, task, due date and owner. Tool can hold multiple projects, meaning project manager or SCRUM master can have an overview of all actions open against each project they are working on. By having all in one space, this optimizes time and effort for tasks management.  


[Back to Table Of Content](#tableOfContents)

<a name="strategy"></a>

# **1.1 Strategy**

<a name="projectGoals"></a>

##  **1.1.1 Project Goals**

A project goal was to create a set PM tool belt were project tasks can be monitored, this page have a potential to build more tools in upcoming project #5, where additional features like Gantt Chart, Critical Path, Delay Calculator, and Task Time Calculator will be added. Currently tool has abilities to store tasks against multiple projects, owners and due dates. User can select either a specific project, or choose the owner of the task.

The reason for this web page is to create tool which I can use as a potential PM SCRUM master in the future also to create product which can be a sellable. Therefore, in my thought process, I aimed to create a good basis in project #4 and expand on that in my next project #5. 


<a name="userStories"></a>

## **1.1.2 User Stories **

![User Stories](images/readme_images/user_stories.png)

# **1.2. Structure**



<a name="skeleton"></a>

# **1.3. Skeleton**

diagram below:

![flow](images/readme_images/pms_flow.png)

[Back to Table Of Content](#tableOfContents)

<a name="colorScheme"></a>

# **1.4. Color Scheme**


[Back to Table Of Content](#tableOfContents)

<a name="features"></a>

# **2. Features**

[Back to Table Of Content](#tableOfContents)

<a name="technologies"></a>

•	Responsive design
•	Navigation Menu (Site Wide)
•	Postgress databases to store information and user login/profile information
•	CRUD Functionality
•	Filter list details functionality
•	Filter due date range
•	Hiding filter once not in use
•	Login functionality
•	Logout functionality
•	Register functionality


Importance and Difficulty table:

![Hero image](images/readme_images/importance_difficulty.png)

# **3. Technologies Used**

During creation journey I did use:

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * Chrome dev tool used to debug and test code while building
* [Github](http://github.com)
    * For storing project code written in gitpod
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
    * To style the site a framework addition to CSS3
* [Bootstrap](https://docs.python.org/3/library/os.html)
    * Used for os.environ


[Back to Table Of Content](#tableOfContents)

<a name="testing"></a>

# **4. Testing**

<a name="pep"></a>

## **4.1 PEP8**


[Back to Table Of Content](#tableOfContents)

<a name="manualTesting"></a>

## **4.2 Manual testing**



[Back to Table Of Content](#tableOfContents)

<a name="functionTest"></a>

## **4.3 Function tests**


<a name="development"></a>

# **5. Development Cycle**


Page was building based on diagram and user stories. The first days of this project I was focused with installing packets and building the connection with a database & cloudinary. Once build the connection with database I did deploy project to Heroku to avoid potential error with deployed version.

CRUD functionality over task list was a next phase of this implementations, to ensure user is capable to manipulate data by adding, updating, deleting and marking as completed to have a full control over a data.

Adding Calendar picker to due date field to avoid potential issues with typing date in the different way as is expected by form as well as improve UX by delivering visual ability to locate chosen date on the calendar it self.

As per Agile approach the next features appear during next iteration cycle where an issue with building a separate way to store Projects in form of the list to have ability to standardize projects naming convention and keep control over a data and future task creation.
Tu ensure the project data is also coming under a CRUD functionality I decided to build it in the class view model, which give me an opportunity to learn this approach in real situation.

Filter option was implemented to reduce a displayed data and to give a better end user experience.
To avoid overwhelming number of displayed data the pagination was implemented.



[Back to Table Of Content](#tableOfContents)

<a name="deployment"></a>

# **6. Deployment**

To deploy my final project to the cloud I used Heroku. To do this I had to:

1. Push the latest code to GitHub.
2. Go to Heroku
3. Select new in the top right corner.
4. Create new app.
5. Enter the app name and select Europe as the region.
6. Connect to GitHub.
7. Search for repo-name.
8. Select connect to the relevant repo you want to deploy.
9. Select the settings tab.
10. Add buildpack
11. Select Python, then save changes.
12. Select Nodejs, then save changes.
13. Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
14. Navigate to the deploy tab
15. Scroll down to Manual Deploy and select deploy branch.

[Deployed version](TBA)

[Back to Table Of Content](#tableOfContents)

<a name="endProduct"></a>

# **7. End Product**

## **End Product screens**

![Hero image]()

[See testing photos](#functionTest) for more end product photo.

[Back to Table Of Content](#tableOfContents)

<a name="knownBugs"></a>

# **8. Known bugs**

<a name="fixedBugs"></a>

## **8.1 Fixed bugs**


During development I did face multiple bugs: 

* 301 Redirect Error

Error

![301 redirect Error](images/readme_images/E1_301redirect_Error.png)

Fix 

![301 redirect Error](images/readme_images/E1_solution_True.png)

   
* Issue with page rendering (Ger)
    * Page wasent rendering due to lack of implementing url by using jinja template

Fix

![301 redirect Error](images/readme_images/E1_solution_True.png)

* Extending base.html template to allauth html files
    * Issue with a file structure and which was not able to pull details from base.html

Fix

Moved the base.html to a main templates folder

![301 redirect Error](images/readme_images/E4_location.png)

Updated the other templates accordingly

![301 redirect Error](images/readme_images/E4_template.png)

* Templates DIR typo
    * used DRI insted of DIR

![301 redirect Error](images/readme_images/E5_DIR_typo.png)


* Display CSS setting in the Heroku deployed version (Alan, John)
    * Issue related with not using a correct folders structure, link to the static files was incorectly writen

* Link to style sheet shoul be in the < head >

![301 redirect Error](images/readme_images/E6_link_to_css.png)

* Setting.py, setting debug to:

SECURITY WARNING: don't run with debug turned on in production!

DEBUG = "DEVELOPMENT" in os.environ

* env.py set os.environ["DEVELOPMENT"] = "True"

* import to urls.py 

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path(......
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


<a name="remainBugs"></a>
   
No remainig bugs

## **8.2 Remaining Bugs**

No bugs remaining

All known bugs were corrected before deployment

[Back to Table Of Content](#tableOfContents)

<a name="credits"></a>

# **9. Credits**

* Heroku deployment instructions from Code Institute
* Hello Django and Djngo blog from code institute
* Django Blog by Codemy
* Stack overflow to support with debugig
* CI Tutor Support for Help with
   * Issue with page rendering (Ger)
   * Extending base.html template to allauth html files
   * Display CSS setting in the Heroku deployed version (Alan, John)
* GitHub Python Template [Code Institute](https://codeinstitute.net/)
