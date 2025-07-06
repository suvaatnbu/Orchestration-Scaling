elbv2 = boto3.client('elbv2')

# Create Load Balancer
lb = elbv2.create_load_balancer(
    Name='mern-lb',
    Subnets=[subnet_id],
    SecurityGroups=[sg_id],
    Scheme='internet-facing',
    Type='application',
    IpAddressType='ipv4'
)
lb_arn = lb['LoadBalancers'][0]['LoadBalancerArn']

# Create Target Group
tg = elbv2.create_target_group(
    Name='mern-tg',
    Protocol='HTTP',
    Port=5000,
    VpcId=vpc_id,
    TargetType='instance'
)
tg_arn = tg['TargetGroups'][0]['TargetGroupArn']

# Create Listener
elbv2.create_listener(
    LoadBalancerArn=lb_arn,
    Protocol='HTTP',
    Port=80,
    DefaultActions=[{'Type': 'forward', 'TargetGroupArn': tg_arn}]
)

