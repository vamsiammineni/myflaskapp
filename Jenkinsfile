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
                    dockerImage = docker.build("${REGISTRY}:${env.BUILD_ID}")
                }
            }
        }
        stage('Deploy Image') {
            steps {
                script {
                    docker.withRegistry('', REGISTRYCREDS){
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $REGISTRY:${env.BUILD_ID}"
            }
        }
        stage('Launch application') {
            steps {
                script {
                    container = docker.image('myflaskapp:${env.BUILD_ID}').run('-p 5000:5000')
                }
            }
        }
    }
}