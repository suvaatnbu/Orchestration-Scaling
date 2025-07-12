import boto3

elbv2 = boto3.client('elbv2')

response = elbv2.create_load_balancer(
    Name='my-alb',
    Subnets=['subnet-xxxxxxxx', 'subnet-yyyyyyyy'],  # Replace with actual subnet IDs
    Scheme='internet-facing',
    Tags=[{'Key': 'Name', 'Value': 'my-alb'}],
    Type='application',
    IpAddressType='ipv4'
)

print("✅ ALB Created:", response['LoadBalancers'][0]['LoadBalancerArn'])