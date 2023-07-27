import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro a modificar
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test1.reno.poc.vficloud.net'
record_type = 'A'
ttl = 300
weight = 100
ip_address = '192.0.2.11'

# Crea el lote de cambios para modificar el registro
change_batch = {
    'Changes': [
        {
            'Action': 'UPSERT',
            'ResourceRecordSet': {
                'Name': record_name,
                'Type': record_type,
                'TTL': ttl,
                'ResourceRecords': [
                    {
                        'Value': ip_address
                    }
                ],
                'SetIdentifier': 'weighted',
                'Weight': weight
            }
        }
    ]
}

# Modifica el registro en Route53
response = route53_client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch=change_batch
)

print('Registro modificado exitosamente.')
