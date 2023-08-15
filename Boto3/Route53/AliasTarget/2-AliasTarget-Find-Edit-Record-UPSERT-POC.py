import boto3
from inputs_poc import *
# from inputs_poc import hosted_zone_id
# from inputs_poc import weight_100
# from inputs_poc import weight_0
# from inputs_poc import elb_arn_100
# from inputs_poc import elb_arn_0
# from inputs_poc import records_to_modify
# from inputs_poc import record_type

# Crea un cliente de Route53
route53_client = boto3.client('route53')

for record in records_to_modify:
    # Compruebo que existe el registro que se quiere modificar
    try:

        # Obtiene el registro existente
        response = route53_client.list_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            StartRecordName=record['record_name'],
            StartRecordType=record_type,
            MaxItems='1'
        )

        # existing_record = response['ResourceRecordSets'][0]
        # record_find = existing_record['Name']
        print('Registro buscado:')
        print(record['record_name'])
        print()
        #print(record_find)

        # Verifica si se encontró el registro
        if 'ResourceRecordSets' in response and len(response['ResourceRecordSets']) > 0 and response['ResourceRecordSets'][0]['Name'] == record['record_name'] :
        #if 'ResourceRecordSets' in response and len(response['ResourceRecordSets']) > 0 :
            # El registro se encontró en la lista de ResourceRecordSets
            record = response['ResourceRecordSets'][0]['Name']
            print('Registro encontrado:')
            print(record)
            print()

        else:
            print('El registro no se encontró en la zona hospedada.')
            print(record)

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
                    'SetIdentifier': 'NewLB',
                    'Weight': weight_100,
                    'AliasTarget': {
                        'HostedZoneId': 'ZHURV8PSTC4K8',
                        'DNSName': elb_arn_100,
                        'EvaluateTargetHealth': False
                    }
                }
            },
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': existing_record['Name'],
                    'Type': existing_record['Type'],
                    'SetIdentifier': 'OldLB',
                    'Weight': weight_0,
                    'AliasTarget': {
                        'HostedZoneId': 'ZHURV8PSTC4K8',
                        'DNSName': elb_arn_0,
                        'EvaluateTargetHealth': False
                    }
                }
            }
        ]
    }

    # Aplica los cambios al registro
    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch=change_batch
    )

    #print('Registro modificado exitosamente.')
    # print(f'Registro {record["record_name"]} modificado exitosamente.')
    # print('-------')

    print('Registro modificado:')
    print(existing_record['Name'])
    print('-------')