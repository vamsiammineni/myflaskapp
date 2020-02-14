pipeline {
    agent any
    environment {
        REGISTRY = "vamsiammineni/myflaskapp"
        REGISTRYCREDS = 'dockerhub'
        DOCKER_TAG = getDockerTag()
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
    }
}

def getDockerTag(){
    def tag = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}