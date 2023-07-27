import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro a modificar
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test.reno.poc.vficloud.net.'
record_type = 'A'
weight_100 = 100
weight_0 = 0
type_a_value_100 = 'IP_DEL_CASO_100'
type_a_value_0 = 'IP_DEL_CASO_0'

# Obtiene el registro existente
response = route53_client.list_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    StartRecordName=record_name,
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
        },
        {
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': existing_record['Name'],
                'Type': existing_record['Type'],
                'SetIdentifier': 'case-100',
                'Weight': weight_100,
                'TTL': existing_record['TTL'],
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
                'Name': existing_record['Name'],
                'Type': existing_record['Type'],
                'SetIdentifier': 'case-0',
                'Weight': weight_0,
                'TTL': existing_record['TTL'],
                'ResourceRecords': [
                    {
                        'Value': type_a_value_0
                    }
                ]
            }
        }
    ]
}

# Aplica los cambios al registro
response = route53_client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch=change_batch
)

print('Registro modificado exitosamente.')
