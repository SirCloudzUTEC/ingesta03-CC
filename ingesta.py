import csv
import os

import boto3
import pymysql

# Configuracion (se pasa por variables de entorno; los valores por defecto son de ejemplo)
host = os.environ.get("DB_HOST", "localhost")
puerto = int(os.environ.get("DB_PORT", "3306"))
usuario = os.environ.get("DB_USER", "root")
clave = os.environ.get("DB_PASSWORD", "")
baseDatos = os.environ.get("DB_NAME", "bd_ingesta")
tabla = os.environ.get("DB_TABLE", "personas")

ficheroUpload = "data.csv"
nombreBucket = os.environ.get("S3_BUCKET", "gcr-output-01")

# 1. Conectarse a MySQL y leer todos los registros de la tabla
conexion = pymysql.connect(host=host, port=puerto, user=usuario,
                           password=clave, database=baseDatos)
try:
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM `{tabla}`")
        registros = cursor.fetchall()
        columnas = [c[0] for c in cursor.description]
finally:
    conexion.close()

print(f"Registros leidos de {baseDatos}.{tabla}: {len(registros)}")

# 2. Guardar los registros en un archivo csv
with open(ficheroUpload, "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(columnas)
    escritor.writerows(registros)

print(f"Archivo {ficheroUpload} generado")

# 3. Subir el archivo csv al bucket S3
s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")
