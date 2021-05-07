FROM python:3.7-slim-buster

RUN pip install mlflow boto3 pymysql

CMD mlflow server --backend-store-uri mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}:${MYSQL_PORT}/${MYSQL_DATABASE} --default-artifact-root s3://${MLFLOW_BUCKET} --host 0.0.0.0
