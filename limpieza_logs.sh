#!/bin/bash
# limpieza_logs.sh - Borrado de archivos .log
echo "Borrando archivos de log..."
rm -f ~/environment/*.log
echo "Limpieza completada el: $(date)"
