# Daily Meal & Ingredients Planner

This is a short Python program that will give you a list of ingredients to go & buy (or check you already have) based on your meal choices.

It will take approx. 5 mins

I have built a programme which allows the user to choice 1 of 3 meals which gives the user choice on which meal to prepare themselves based on whether they have the ingredients or not. 

This is a Python Programme run on the Code Institute Mock Terminal. 

Deployed Heroku Site for my Project
https://stephanie-python-project-b041af7a44a3.herokuapp.com/

# User Experience
## As a user

I want to easily navigate my way through the programme to select my meal.
Follow a chronological order that makes sense.
Tell me exactly what keys to enter and if I make a mistake, tell me what I done wrong
Have simple instruction to follow
Give me options to re-start my choice I selected anything wrong
I want to know exactly how long it will take for my order to be made

# Flow Chart
## Lucid Chart
I used a basic Lucid Flow chart initially to help me decide on the flow & outcomes of the user process
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/e5a708ce-e448-4412-bb4f-865a807bd5f0)

# Features
## Opening Page
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/e797e674-4569-4c5d-9889-93856b934e95)
## Meal Choice
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/98e3572a-82b9-46cf-85e8-cbc4932d2c11)
## Meal Confirmation with ingredients
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/87d96713-63ea-496e-bbde-562f5bbc1128)
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/8f0b5f0f-b452-4b43-ac74-81abe60c47b1)
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/05ba6d59-91c1-49f9-b7ef-b7bf82991b35)
## Future Features
Provide User with corresponding cooking instructions based on their meal choice.

# Technology Used 
Python to write my programme
JavaScript provided in the Code Institute template
CSS provided in the Code Institute template
HTML provided in the Code Institute template
Heroku to deploy the project

# Testing & Bugs
I have manually tested this sproject by doing the following:

Passed the code through a PEP8 linter (Python Tutor)
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/ac21ea23-0981-4588-a3c1-596a3735eb3a)

Given invalid inputs to all input choices and made sure they allow the user to carry on with their order
Tested in my local terminal and the Code Institute Heroku terminal
## Fixed Bugs
Correcting Syntax and ensuring PEP8 compliant indentation

# Unfixed Bugs
## Issue with exception error for meal choices
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/47b74d04-7ef0-4c9d-8803-c280488b964e)
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/0db6a6e1-4de0-4015-bda9-0d3e76a630c0)
![image](https://github.com/stephanielenehan/Stephanie-Python-Project/assets/35435182/b54f35b8-858c-47f7-8444-826b1387787f)

# Deployment
## This project was developed through Gitpod, using Code Institue's mock terminal for Heroku
Deploy from GitHub
Log into your GitHub repository
Click 'Settings' in the main Repository menu
Click 'Pages' from the left-hand side navigation menu
Within the Source section, click the "Branch" button and change from 'None' to 'Main'
The page should automatically refresh with a url displayed
Test the link by clicking on the url

## Forking
Navigate to the repo pizzas
Click the 'Fork' button on the upper right part of the page.
You will now have a fork of my repository added to your GitHub profile.

## Cloning
Login to Github and go to my repo
Above the list of files click the green ‘code’ button.
This will bring up a few options as to how you would like to clone. You can 4. select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
Open git bash
Type ‘git clone’ and then paste the URL you copied. Press Enter.

## Set up API
Credit to Jorgen Brattang for the description

Head to Google cloud platform and sign in or create a free google account
From the google cloud platform dashboard click 'Select a new project'. Then select 'New project'.
Create a name for your project under 'Project name' then click 'Create'.
This should bring up a box with your project in. Underneath click 'SELECT PROJECT'.
From the sidebar navigate to 'APIs and services', 'Library'.
In the search bar search for google drive.
Select 'Google drive API' and click 'ENABLE'.
Click the 'CREATE CREDENTIALS' button located to the top right of the page.
From the dropdown menu under 'Which API are you using?' select 'Google drive API'.
Under 'What data will you be accessing' choose 'Application data'.
Under 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine or Cloud Functions?' select 'No, i'm not using them' and click 'NEXT'.
Enter a Service Account Name. You can name it whatever you like. I would suggest naming it the same as what you named your project. Then click 'CREATE AND CONTINUE'.
In the 'Role' dropdown menu select 'Basic', 'Editor', then click 'Continue'.
The next page can be left blank so just click 'DONE'.
Under 'Service Accounts' find the account you just created and click it.
Navigate to the 'KEYS' tab and click 'ADD KEY', 'Create new key'. Select 'JSON' and click 'CREATE'.
This will download a json file to your machine. This normally downloads into your 'downloads' folder but if you're unsure you can right click the file once it's downloaded and click 'show in folder' to locate it.
Next we will have to link the Google Sheets API. To do this navigate back to the library by clicking on the burger icon in the top left hand corner and selecting 'APIs and services', 'Library' from the dropdown menu.
In the search bar search for 'Google Sheets' and select 'Google Sheets API' and click 'ENABLE'.
Now, using a programme like Gitpod open or create a repository.
Drag and drop the json file that you downloaded earlier into your workspace. Rename this file to 'creds.json'.
Open the file and copy the email address under 'client_email' without the quotation marks.
Open up the google sheet you want to use and click the 'Share' button.
Paste in the client email. Make sure 'Editor' is selected, untick 'Notify people' and then click 'Share'.
To protect sensitive information be sure to add your creds.json file to your .gitignore file inside your editor.
In order to use our google sheets API you need to install two additional dependencies into your project.
Copy the following code on the first two lines of your workspace
gspread

Below this, add the following code:
scope

## Set up Heroku
Credit to Jorgen Brattang for the description

The requirements.txt file in the IDE must be updated to package all dependencies. To do this:

Enter the following into the terminal: 'pip3 freeze > requirements.txt'
Commit the changes and push to GitHub
Go to Heroku.com and sign in or create a free account.

From the heroku dashboard click the 'Create new app' button.

Name the app something unique and choose what region you are in then click 'Create app'.

Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.

In the field for KEY enter the value CREDS in all capitals.

In the field for VALUE copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.

In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.

Scroll down to the Buildpacks section and click 'Add buildpack'.

Click Python then save changes.

Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.

Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.

Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.

From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.

Enter the repository name as it is in GitHub and click 'search'.

Click the 'connect' button next to the repository to link it to heroku.

To deploy, scroll down and click the 'Deploy Branch' button.

Heroku will notify you that the app was successfully deployed with a button to view the app.

If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.

# Credits 
 - My own custom code based on CI Love Sandwiches Walkthrough
 - Basic structure inspired by https://fredboys-fredspizza-4omysm4rw12.ws-eu110.gitpod.io/
 - README.md content on forking & Cloning https://fredboys-fredspizza-4omysm4rw12.ws-eu110.gitpod.io/


# General Dev issue and how I resolved / dealt with: 
E.G. Workspace became unavailable due to issue outside my control.
 - Is there something I can do to resolve the actual issue for myself? - No. 

 - Is there a work around I can pull together to resolve (even temporarily) the issue for myself? - Yes
    - By using the CI Students workspace on Gitpod as opposed to my own Gitpod hours by default I left myself with the full 50 hrs of my own Gitpod free allocation. Downside I had to reinstall my creds.json and dependencies like gspread and google-auth but it worked. 
 
 - If there was no feasible timely workaround until the workspace access issue was reolved, 
    is there anything else I can access and work on? -Yes
     - The Readme.md file of your Repo can be accessed and edited right on the Github website. (Credit to a previous mentor Malia Havlicek who showed me that trick)


