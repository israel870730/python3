import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro a modificar
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test.reno.poc.vficloud.net.'
record_type = 'A'
weight_100 = 90
weight_0 = 10
type_a_value_100 = '192.68.100.10'
type_a_value_0 = '192.68.100.20'


# Compruebo que existe el registro que se quiere modificar
try:

    # Obtiene el registro existente
    response = route53_client.list_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        StartRecordName=record_name,
        StartRecordType=record_type,
        MaxItems='1'
    )

    # existing_record = response['ResourceRecordSets'][0]
    # record_find = existing_record['Name']
    print('Registro buscado:')
    print(record_name)
    print()
    #print(record_find)

    # Verifica si se encontró el registro
    if 'ResourceRecordSets' in response and len(response['ResourceRecordSets']) > 0 and response['ResourceRecordSets'][0]['Name'] == record_name :
        # El registro se encontró en la lista de ResourceRecordSets
        record = response['ResourceRecordSets'][0]['Name']
        print('Registro encontrado:')
        print(record)

    else:
        print('El registro no se encontró en la zona hospedada.')

except Exception as e:
    print('Ocurrió un error al buscar el registro:', str(e))
    print('Ocurrió un error al buscar el registro:')
    print(e.response['Error']['Message'])


#Edito el registro 
existing_record = response['ResourceRecordSets'][0]

# Modifica el registro para cambiar la política de enrutamiento
change_batch = {
    'Comment': 'Modificando el registro de enrutamiento de Simple a Weighted',
    'Changes': [
        {
            'Action': 'UPSERT',
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
            'Action': 'UPSERT',
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