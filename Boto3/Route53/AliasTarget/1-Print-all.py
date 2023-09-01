import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define el ID de la zona hospedada
hosted_zone_id = 'Z060650324SLX0FC91XIA'

# Obtiene la lista de registros de la zona hospedada
response = route53_client.list_resource_record_sets(HostedZoneId=hosted_zone_id)

# Itera sobre los registros y muestra la información
for record_set in response['ResourceRecordSets']:
    print(record_set)
        
    print('---')
