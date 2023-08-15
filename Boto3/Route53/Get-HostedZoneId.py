import boto3

# Crea un cliente de Route53
route53_client = boto3.client('route53')

# Define el nombre de la zona hospedada
hosted_zone_name = 'reno.cst.vficloud.net'

# Obtiene la lista de zonas hospedadas
response = route53_client.list_hosted_zones_by_name(DNSName=hosted_zone_name)

# Verifica si se encontró la zona hospedada
if response['HostedZones']:
    # Obtiene el HostedZoneId de la primera zona encontrada (puede haber más de una)
    hosted_zone_id = response['HostedZones'][0]['Id']
    print('HostedZoneId:', hosted_zone_id)
else:
    print('No se encontró la zona hospedada')
