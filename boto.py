# infra_provision.py
import boto3

# Initialize clients
ec2 = boto3.client('ec2')
autoscaling = boto3.client('autoscaling')
elbv2 = boto3.client('elbv2')

# Step 1: Create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

# Step 2: Create Internet Gateway and Attach
igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)

# Step 3: Create Subnet and Route Table
subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
subnet_id = subnet['Subnet']['SubnetId']

rtb = ec2.create_route_table(VpcId=vpc_id)
rtb_id = rtb['RouteTable']['RouteTableId']
ec2.create_route(RouteTableId=rtb_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=rtb_id)

# Step 4: Create Security Group
sg = ec2.create_security_group(GroupName='web-sg', Description='Allow HTTP and SSH', VpcId=vpc_id)
sg_id = sg['GroupId']
ec2.authorize_security_group_ingress(GroupId=sg_id, IpPermissions=[
    {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
    {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
])

# Step 5: Launch Configuration and ASG
autoscaling.create_launch_configuration(
    LaunchConfigurationName='web-launch-config',
    ImageId='ami-0abcdef1234567890',  # Replace with valid AMI
    InstanceType='t2.micro',
    SecurityGroups=[sg_id],
    KeyName='your-key-pair'
)

autoscaling.create_auto_scaling_group(
    AutoScalingGroupName='web-asg',
    LaunchConfigurationName='web-launch-config',
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=2,
    VPCZoneIdentifier=subnet_id
)

# Step 6: Create ALB, Target Group, Listener
lb = elbv2.create_load_balancer(
    Name='web-alb',
    Subnets=[subnet_id],
    SecurityGroups=[sg_id],
    Scheme='internet-facing',
    Type='application',
    IpAddressType='ipv4'
)
lb_arn = lb['LoadBalancers'][0]['LoadBalancerArn']

# Target Group
tg = elbv2.create_target_group(
    Name='web-targets',
    Protocol='HTTP',
    Port=80,
    VpcId=vpc_id,
    TargetType='instance'
)
tg_arn = tg['TargetGroups'][0]['TargetGroupArn']

# Listener
elbv2.create_listener(
    LoadBalancerArn=lb_arn,
    Protocol='HTTP',
    Port=80,
    DefaultActions=[{'Type': 'forward', 'TargetGroupArn': tg_arn}]
)

print(f"✅ Infrastructure created: VPC {vpc_id}, Subnet {subnet_id}, ASG 'web-asg', ALB ARN {lb_arn}")

# infra_teardown.py
# (Teardown script will delete resources in reverse order of creation.)

