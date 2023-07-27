import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro a modificar
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
#record_name = 'test.reno.poc.vficloud.net.'
record_type = 'A'

records_to_delete = [
    {
        'record_name': 'test.reno.poc.vficloud.net.'
    },
    {
        'record_name': 'test1.reno.poc.vficloud.net.'
    }
]

for record in records_to_delete:
    # Obtiene el registro existente
    response = route53_client.list_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        #StartRecordName=record_name,
        StartRecordName=record['record_name'],
        StartRecordType=record_type,
        MaxItems='1'
    )

    existing_record = response['ResourceRecordSets'][0]

    # Modifica el registro para cambiar la política de enrutamiento
    change_batch = {
        'Comment': 'Modificando el registro de enrutamiento de Simple a Weighted',
        'Changes': [
            {
                'Action': 'DELETE',
                'ResourceRecordSet': existing_record
            }
        ]
    }

    # Aplica los cambios al registro
    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch=change_batch
    )

    print(f'Registro {record["record_name"]} eliminado exitosamente.')
