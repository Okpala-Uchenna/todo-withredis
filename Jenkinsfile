pipeline {
    agent any

    environment {
        DOCKER_COMPOSE = '/usr/local/bin/docker-compose'  // Update the path if necessary
        GITHUB_CREDS = 'f619b8b7-c394-412a-af83-2acc73e6b05d' // Jenkins credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull your code from the repository using Git credentials
                git branch: 'master', // Changed from 'main' to 'master'
                    credentialsId: "${env.GITHUB_CREDS}",
                    url: 'https://github.com/Okpala-Uchenna/todo-withredis.git'
            }
        }

        stage('Build and Deploy with Docker Compose') {
            steps {
                script {
                    // Ensure Docker is available
                    sh 'docker --version'
                    sh 'docker-compose --version'
                    
                    // Run docker-compose up with the build flag
                    sh """
                        docker-compose -f docker-compose.yml up --build -d
                    """
                }
            }
        }

        stage('Post-Build Cleanup') {
            steps {
                // Optionally, you can run tests, stop containers, or clean up
                sh 'docker-compose down'
            }
        }
    }

    post {
        success {
            echo "Docker Compose build and deployment succeeded!"
        }
        failure {
            echo "There was an issue with the build or deployment."
        }
        always {
            // Ensure containers are down even if the pipeline fails
            sh 'docker-compose down'
        }
    }
}
