pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-creds')
        AWS_SECRET_ACCESS_KEY = credentials('aws-creds')
    }

    stages {
        stage('Prepare Scripts') {
            steps {
                sh 'cp -r /var/lib/jenkins/jenkins-boto3-scripts/* .'
            }
        }

        stage('Install Boto3') {
            steps {
                sh 'pip3 install boto3'
            }
        }

        stage('Run VPC Script') {
            steps {
                sh 'python3 vpc.py'
            }
        }

        stage('Run ALB Script') {
            steps {
                sh 'python3 alb.py'
            }
        }

        stage('Run ASG Script') {
            steps {
                sh 'python3 asg.py'
            }
        }

        stage('Update Route53') {
            steps {
                sh 'python3 route53_alb.py'
            }
        }
    }
}