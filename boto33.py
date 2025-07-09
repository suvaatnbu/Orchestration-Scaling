import boto3

ec2 = boto3.client('ec2')

# 1. Create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']

# Enable DNS support
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})

# 2. Create Internet Gateway
igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)

# 3. Create Subnet
subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc_id)
subnet_id = subnet['Subnet']['SubnetId']

# 4. Create Route Table & Associate with Subnet
rt = ec2.create_route_table(VpcId=vpc_id)
rt_id = rt['RouteTable']['RouteTableId']
ec2.create_route(RouteTableId=rt_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
ec2.associate_route_table(RouteTableId=rt_id, SubnetId=subnet_id)
import boto3

ec2 = boto3.client('ec2')

# 1. Create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']

# Enable DNS support
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})

# 2. Create Internet Gateway
igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)

# 3. Create Subnet
subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc_id)
subnet_id = subnet['Subnet']['SubnetId']

# 4. Create Route Table & Associate with Subnet
rt = ec2.create_route_table(VpcId=vpc_id)
rt_id = rt['RouteTable']['RouteTableId']
ec2.create_route(RouteTableId=rt_id, DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
ec2.associate_route_table(RouteTableId=rt_id, SubnetId=subnet_id)

