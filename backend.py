autoscaling = boto3.client('autoscaling')
ec2_resource = boto3.resource('ec2')

# Create Launch Template
lt = ec2.create_launch_template(
    LaunchTemplateName='MERNBackendTemplate',
    LaunchTemplateData={
        'ImageId': 'ami-0abcdef1234567890',  # Update with latest Amazon Linux 2 AMI
        'InstanceType': 't2.micro',
        'SecurityGroupIds': [sg_id],
        'UserData': '''
            #!/bin/bash
            yum update -y
            amazon-linux-extras install docker -y
            service docker start
            docker run -d -p 5000:5000 <your-backend-ecr-image>
        '''
    }
)
lt_id = lt['LaunchTemplate']['LaunchTemplateId']

# Create Auto Scaling Group
autoscaling.create_auto_scaling_group(
    AutoScalingGroupName='MERNBackendASG',
    LaunchTemplate={'LaunchTemplateId': lt_id, 'Version': '$Latest'},
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    VPCZoneIdentifier=subnet_id
)

