import boto3
from values import (
    ECS_CLUSTER_NAME, DOCKER_IMAGE_URI, ECS_CONTAINER_NAME, 
    ECS_TASK_DEFINITION_NAME, ECS_TASK_ROLE_ARN
)

client = boto3.client('ecs')

def create_cluster():
    try:
        response = client.create_cluster(
            clusterName=ECS_CLUSTER_NAME
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False

def delete_cluster():
    try:
        response = client.delete_cluster(
            cluster=ECS_CLUSTER_NAME
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False

def create_task_definition():
    try:
        response = client.register_task_definition(
            family=ECS_TASK_DEFINITION_NAME,
            taskRoleArn=ECS_TASK_ROLE_ARN,
            executionRoleArn=ECS_TASK_ROLE_ARN,
            networkMode='awsvpc',
            containerDefinitions=[
                {
                    'name': ECS_CONTAINER_NAME,
                    'image': f'{DOCKER_IMAGE_URI}:latest',
                    'portMappings': [
                        {
                            'containerPort': 5000,
                            'protocol': 'tcp'
                        },
                    ],
                    'essential': True,
                    'logConfiguration': {
                        'logDriver': 'awslogs',
                        'options': {                            
                            'awslogs-group': f'/ecs/{ECS_TASK_DEFINITION_NAME}',
                            'awslogs-region': 'us-east-1',
                            'awslogs-stream-prefix': 'ecs'
                        }
                    }
                }
            ],
            requiresCompatibilities=[
                'FARGATE',
            ],
            cpu='256',
            memory='512',
            runtimePlatform={
                'cpuArchitecture': 'X86_64',
                'operatingSystemFamily': 'LINUX'
            }
        )
        return response['taskDefinition']
    except Exception as e:
        print(str(e))
        return False
