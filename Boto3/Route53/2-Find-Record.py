import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro a modificar
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_type = 'A'

records_to_find = [
    {
        'record_name': 'test.reno.poc.vficloud.net.',
        'type': record_type
    },
    {
        'record_name': 'test3.reno.poc.vficloud.net.',
        'type': record_type
    },
    {
        'record_name': 'test9.reno.poc.vficloud.net.',
        'type': record_type
    }
]

for record in records_to_find:
    try:

        # Obtiene el registro existente
        response = route53_client.list_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            StartRecordName=record['record_name'],
            StartRecordType=record['type'],
            MaxItems='1'
        )

        print('Registro buscado:')
        print(record['record_name'])
        print()

        # Verifica si se encontró el registro
        if 'ResourceRecordSets' in response and len(response['ResourceRecordSets']) > 0 and response['ResourceRecordSets'][0]['Name'] == record['record_name'] :
            # El registro se encontró en la lista de ResourceRecordSets
            record = response['ResourceRecordSets'][0]['Name']
            print('Registro encontrado:')
            print(record)
            print('--------------------')

            #Para imprimir toda la info del registro
            print(response['ResourceRecordSets'])

        else:
            print('El registro no se encontró en la zona hospedada.')
            print('--------------------')

    except Exception as e:
        print('Ocurrió un error al buscar el registro:', str(e))
        print('Ocurrió un error al buscar el registro:')
        print(e.response['Error']['Message'])
