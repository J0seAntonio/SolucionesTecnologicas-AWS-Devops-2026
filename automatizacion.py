import boto3
from datetime import datetime, timedelta

def listar_instancias():
    print("\n--- Listando Instancias EC2 ---")
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']}, Tipo: {instance['InstanceType']}, Estado: {instance['State']['Name']}")

def reporte_cpu():
    print("\n--- Reporte de Uso de CPU (Últimas 24h) ---")
    cw = boto3.client('cloudwatch')
    ec2 = boto3.client('ec2')
    instancias = ec2.describe_instances()
    
    for reservation in instancias['Reservations']:
        for instance in reservation['Instances']:
            id_instancia = instance['InstanceId']
            stats = cw.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': id_instancia}],
                StartTime=datetime.utcnow() - timedelta(days=1),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )
            print(f"Instancia {id_instancia}: " + (f"{stats['Datapoints'][0]['Average']}%" if stats['Datapoints'] else "Sin datos"))

def listar_s3():
    print("\n--- Listando Buckets S3 ---")
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"Bucket: {bucket['Name']}")
        # Listar objetos
        objetos = s3.list_objects_v2(Bucket=bucket['Name'])
        if 'Contents' in objetos:
            for obj in objetos['Contents']:
                print(f"  - Objeto: {obj['Key']}")

def consultar_autoscaling():
    print("\n--- Grupos de Auto Scaling ---")
    asg = boto3.client('autoscaling')
    response = asg.describe_auto_scaling_groups()
    for group in response['AutoScalingGroups']:
        print(f"Nombre: {group['AutoScalingGroupName']}")
        print(f"  Capacidad (Min: {group['MinSize']}, Max: {group['MaxSize']}, Deseada: {group['DesiredCapacity']})")

if __name__ == "__main__":
    listar_instancias()
    reporte_cpu()
    listar_s3()
    consultar_autoscaling()