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
                    container = docker.image(REGISTRY + ":" + "${env.BUILD_ID}").run('-p 80:80')
                    echo container
                }
            }
        }
        stage('Test the application') {
            steps {
                script {
                    def response = sh(script: sh 'curl localhost:80', returnStdout: true)
                    if( response == 'This is our home page') {
                        return True
                     } else {
                        return False
                     }
                }
            }
        }
    }
}