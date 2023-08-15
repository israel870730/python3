import boto3

# Crea un cliente de Route 53
route53_client = boto3.client('route53')

zone_name = 'reno.cst.vficloud.net.'
response = route53_client.list_resource_record_sets(
    HostedZoneId='Z06002641ST07BELWWL3N',
    StartRecordName=zone_name,
    StartRecordType='A',
    MaxItems='100'
)

records = response['ResourceRecordSets']

# Filtra los registros con un peso igual a 100
records_with_weight_100 = [record for record in records if record.get('Weight') == 100]

for record in records_with_weight_100:
    #Para obtener toda la info del registro
    #print(record)
    #Para obtener solo el nombre
    print(record['Name'])
    print('Nombre:', record['Name'])
    print('Type', record['Type'])
    print('Identifier', record['SetIdentifier'])
    print('Weight', record['Weight'])

    alias_target = record.get('AliasTarget')
    if alias_target and 'DNSName' in alias_target:
        dns_name = alias_target['DNSName']
        print('LB:', dns_name)
    
    print('-----')

