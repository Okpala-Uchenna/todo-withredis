pipeline {
    agent any

    environment {
        // Define any environment variables, if needed
        DOCKER_COMPOSE = '/usr/local/bin/docker-compose'  // Update the path if necessary
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull your code from the repository
                checkout scm
            }
        }

        stage('Build and Deploy with Docker Compose') {
            steps {
                script {
                    // Ensure Docker is available (this may be redundant if running on Docker nodes)
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
