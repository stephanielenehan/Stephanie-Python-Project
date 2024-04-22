![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!


Deployed Heroku Site for my Project
https://stephanie-python-project-b041af7a44a3.herokuapp.com/


Note to self: General Dev issue and how I reolved / dealt with: 
E.G. Workspace became unavailable due to issue outside my control.
 - Is there something I can do to resolve the actual issue for myself? - No. 

 - Is there a work around I can pull together to resolve (even temporarily) the issue for myself? - Yes
    - By using the CI Students workspace on Gitpod as opposed to my own Gitpod hours by default I left myself with the full 50 hrs of my own Gitpod free allocation. Downside I had to reinstall my creds.json and dependencies like gspread and google-auth but it worked. 
 
 - If there was no feasible timely workaround until the workspace access issue was reolved, 
    is there anything else I can access and work on? -Yes
     - The Readme.md file of your Repo can be accessed and edited right on the Github website. (Credit to a previous mentor Malia Havlicek who showed me that trick)


