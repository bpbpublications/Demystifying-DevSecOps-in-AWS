import json
import boto3
import random, string

def lambda_handler(event, context):
    security_hub = boto3.client('securityhub')
    findings =  event['dependencies'] #this may change with different tools
    result = []
    for security_issue in findings:
        finding = {
              "SchemaVersion": "2018-10-08",
              "Id": ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=7)),
                "Resources": [
                {
                    "Type": security_issue['name'],
                    "Id": "CodeBuild kjhakdlau09783o803hahjadkhdka",
                    "Partition": "aws",
                    "Region": "us-east-1",
                    "Tags": {
                    "TagKey": "TagValue"
                    }
                }
                ],
            "AwsAccountId": "493325875471",
            'Title': f'OWASP Dependency Check - Findings in {security_issue["name"]}',
            'Description': f'A vulnerability has been detected in {security_issue["name"]}',
            'ProductArn': 'arn:aws:securityhub:<REGION>:<ACCOUNT_ID>:product/<PRODUCT_NAME>',
            'GeneratorId': '<GENERATOR_ID>',
            'Severity': {
                'Normalized': int(security_issue['vulnerabilities'][0]['cvss_score']),
                'Product': int(security_issue['vulnerabilities'][0]['cvss_score'])
            },
            'Types': [
                'Software and Configuration Checks/Vulnerabilities'
            ],
            'RecordState': 'ACTIVE',
            'CreatedAt': '<TimeStamp>',
            'UpdatedAt': '<TimeStamp>',
            'ProductFields': {
                'resource_type': security_issue['name'],
                'resource_name': security_issue['name'],
                'vulnerability_id': security_issue['vulnerabilities'][0]['identifier']
            }
        }
        
        result.append(finding)
    
    response = security_hub.batch_import_findings(
        Findings=result
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
