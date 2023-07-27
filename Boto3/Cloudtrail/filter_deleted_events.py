import boto3

def filter_deleted_events():
    # Configura el cliente de CloudTrail
    cloudtrail_client = boto3.client('cloudtrail')

    # Definir el filtro para eventos de eliminación (Delete)
    event_filter = {
        'AttributeKey': 'EventName',
        'AttributeValue': 'Delete*'
    }

    # Realiza la búsqueda en los registros de eventos
    response = cloudtrail_client.lookup_events(LookupAttributes=[event_filter])

    # Filtra solo los eventos que tengan una identificación de recurso de AWS (por ejemplo, ARN)
    deleted_events = [event for event in response['Events'] if event.get('Resources')]

    return deleted_events

# Ejecuta la función para filtrar los eventos de eliminación
deleted_events = filter_deleted_events()

# Imprime los eventos de eliminación
for event in deleted_events:
    print(event)
