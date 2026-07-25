# Fresh Fruit Store

## DESCRIPTION

Fresh Fruit Store is a basic web application showcasing a list of fruits along with their prices per unit. The project was developed to understand the fundamentals of web deployment, AWS EC2, Nginx, Flask, Git, and GitHub Actions by implementing a complete CI/CD deployment pipeline.

## FEATURES

- Displays a list of fruits with prices.
- Fetches fruit data from a Flask REST API.
- Responsive frontend built with HTML, CSS and JavaScript.
- Reverse proxy configured using Nginx.
- Hosted on AWS EC2.
- Automatic deployment using GitHub Actions.
- Secure SSH based deployment using GitHub Secrets.

## TECH STACK

### Frontend:
- HTML5
- CSS3
- JavaScript

### Backend:
- Python 3.12.3
- Flask 3.1.3
- Flask-CORS 6.0.5

### Cloud & Operating System:
- Amazon Web Services (AWS) EC2
- Ubuntu Server 24.04.4 LTS (Noble)

### Web Server:
- Nginx 1.24.0

### Version Control:
- Git 2.43.0
- GitHub

### CI/CD:
- GitHub Actions

### Service Management:
- systemd

## PROJECT ARCHITECTURE

```text
          Browser
             |
             ▼
          Nginx (Port 80)
             |
             ▼
          Flask REST API (Port 8000)
             |
             ▼
          Fruit Data
```

## FOLDER STRUCTURE

```text
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
```

## LIVE DEPLOYMENT

The application is deployed on an AWS EC2 instance using Nginx as a reverse proxy and Flask as the backend server.

The application is accessible through the public IPv4 address of the running EC2 instance.

## CI/CD PIPELINE

The project uses GitHub Actions to implement a CI/CD pipeline that automatically builds and deploys the application whenever code is pushed to the main branch. The build stage verifies the application, and the deploy stage updates the application running on AWS EC2.

```text
Code Change
          │
          ▼
git push to main
          │
          ▼
GitHub Actions Workflow Starts
          │
          ▼
──────────── BUILD JOB ────────────
          │
          ├── Checkout Repository
          │
          ├── Set Up Python 3.12
          │
          ├── Install Dependencies
          │
          └── Build Check
                  │
                  ▼
           If successful
                  │
                  ▼
─────────── DEPLOY JOB ───────────
                  │
                  ├── Connect to EC2 using SSH
                  │
                  ├── Navigate to project folder
                  │
                  ├── Pull latest code
                  │
                  ├── Restart Flask service
                  │
                  └── Reload Nginx
                          │
                          ▼
                Updated website is live
```

## Author

**Avni Gupta**
