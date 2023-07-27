import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define los parámetros del registro a modificar
hosted_zone_id = 'Z02608501GXHZ4F42FBXM'
record_name = 'test.reno.poc.vficloud.net.'
#record_type = 'A'
weight_100 = 100
weight_0 = 0


#for record in records_to_modify:
with open('registros.txt', 'r') as file:
    for line in file:
        record_data = line.strip().split(',')
        record_name, record_type, weight, elb_arn = record_data

        response = route53_client.list_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            StartRecordName=record_name,
            StartRecordType=record_type,
            MaxItems='1'
        )

        # Verifica si se encontró el registro
        if 'ResourceRecordSets' in response and len(response['ResourceRecordSets']) > 0:
            existing_record = response['ResourceRecordSets'][0]

            # Modifica el registro para cambiar la política de enrutamiento
            change_batch = {
                'Comment': 'Modificando el registro de enrutamiento de Simple a Weighted',
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': record_name,
                            'Type': record_type,
                            'SetIdentifier': 'case-100',
                            #'Weight': weight_100,
                            'Weight': int(weight),
                            'TTL': existing_record['TTL'],
                            'ResourceRecords': [
                                {
                                    'Value': elb_arn
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
                                    'Value': elb_arn
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

            #print('Registro modificado exitosamente.')
            #print(f'Registro {record["record_name"]} modificado exitosamente.')
            # print('Registro modificado:')
            # print(record['record_name'])
            # print('-------')

            print('Registro modificado:')
            print(existing_record['Name'])
            print('-------')