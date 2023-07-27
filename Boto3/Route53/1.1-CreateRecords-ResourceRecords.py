import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
#record_name = 'test.reno.poc.vficloud.net'
value = '10.0.0.2'

records_to_modify = [
    {
        'record_name': 'test.reno.poc.vficloud.net',
        'elb_arn': value
    },
    {
        'record_name': 'test1.reno.poc.vficloud.net',
        'elb_arn': value
    }
]

for record in records_to_modify:
    # Crea el registro con la política de enrutamiento ponderado
    change_batch = {
        'Comment': 'Creando un registro con enrutamiento ponderado',
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': record['record_name'],
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': value
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

    print(f'Registro {record["record_name"]} creado exitosamente.')
