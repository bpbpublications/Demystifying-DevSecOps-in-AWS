import boto3
from values import ECR_REPO_NAME

client = boto3.client('ecr')

def create_repo():
    try:
        response = client.create_repository(
            repositoryName=ECR_REPO_NAME,
            imageScanningConfiguration={
                'scanOnPush': True
            }
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False

def delete_repo():
    try:
        response = client.delete_repository(
            repositoryName=ECR_REPO_NAME,
            force=True
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False