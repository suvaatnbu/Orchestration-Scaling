lambda_client = boto3.client('lambda')

response = lambda_client.create_function(
    FunctionName='BackupDBLambda',
    Runtime='python3.9',
    Role='<LambdaExecutionRoleARN>',
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': open('backup_function.zip', 'rb').read()},
    Timeout=120,
)

