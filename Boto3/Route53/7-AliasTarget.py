import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test6.reno.poc.vficloud.net.'
record_type = 'A'
ttl = 300
elb_dns = 'internal-k8s-renovite-6622965409-877192526.eu-west-2.elb.amazonaws.com'

# Crea el lote de cambios para el registro
change_batch = {
    'Changes': [
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': record_name,
                'Type': record_type,
                #'TTL': ttl,
                'AliasTarget': {
                    'HostedZoneId': 'ZHURV8PSTC4K8',
                    'DNSName': elb_dns,
                    'EvaluateTargetHealth': False
                }
            }
        }
    ]
}

# Crea el registro en Route53
response = route53_client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch=change_batch
)

print('Registro creado exitosamente.')
