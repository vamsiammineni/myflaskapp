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
                }
            }
        }
        stage('Test the application') {
            steps {
                script {
                    if(sh 'curl localhost:80' == 'This is our home page') {
                        return True
                     } else {
                        return False
                     }
                }
            }
        }
    }
}