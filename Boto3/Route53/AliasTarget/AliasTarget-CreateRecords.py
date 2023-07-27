import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
#record_name = 'test8.reno.poc.vficloud.net.'
record_type = 'A'
elb_arn_0 = 'dualstack.internal-k8s-renovite-49739b7d24-990850777.eu-west-2.elb.amazonaws.com.'

records_to_modify = [
    {
        'record_name': 'test.reno.poc.vficloud.net',
        'elb_arn': elb_arn_0
    },
    {
        'record_name': 'test1.reno.poc.vficloud.net',
        'elb_arn': elb_arn_0
    }
]

for record in records_to_modify:
    # Crea el lote de cambios para el registro ponderado
    change_batch = {
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': record['record_name'],
                    'Type': record_type,
                    'AliasTarget': {
                        'HostedZoneId': 'ZHURV8PSTC4K8',
                        'DNSName': elb_arn_0,
                        'EvaluateTargetHealth': False
                    }
                }
            }
        ]
    }

    # Crea los registros ponderados en Route53
    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch=change_batch
    )

    print(f'Registro {record["record_name"]} creado exitosamente.')
