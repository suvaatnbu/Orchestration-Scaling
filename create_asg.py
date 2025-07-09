import boto3

autoscaling = boto3.client('autoscaling', region_name='us-east-1')
ec2 = boto3.client('ec2', region_name='us-east-1')

# Pre-requisites
launch_template_name = 'backend-launch-template'
ami_id = 'ami-0abcdef1234567890'  # ✅ Replace with your AMI ID
instance_type = 't3.micro'
key_name = 'your-keypair-name'     # ✅ Replace with your keypair name
sg_id = 'sg-xxxxxxxx'              # ✅ Replace with Security Group ID
subnet_ids = ['subnet-xxxxxxx', 'subnet-yyyyyyy']  # ✅ Replace with Subnet IDs

# 1. Create Launch Template
launch_template = ec2.create_launch_template(
    LaunchTemplateName=launch_template_name,
    LaunchTemplateData={
        'ImageId': ami_id,
        'InstanceType': instance_type,
        'KeyName': key_name,
        'SecurityGroupIds': [sg_id],
        'TagSpecifications': [{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'backend-instance'}]
        }]
    }
)
print(f"✅ Launch Template Created: {launch_template_name}")

# 2. Create Auto Scaling Group
asg = autoscaling.create_auto_scaling_group(
    AutoScalingGroupName='backend-asg',
    LaunchTemplate={
        'LaunchTemplateName': launch_template_name,
        'Version': '$Latest'
    },
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    VPCZoneIdentifier=','.join(subnet_ids),
    HealthCheckType='EC2',
    Tags=[
        {
            'ResourceId': 'backend-asg',
            'ResourceType': 'auto-scaling-group',
            'Key': 'Name',
            'Value': 'backend-asg',
            'PropagateAtLaunch': True
        }
    ]
)
print("✅ Auto Scaling Group Created: backend-asg")

