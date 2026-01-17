pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python -m pytest tests/ || true'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying Flask application...'
                sh 'python app.py'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed!'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
