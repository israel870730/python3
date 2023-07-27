import boto3
from datetime import datetime, timedelta

def filter_deleted_events_one_month_ago():
    # Configura el cliente de CloudTrail
    cloudtrail_client = boto3.client('cloudtrail')

    # Calcula la fecha de hace 1 mes
    one_month_ago = datetime.now() - timedelta(days=30)

    # Define el rango de tiempo para buscar eventos desde hace 1 mes hasta ahora
    start_time = datetime(year=one_month_ago.year, month=one_month_ago.month, day=one_month_ago.day)
    end_time = datetime.now()

    # Define el filtro para eventos de eliminación (Delete)
    event_filter = {
        'AttributeKey': 'EventName',
        'AttributeValue': 'Delete*'
    }

    # Realiza la búsqueda en los registros de eventos con el filtro de tiempo
    response = cloudtrail_client.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        LookupAttributes=[event_filter]
    )

    # Filtra solo los eventos que tengan una identificación de recurso de AWS (por ejemplo, ARN)
    deleted_events = [event for event in response['Events'] if event.get('Resources')]

    return deleted_events

# Ejecuta la función para filtrar los eventos de eliminación de hace 1 mes
deleted_events_one_month_ago = filter_deleted_events_one_month_ago()

# Imprime los eventos de eliminación de hace 1 mes
for event in deleted_events_one_month_ago:
    print(event)
