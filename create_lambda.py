import boto3
import zipfile

lambda_client = boto3.client('lambda', region_name='us-east-1')
iam_client = boto3.client('iam')

# 1. Create IAM Role for Lambda
role = iam_client.create_role(
    RoleName='lambda-execution-role',
    AssumeRolePolicyDocument='''{
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "lambda.amazonaws.com"},
        "Action": "sts:AssumeRole"
      }]
    }'''
)
role_arn = role['Role']['Arn']
print(f"✅ IAM Role Created: {role_arn}")

# Attach AWSLambdaBasicExecutionRole policy
iam_client.attach_role_policy(
    RoleName='lambda-execution-role',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
)

# 2. Create Deployment Package
with zipfile.ZipFile('lambda_function.zip', 'w') as z:
    z.writestr('lambda_function.py', """
def lambda_handler(event, context):
    return {'statusCode': 200, 'body': 'Hello from Lambda!'}
""")

# 3. Deploy Lambda Function
with open('lambda_function.zip', 'rb') as f:
    zipped_code = f.read()

lambda_client.create_function(
    FunctionName='MyLambdaFunction',
    Runtime='python3.12',
    Role=role_arn,
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': zipped_code},
    Timeout=10,
    MemorySize=128
)
print("✅ Lambda Function Created: MyLambdaFunction")

