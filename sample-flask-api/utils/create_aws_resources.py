from aws_resources import ecr
from aws_resources import ecs
from aws_resources import iam

ecr.create_repo()
print('Created ECR repository')
ecs.create_cluster()
print('Created ECS Cluster')
iam.create_role()
print('Created ECS Task Role')
iam.create_policy()
print('Created ECS Task Execution Policy')
iam.attach_policy_to_role()
print('Attached policy to the role')
ecs.create_task_definition()
print('Created task definition')
