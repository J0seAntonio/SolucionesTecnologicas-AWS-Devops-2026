import json
import random

def lambda_handler(event, context):
    mensajes = ["Despliegue exitoso", "Microservicio activo", "DevOps Pro"]
    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': random.choice(mensajes)})
    }
