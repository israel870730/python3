# Define los parámetros del registro a modificar

#ID de la zona que se va a modificar
hosted_zone_id = 'Z060650324SLX0FC91XIA'

#Tipo de registro
record_type = 'A'

#Peso que van a tener los registros ponderados
weight_100 = 100
weight_0 = 0

#Aqui se ponen los LB, el que tiene valor 100 es a donde va a ir todo el trafico
elb_arn_100 = 'dualstack.internal-k8s-renovite-3638df1057-1380333530.eu-central-1.elb.amazonaws.com.'
elb_arn_0 = 'dualstack.internal-k8s-renovite-3638df1057-1380333530.eu-central-1.elb.amazonaws.com.'


records_to_modify = [
    {
        'record_name': 'prometheus-alertmanager.reno.prod.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'prometheus.reno.prod.vficloud.net.',
        'elb_arn': elb_arn_100
    }
]