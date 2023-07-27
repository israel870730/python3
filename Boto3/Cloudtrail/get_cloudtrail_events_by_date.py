import boto3
from datetime import datetime, timedelta

def get_cloudtrail_events_by_date(date):
    # Configura el cliente de CloudTrail
    cloudtrail_client = boto3.client('cloudtrail')

    # Convierte la fecha a formato de timestamp de Unix
    timestamp = int(date.timestamp())

    # Define el rango de tiempo para buscar eventos (1 día completo)
    start_time = datetime(year=date.year, month=date.month, day=date.day)
    end_time = start_time + timedelta(days=1)

    # Realiza una búsqueda en los registros de eventos con el filtro de tiempo
    response = cloudtrail_client.lookup_events(
        StartTime=start_time,
        EndTime=end_time
    )

    # Obtén los eventos
    events = response['Events']

    return events

# Define la fecha que deseas consultar (en formato año-mes-día)
fecha_deseada = '2023-07-25'
fecha_deseada_obj = datetime.strptime(fecha_deseada, '%Y-%m-%d')

# Ejecuta la función para obtener los eventos de CloudTrail en la fecha determinada
events_by_date = get_cloudtrail_events_by_date(fecha_deseada_obj)

# Imprime los eventos
for event in events_by_date:
    print(event)
