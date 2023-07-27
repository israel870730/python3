import boto3
from datetime import datetime, timedelta

def filter_modified_events_three_days_ago():
    # Configura el cliente de CloudTrail
    cloudtrail_client = boto3.client('cloudtrail')

    # Calcula la fecha de hace 3 días
    three_days_ago = datetime.now() - timedelta(days=3)

    # Define el rango de tiempo para buscar eventos desde hace 3 días hasta ahora
    start_time = datetime(year=three_days_ago.year, month=three_days_ago.month, day=three_days_ago.day)
    end_time = datetime.now()

    # Define el filtro para eventos de modificación (Modify)
    event_filter = {
        'AttributeKey': 'EventName',
        'AttributeValue': 'Modify*'
    }

    # Realiza la búsqueda en los registros de eventos con el filtro de tiempo
    response = cloudtrail_client.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        LookupAttributes=[event_filter]
    )

    # Filtra solo los eventos que tengan una identificación de recurso de AWS (por ejemplo, ARN)
    modified_events = [event for event in response['Events'] if event.get('Resources')]

    return modified_events

# Ejecuta la función para filtrar los eventos de modificación de hace 3 días
modified_events_three_days_ago = filter_modified_events_three_days_ago()

# Imprime los eventos de modificación de hace 3 días
for event in modified_events_three_days_ago:
    print(event)
