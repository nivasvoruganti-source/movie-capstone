pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 10'
                 sh 'curl http://movie-capstone-backend:5000/health'
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}
