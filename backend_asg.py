# deploy_backend_asg.py

import boto3

# AWS Clients
ec2_client = boto3.client('ec2', region_name='ap-south-1')
asg_client = boto3.client('autoscaling', region_name='ap-south-1')

# Configuration
ami_id = 'ami-0f918f7e67a3323f0'
instance_type = 't2.micro'
key_name = 'jenkins22'
security_group_id = 'sg-0d9c056fc9f92043d'
subnet_ids = 'subnet-0c1842aca7dc1b6b0'
docker_image = 'suvaatnbu/backend:latest'
launch_template_name = 'backend-launch-template'
asg_name = 'backend-asg'

# Create Launch Template
response = ec2_client.create_launch_template(
    LaunchTemplateName=launch_template_name,
    LaunchTemplateData={
        'ImageId': ami_id,
        'InstanceType': instance_type,
        'KeyName': key_name,
        'SecurityGroupIds': [security_group_id],
        'UserData': f"""#!/bin/bash
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo docker run -d -p 5000:5000 {docker_image}
"""
    }
)

print(f"Launch Template created: {launch_template_name}")

# Create Auto Scaling Group
asg_client.create_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    LaunchTemplate={
        'LaunchTemplateName': launch_template_name,
        'Version': '$Latest'
    },
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=2,
    VPCZoneIdentifier=subnet_ids,
    HealthCheckType='EC2',
    HealthCheckGracePeriod=300
)

print(f"Auto Scaling Group created: {asg_name}")

# teardown_backend_asg.py

import boto3

asg_client = boto3.client('autoscaling', region_name='ap-south-1')
ec2_client = boto3.client('ec2', region_name='ap-south-1')

asg_name = 'backend-asg'
launch_template_name = 'backend-launch-template'

# Delete ASG
try:
    asg_client.delete_auto_scaling_group(
        AutoScalingGroupName=asg_name,
        ForceDelete=True
    )
    print(f"ASG {asg_name} deletion initiated.")
except Exception as e:
    print(f"Error deleting ASG: {e}")

# Delete Launch Template
try:
    ec2_client.delete_launch_template(LaunchTemplateName=launch_template_name)
    print(f"Launch Template {launch_template_name} deleted.")
except Exception as e:
    print(f"Error deleting Launch Template: {e}")

# Jenkinsfile

pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        AWS_ACCESS_KEY_ID = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
    }

    stages {

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t suvaatnbu/backend:latest ./backend'
            }
        }

        stage('Push Backend Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                    sh 'docker push suvaatnbu/backend:latest'
                }
            }
        }

        stage('Deploy Backend to ASG') {
            steps {
                withCredentials([aws(credentialsId: 'aws-credentials', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh 'python3 deploy_backend_asg.py'
                }
            }
        }
    }
} 

