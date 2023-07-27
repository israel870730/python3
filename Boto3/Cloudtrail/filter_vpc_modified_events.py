import boto3
from datetime import datetime, timedelta

def filter_vpc_modified_events():
    # Configura el cliente de CloudTrail
    cloudtrail_client = boto3.client('cloudtrail')

    # Calcula la fecha de hace 3 días
    three_days_ago = datetime.now() - timedelta(days=3)

    # Define el rango de tiempo para buscar eventos desde hace 3 días hasta ahora
    start_time = datetime(year=three_days_ago.year, month=three_days_ago.month, day=three_days_ago.day)
    end_time = datetime.now()

    # Define los filtros para eventos de modificación y eventos de VPC
    event_filters = [
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'Modify*'
        },
        {
            'AttributeKey': 'EventSource',
            'AttributeValue': 'ec2.amazonaws.com'
        }
    ]

    # Realiza la búsqueda en los registros de eventos con los filtros
    response = cloudtrail_client.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        LookupAttributes=event_filters
    )

    # Filtra solo los eventos que tengan una identificación de recurso de VPC (por ejemplo, VPC ID)
    vpc_modified_events = [event for event in response['Events'] if is_vpc_event(event)]

    return vpc_modified_events

def is_vpc_event(event):
    # Verifica si el evento tiene recursos y si algún recurso es una VPC
    if 'Resources' in event:
        for resource in event['Resources']:
            if 'ResourceType' in resource and resource['ResourceType'] == 'AWS::EC2::VPC':
                return True
    return False

# Ejecuta la función para filtrar los eventos de modificación relacionados con VPC
vpc_modified_events = filter_vpc_modified_events()

# Imprime los eventos de modificación relacionados con VPC
for event in vpc_modified_events:
    print(event)
