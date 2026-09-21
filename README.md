# ingesta02

Lee todos los registros de una tabla MySQL, los guarda en `data.csv` y sube el archivo a un bucket S3.

## Configuracion (variables de entorno)

| Variable | Descripcion | Por defecto |
|---|---|---|
| DB_HOST | Host de MySQL (ej. endpoint RDS o IP de la EC2) | localhost |
| DB_PORT | Puerto | 3306 |
| DB_USER | Usuario | root |
| DB_PASSWORD | Clave | (vacia) |
| DB_NAME | Base de datos | bd_ingesta |
| DB_TABLE | Tabla a leer | personas |
| S3_BUCKET | Bucket destino | dgt-ingesta-02 |

## Ejecucion

```bash
docker build -t ingesta02 .
docker run --rm \
  -e DB_HOST=<host> -e DB_USER=<user> -e DB_PASSWORD=<clave> \
  -e DB_NAME=bd_ingesta -e DB_TABLE=personas -e S3_BUCKET=<bucket> \
  -v ~/.aws:/root/.aws:ro \
  ingesta02
```

En una EC2 con rol IAM (LabRole) no hace falta montar `~/.aws`.
