import boto3

route53 = boto3.client('route53')

response = route53.change_resource_record_sets(
    HostedZoneId='ZXXXXXXXXXXXX',  # Replace with your Hosted Zone ID
    ChangeBatch={
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'jenkins.example.com.',  # Replace with your domain
                    'Type': 'A',
                    'AliasTarget': {
                        'HostedZoneId': 'Z32O12XQLNTSW2',  # ALB zone ID
                        'DNSName': 'my-alb-123456789.us-east-1.elb.amazonaws.com',  # Replace
                        'EvaluateTargetHealth': False
                    }
                }
            }
        ]
    }
)

print("✅ Route 53 Record Updated:", response)