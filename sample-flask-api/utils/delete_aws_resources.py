from aws_resources import ecr
from aws_resources import ecs
from aws_resources import iam

ecr.delete_repo()
print('Deleted ECR repo')
ecs.delete_cluster()
print('Deleted ECS Cluster')
iam.detach_policy_from_role()
print('Detached policy from the role')
iam.delete_policy()
print('Deleted policy')
iam.delete_role()
print('Deleted role')
