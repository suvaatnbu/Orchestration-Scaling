import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region if needed

# 1. Create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']
print(f"✅ VPC Created: {vpc_id}")

# Enable DNS
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

# 2. Create Subnets
subnet1 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24', AvailabilityZone='us-east-1a')
subnet2 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.2.0/24', AvailabilityZone='us-east-1b')
subnet_ids = [subnet1['Subnet']['SubnetId'], subnet2['Subnet']['SubnetId']]
print(f"✅ Subnets Created: {subnet_ids}")

# 3. Create Internet Gateway and attach to VPC
igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
print(f"✅ Internet Gateway Attached: {igw_id}")

# 4. Create Route Table and associate with subnets
route_table = ec2.create_route_table(VpcId=vpc_id)
route_table_id = route_table['RouteTable']['RouteTableId']
ec2.create_route(RouteTableId=route_table_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
for subnet_id in subnet_ids:
    ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=route_table_id)
print(f"✅ Route Table Configured: {route_table_id}")

# 5. Create Security Group
sec_group = ec2.create_security_group(GroupName='backend-sg', Description='Security group for backend', VpcId=vpc_id)
sg_id = sec_group['GroupId']

# Allow inbound HTTP (port 80) and SSH (port 22)
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80,
         'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
    ]
)
print(f"✅ Security Group Created: {sg_id}")

