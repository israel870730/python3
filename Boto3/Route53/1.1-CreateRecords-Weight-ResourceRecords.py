import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test3.reno.poc.vficloud.net'
weight_100 = 100
weight_0 = 0
type_a_value_100 = '10.0.0.1'
type_a_value_0 = '10.0.0.2'

# Crea el registro con la política de enrutamiento ponderado
change_batch = {
    'Comment': 'Creando un registro con enrutamiento ponderado',
    'Changes': [
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': record_name,
                'Type': 'A',
                'SetIdentifier': 'case-100',
                'Weight': weight_100,
                'TTL': 300,
                'ResourceRecords': [
                    {
                        'Value': type_a_value_100
                    }
                ]
            }
        },
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': record_name,
                'Type': 'A',
                'SetIdentifier': 'case-0',
                'Weight': weight_0,
                'TTL': 300,
                'ResourceRecords': [
                    {
                        'Value': type_a_value_0
                    }
                ]
            }
        }
    ]
}

# Crea los registros en Route53
response = route53_client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch=change_batch
)

print('Registros creados exitosamente.')
