import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
asg = boto3.client('autoscaling', region_name='ap-south-1')

ASG_NAME = 'backend-auto-scaling-group'
LAUNCH_TEMPLATE_NAME = 'backend-launch-template'

# Delete Auto Scaling Group
print("Deleting Auto Scaling Group...")
asg.delete_auto_scaling_group(
    AutoScalingGroupName=ASG_NAME,
    ForceDelete=True
)
print(f"✅ ASG `{ASG_NAME}` deletion initiated.")

# Delete Launch Template
print("Deleting Launch Template...")
ec2.delete_launch_template(
    LaunchTemplateName=LAUNCH_TEMPLATE_NAME
)
print(f"✅ Launch Template `{LAUNCH_TEMPLATE_NAME}` deleted.")

