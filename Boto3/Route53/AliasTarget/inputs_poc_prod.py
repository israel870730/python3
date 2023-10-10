# Define los parámetros del registro a modificar

#ID de la zona que se va a modificar
hosted_zone_id = '#-ID'

#Tipo de registro
record_type = 'A'

#Peso que van a tener los registros ponderados
weight_100 = 100
weight_0 = 0

#Aqui se ponen los LB, el que tiene valor 100 es a donde va a ir todo el trafico
elb_arn_100 = 'LB-1.'
elb_arn_0 = 'LB-2.'

#Registros que se van a modificar
records_to_modify = [
    {
        'record_name': 'record.domain.com.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'record1.domain.com.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'record2.domain.com.',
        'elb_arn': elb_arn_100
    }
]