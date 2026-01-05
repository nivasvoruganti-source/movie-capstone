pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nivasvoruganti-source/movie-capstone.git'
            }
        }

        stage('Build Docker Images') {
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
                sh '''
                echo "Waiting for backend to start..."
                sleep 10
                curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
        success {
            echo '✅ Movie Capstone Pipeline SUCCESS'
        }
        failure {
            echo '❌ Movie Capstone Pipeline FAILED'
        }
    }
}

