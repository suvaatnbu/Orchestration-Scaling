import boto3

# AWS Config
ec2_client = boto3.client('ec2', region_name='us-east-1')
asg_client = boto3.client('autoscaling', region_name='us-east-1')

# Variables
ami_id = 'ami-0abcdef1234567890'  # Use Ubuntu 22.04 or Amazon Linux 2 AMI
instance_type = 't3.micro'
key_name = 'your-key-pair-name'
security_group_id = 'sg-xxxxxxxx'  # Open ports: 22 (SSH), 5000 (Backend)
backend_docker_image = 'your-dockerhub-username/backend:latest'
launch_template_name = 'backend-launch-template'
auto_scaling_group_name = 'backend-asg'

# 1️⃣ Create Launch Template
response = ec2_client.create_launch_template(
    LaunchTemplateName=launch_template_name,
    LaunchTemplateData={
        'ImageId': ami_id,
        'InstanceType': instance_type,
        'KeyName': key_name,
        'SecurityGroupIds': [security_group_id],
        'UserData': """#!/bin/bash
sudo apt update -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo docker run -d -p 5000:5000 {image}
""".format(image=backend_docker_image)
    }
)

print(f"✅ Launch Template created: {response['LaunchTemplate']['LaunchTemplateName']}")

# 2️⃣ Create Auto Scaling Group
asg_client.create_auto_scaling_group(
    AutoScalingGroupName=auto_scaling_group_name,
    LaunchTemplate={
        'LaunchTemplateName': launch_template_name,
        'Version': '$Latest'
    },
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=2,
    VPCZoneIdentifier='subnet-xxxxxxx,subnet-yyyyyyy',  # Your public/private subnets
    TargetGroupARNs=[
        'arn:aws:elasticloadbalancing:us-east-1:111122223333:targetgroup/your-target-group-name/abc123'
    ],
    HealthCheckType='EC2',
    HealthCheckGracePeriod=300
)

print(f"✅ Auto Scaling Group created: {auto_scaling_group_name}")

