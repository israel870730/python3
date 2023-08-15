# Define los parámetros del registro a modificar

#ID de la zona que se va a modificar
hosted_zone_id = 'Z06002641ST07BELWWL3N'

#Tipo de registro
record_type = 'A'

#Peso que van a tener los registros ponderados
weight_100 = 100
weight_0 = 0

#Aqui se ponen los LB, el que tiene valor 100 es a donde va a ir todo el trafico
elb_arn_100 = 'dualstack.internal-k8s-renovite-baaa363475-2032672493.eu-west-2.elb.amazonaws.com.'
elb_arn_0 = 'dualstack.internal-k8s-renovite-7e741991b4-567387560.eu-west-2.elb.amazonaws.com.'

#Registros que se van a modificar
records_to_modify = [
    {
        'record_name': 'test.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'prometheus.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'com-gb.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'elasticsearch.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'grafana.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'hsm-microservice.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'hsm-portal.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'hz-mancenter.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'kibana.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'kube-dashboard.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'l2.reno.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'login.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'prometheus-alertmanager.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'rcp-portal.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'recon-portal.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'sftp-cloud.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'sftp.reno.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'switch-portal.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'switch-txn.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    }
]