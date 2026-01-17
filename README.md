# Flask Application Deployment

This is a simple Flask application designed to be deployed via a Jenkins CI/CD pipeline.

## Features
- Simple Flask web application
- Displays a success message: "This simple flask application deployed by jenkins CICD pipeline."
- Responsive UI with styled HTML
- Docker support for containerized deployment
- Jenkins pipeline configuration for automated CI/CD

## Running Locally

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Docker Deployment

Build the Docker image:
```bash
docker build -t flask-app .
```

Run the container:
```bash
docker run -p 5000:5000 flask-app
```

## Jenkins CI/CD Pipeline

The `Jenkinsfile` contains the pipeline configuration with the following stages:

1. **Checkout**: Clones the repository
2. **Install Dependencies**: Installs Python packages from requirements.txt
3. **Test**: Runs pytest (if tests exist)
4. **Deploy**: Launches the Flask application

## Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Jenkinsfile         # Jenkins pipeline configuration
├── Dockerfile          # Docker container configuration
└── README.md           # This file
```
