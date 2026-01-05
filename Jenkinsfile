pipeline {
    agent any

    stages {
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

        stage('Wait for Backend') {
            steps {
                sh 'sleep 15'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5000/health'
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}


