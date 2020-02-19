pipeline {
    agent any
    environment {
        REGISTRY = "vamsiammineni/myflaskapp"
        REGISTRYCREDS = 'dockerhub'
    }
    stages {
        stage('Unit Tests'){
            steps {
                script {
                   sh 'pip3 install -r requirements.txt'
                   sh 'python3  test.py'
                }
            }
        }
        stage('Build Docker Image') {
            steps{
                echo 'Starting to build docker image'
                script {
                    dockerImage_current_version = docker.build("${REGISTRY}:${env.BUILD_ID}")
                    dockerImage_latest_version = docker.build("${REGISTRY}:latest")
                }
            }
        }
        stage('Deploy Image') {
            steps {
                script {
                    docker.withRegistry('', REGISTRYCREDS){
                        dockerImage_current_version.push()
                        dockerImage_latest_version.push()
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $REGISTRY:${env.BUILD_ID}"
                sh "docker rmi $REGISTRY:latest"
            }
        }
        stage('Launch application') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
        stage('Docker Cleanup') {
            steps {
                script {
                    sh 'docker-compose stop'
                    sh 'docker system prune -a -f'
                }
            }
        }
    }
}