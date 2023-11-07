import boto3
import json
from values import ECS_TASK_POLICY_ARN, ECS_TASK_POLICY_DESC, ECS_TASK_POLICY_JSON, ECS_TASK_POLICY_NAME, ECS_TASK_ROLE_JSON, ECS_TASK_ROLE_NAME, ECS_TASK_ROLE_DESC

client = boto3.client('iam')

def create_role():
    try:
        response = client.create_role(
            RoleName=ECS_TASK_ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(ECS_TASK_ROLE_JSON),
            Description=ECS_TASK_ROLE_DESC
        )
        return response['Role']
    except Exception as e:
        print(str(e))
        return False

def create_policy():
    try:
        response = client.create_policy(
            PolicyName=ECS_TASK_POLICY_NAME,
            PolicyDocument=json.dumps(ECS_TASK_POLICY_JSON),
            Description=ECS_TASK_POLICY_DESC
        )
        return response['Policy']
    except Exception as e:
        print(str(e))
        return False

def attach_policy_to_role():
    try:
        client.attach_role_policy(
            RoleName=ECS_TASK_ROLE_NAME,
            PolicyArn=ECS_TASK_POLICY_ARN
        )
    except Exception as e:
        print(str(e))
        return False

def detach_policy_from_role():
    try:
        client.detach_role_policy(
            RoleName=ECS_TASK_ROLE_NAME,
            PolicyArn=ECS_TASK_POLICY_ARN
        )
    except Exception as e:
        print(str(e))
        return False

def delete_policy():
    try:
        client.delete_policy(
            PolicyArn=ECS_TASK_POLICY_ARN
        )
    except Exception as e:
        print(str(e))
        return False

def delete_role():
    try:
        client.delete_role(
            RoleName=ECS_TASK_ROLE_NAME
        )
    except Exception as e:
        print(str(e))
        return False


