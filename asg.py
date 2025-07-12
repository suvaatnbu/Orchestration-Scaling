import boto3

autoscaling = boto3.client('autoscaling')

response = autoscaling.create_auto_scaling_group(
    AutoScalingGroupName='my-asg',
    LaunchTemplate={
        'LaunchTemplateId': 'lt-xxxxxxxxxxxxx',  # Replace with your template ID
        'Version': '$Latest'
    },
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=2,
    VPCZoneIdentifier='subnet-xxxxxxxx,subnet-yyyyyyyy',  # Replace with actual subnets
)

print("✅ Auto Scaling Group Created:", response)