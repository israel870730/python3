import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test9.reno.poc.vficloud.net.'
record_type = 'A'
ttl = 300
weight_0 = 0
weight_100 = 100
elb_arn_0 = 'internal-k8s-renovite-6622965409-877192526.eu-west-2.elb.amazonaws.com'
elb_arn_100 = 'internal-k8s-renovite-608827600a-1549390569.eu-west-2.elb.amazonaws.com'

# Crea el lote de cambios para el registro ponderado
change_batch = {
    'Changes': [
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': record_name,
                'Type': record_type,
                'SetIdentifier': 'weighted_0',
                'Weight': weight_0,
                'AliasTarget': {
                    'HostedZoneId': 'ZHURV8PSTC4K8',
                    'DNSName': elb_arn_0,
                    'EvaluateTargetHealth': False
                }
            }
        },
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': record_name,
                'Type': record_type,
                'SetIdentifier': 'weighted_100',
                'Weight': weight_100,
                'AliasTarget': {
                    'HostedZoneId': 'ZHURV8PSTC4K8',
                    'DNSName': elb_arn_100,
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

print('Registros ponderados creados exitosamente.')
