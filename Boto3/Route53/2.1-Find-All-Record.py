import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define el ID de la zona hospedada
hosted_zone_id = 'Z06002641ST07BELWWL3N'

# Obtiene la lista de registros de la zona hospedada
response = route53_client.list_resource_record_sets(HostedZoneId=hosted_zone_id)

# Itera sobre los registros y muestra la información
for record_set in response['ResourceRecordSets']:
    record_name = record_set['Name']
    record_type = record_set['Type']
    ttl = record_set.get('TTL', 'N/A')
    setIdentifier = record_set.get('SetIdentifier', 'N/A')
    weight = record_set.get('Weight', 'N/A')
    #dnsname = record_set.get('AliasTarget', [])
    resource_records = record_set.get('ResourceRecords', [])
    
    #print(resource_records)
    #print(dnsname)
    #print(record_set)

    print('Nombre:', record_name)
    print('Tipo:', record_type)
    print('TTL:', ttl)
    print('SetIdentifier:', setIdentifier)
    print('Weight:', weight)

    # print('---')
    # print('DNSName:', dnsname)
    # print('---')

    # if record_set.get('AliasTarget') and 'DNSName' in record_set['AliasTarget']:
    #     dns_name = record_set['AliasTarget']['DNSName']
    #     print('LB:', dns_name)
    
    # Verifica si el registro tiene un balanceador de carga
    alias_target = record_set.get('AliasTarget')
    if alias_target and 'DNSName' in alias_target:
        dns_name = alias_target['DNSName']
        print('Balanceador de carga:', dns_name)

    for resource_record in resource_records:
        print('Valor:', resource_record['Value'])
    
    print('---')
