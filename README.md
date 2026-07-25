TITLE: Fresh Fruite Store

DESCRIPTION: Fresh Fruit Store is a basic web application showcasing a list of fruits along with their prices per unit. The project was developed to understand fundamentals of web deployment , AWS EC2, Nginx, Flask, Git, and GitHub Actions by implementing a complete CI/CD deployment pipeline.

FEATURES: -Displays a list of fruits with prices.
          -Fetches fruit data from a Flask REST API.
          -Responsive frontend built with HTML, CSS and JavaScript.
          -Reverse proxy configured using Nginx.
          -Hosted on AWS EC2.
          -Automatic deployment using GitHub Actions.
          -Secure deployment using GitHub Secrets

TECH STACK:
          Frontend:
                    -HTML5
                    -CSS3
                    -JavaScript
          Backend:
                    -Python 3.12.3
                    -Flask 3.1.3
                    -Flask CORS 6.0.5
          Cloud & Operating System:
                    -Amazon Web Services (AWS) EC2
                    -Ubuntu Server 24.04.4 LTS (Noble)
          Web Server:
                    -Nginx 1.24.0
          Version Control:
                    -Git 2.43.0
                    -GitHub
          CI/CD:
                    -GitHub Actions
          Service Management:
                    -systemd

FOLDER STRUCTURE:
          fruit-app/
          ├── .github/
          │   └── workflows/
          │       └── build.yml          # GitHub Actions CI/CD workflow
          ├── backend/
          │   ├── app.py                 # Flask backend API
          │   └── requirements.txt       # All Python dependencies
          ├── frontend/
          │   └── index.html             # Frontend webpage
          ├── .gitignore
          └── README.md

HOW TO RUN LOCALLY:


CI/CD PIPELINE:
          
