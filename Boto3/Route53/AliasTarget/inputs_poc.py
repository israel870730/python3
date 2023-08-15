# Define los parámetros del registro a modificar

hosted_zone_id = 'Z06002641ST07BELWWL3N'

record_type = 'A'

weight_100 = 100
weight_0 = 0

elb_arn_100 = 'dualstack.internal-k8s-renovite-7e741991b4-567387560.eu-west-2.elb.amazonaws.com.'
elb_arn_0 = 'dualstack.internal-k8s-renovite-baaa363475-2032672493.eu-west-2.elb.amazonaws.com.'


records_to_modify = [
    {
        'record_name': 'test.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    },
    {
        'record_name': 'prometheus.reno.cst.vficloud.net.',
        'elb_arn': elb_arn_100
    }
]