import boto3

def get_all_cloudtrail_events():
    # Configura el cliente de CloudTrail
    cloudtrail_client = boto3.client('cloudtrail')

    # Realiza una búsqueda en los registros de eventos
    response = cloudtrail_client.lookup_events()

    # Obtén los eventos
    events = response['Events']

    # Verifica si hay más eventos en lotes adicionales y recupéralos
    while 'NextToken' in response:
        response = cloudtrail_client.lookup_events(NextToken=response['NextToken'])
        events.extend(response['Events'])

    return events

# Ejecuta la función para obtener todos los eventos de CloudTrail
all_events = get_all_cloudtrail_events()

# Imprime los eventos
for event in all_events:
    print(event)
