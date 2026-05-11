#!/bin/bash
# usuarios.sh - Gestión de usuarios y permisos
echo "Creando usuario devops_user..."
sudo useradd devops_user
echo "Asignando permisos sobre el entorno..."
sudo chown -R devops_user:devops_user ~/environment
# Restaurar permisos para ec2-user (requisito de la tarea)
sudo chown -R ec2-user:ec2-user ~/environment
echo "Proceso de usuarios completado."
