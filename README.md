# Jenkins CI/CD Pipeline for Flask Application

## Assignment Title
**Implementation of CI/CD Pipeline for a Python Flask Application using Jenkins**

---

## Objective
The objective of this assignment is to design and implement a **CI/CD pipeline** using **Jenkins** that automates:
- Building a Flask application
- Running automated unit tests
- Deploying the application to a staging environment

The pipeline must trigger automatically on code changes and provide build status notifications.

---

## Prerequisites
Before starting this assignment, the following are required:

- Linux-based system / EC2 instance
- Python 3 installed
- Jenkins installed and running
- GitHub account
- Basic knowledge of Git, Python, and Jenkins

---

## Tools & Technologies Used
- **Python 3**
- **Flask**
- **Pytest**
- **Jenkins (Declarative Pipeline)**
- **Git & GitHub**
- **GitHub Webhooks**
- **Linux / EC2**

---

## Step 1: Create Flask Application

### app.py
A simple Flask application was created that displays a confirmation page when accessed.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Application Successfully Deployed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

---

## Step 2: Define Application Dependencies

### requirements.txt
```text
Flask==2.3.2
Werkzeug==2.3.6
pytest==7.4.4
```

---

## Step 3: Create Unit Tests

### tests/test_app.py
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
```

This ensures that the application is tested before deployment.

---

## Step 4: Create Jenkins Pipeline

### Jenkinsfile
A declarative Jenkins pipeline was created with Build, Test, and Deploy stages.

```groovy
pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/S-neha-01/Flask_App.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f "python app.py" || true
                . $VENV/bin/activate
                nohup python app.py &
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
```

---

## Step 5: Configure Jenkins Job

- Created a **Pipeline** job in Jenkins
- Selected **Pipeline script**
- Enabled **GitHub hook trigger for GITScm polling**

---

## Step 6: Configure GitHub Webhook

- Payload URL:
```
http://<EC2-PUBLIC-IP>:8080/github-webhook/
```
- Content type: `application/json`
- Trigger event: Push

This enables automatic pipeline execution on every push.

---

## Step 7: Pipeline Execution Flow

1. Code pushed to GitHub
2. GitHub webhook triggers Jenkins
3. Jenkins checks out code
4. Dependencies installed
5. Unit tests executed
6. Application deployed if tests pass

---

## Screenshots (Evidence)

### Jenkins Pipeline – Successful Build
![Pipeline Success](Screenshot_2026-01-18_12.07.54_AM.png)

### Jenkins Commit Detection
![Pipeline Changes](Screenshot_2026-01-17_10.34.05_PM.png)

### Deployed Flask Application
![Flask Deployment](Screenshot_2026-01-18_12.08.10_AM.png)

### GitHub Webhook Configuration
![GitHub Webhook](Screenshot_2026-01-18_12.15.38_AM.png)

### Jenkins Trigger Configuration
![Jenkins Trigger](Screenshot_2026-01-18_12.11.35_AM.png)

---

## Final Outcome
- Jenkins CI/CD pipeline successfully implemented
- Automated testing enforced
- Application deployed automatically
- Webhook-based automation achieved
- Assignment requirements fulfilled

---

## Conclusion
This assignment demonstrates the practical implementation of CI/CD using Jenkins for a Flask application, following DevOps best practices such as automation, testing, and continuous deployment.

---

## Author
Sneha
