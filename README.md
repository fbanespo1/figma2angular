#Figma to Angular Code Generator

This app allows generating Angular component code from a Figma design file. It uses the Figma API to extract components and OpenAI's GPT-3 to generate TypeScript code for those components.

How it Works
The app follows these steps:

User uploads a Figma file (must have access permission)

The Figma API is called to analyze the file:

The images, fonts, colors and component names are extracted
This structured data is used to understand the design system
The component data is passed to OpenAI's Davinci-002 model to generate Angular code

A prompt is constructed describing each component
Code is generated to recreate the UI with Angular directives
The generated Angular code is displayed in the app

Syntax highlighted code rendered with Streamlit
Download button to save as a .ts file
(Optional) User can integrate into an Angular project

Ng CLI commands can scaffold a new project
Generated component added to app module
Provides a full working Angular app
This automated pipeline saves hours of manually converting designs to Angular code!

Interface
The app provides a simple interface built with Streamlit:

File uploader to select a Figma file
Output area showing generated Angular code
Buttons to download code and create project
Sliders to tweak OpenAI parameters
Streamlit's simplicity and speed allowed quick iterating and changes.

Running Locally
To run the app locally:

Clone the repository
Install requirements: pip install -r requirements.txt
Sign up for Figma and OpenAI APIs to get keys
Add keys to config.py
Run: streamlit run app.py
This will start the web app on localhost.

Deployment
For deployment I recommend:

Building a Docker container for the app
Hosting on a service like AWS Elastic Beanstalk
Using nginx + gunicorn for productionization
This allows deploying easily without managing servers directly.

Future Ideas
Some potential ways to expand the app:

Add more options for code generation: React, Vue, mobile, etc
Incorporate React Storybook for interactive component preview
Perform validation on generated code before download
Version control integration to commit generated code
Let us know if you have any other ideas for features!

Contributors
This app was created by:
Tony

We welcome contributions and feedback!

![Screenshot 2023-07-24 at 8 52 51 PM](https://github.com/fbanespo1/figma2angular/assets/35040191/57205879-001f-42c5-84ff-21d8a970f50f)


![Screenshot 2023-07-24 at 8 52 51 PM](https://github.com/fbanespo1/figma2angular/assets/35040191/57205879-001f-42c5-84ff-21d8a970f50f)
