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
                python -m pip install --upgrade pip
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
            echo 'Pipeline succeeded!'
            emailext(
                subject: "SUCCESS: Flask Jenkins Pipeline",
                body: "Build succeeded: ${env.BUILD_URL}",
                to: "snehamgupta0123@gmail.com"
            )
        }
        failure {
            echo 'Pipeline failed!'
            emailext(
                subject: "FAILED: Flask Jenkins Pipeline",
                body: "Build failed: ${env.BUILD_URL}",
                to: "snehamgupta0123@gmail.com"
            )
        }
    }
}
