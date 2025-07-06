pipeline {
    agent any
    environment {
        ECR_REPO = 'your-ecr-repo-uri'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $ECR_REPO:$IMAGE_TAG .'
                sh 'aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REPO'
                sh 'docker push $ECR_REPO:$IMAGE_TAG'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}

