pipeline {
    agent any

    environment {
        APP_NAME = "todo-app"
        DOCKER_IMAGE = "todo-app-image"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building application...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running application tests...'
                sh 'docker run --rm $DOCKER_IMAGE npm test' // Replace 'npm test' with your test command
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Running code quality checks...'
                sh 'docker run --rm $DOCKER_IMAGE npm run lint' // Replace with your linting/formatting command
            }
        }

        stage('Package Application') {
            steps {
                echo 'Packaging application...'
                sh 'docker save -o $APP_NAME.tar $DOCKER_IMAGE'
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                echo 'Deploying application to test environment...'
                sh 'docker load < $APP_NAME.tar'
                sh 'docker run -d --name $APP_NAME -p 8080:8080 $DOCKER_IMAGE'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker containers and images...'
            sh 'docker rm -f $APP_NAME || true'
            sh 'docker rmi $DOCKER_IMAGE || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
