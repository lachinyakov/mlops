#!/bin/bash

# Скрипт инициализации dvc
# ${BUCKET} Имя проекта/репозитория что бы подключиться к нужному бакету в хранилище

# инициализируем dvc
dvc init &&
# добавляем бакет стораджа
dvc remote add -d storage s3://${BUCKET} &&
# устанавливаем что доступ в localhost в minio
dvc remote modify storage endpointurl http://127.0.0.1:9000 &&
# устанавливаем права доступа для хранилища
dvc remote modify storage credentialpath .aws/creds &&
echo "dvc setting is success" && exit 0 ||
echo "fail to setting dvc" && exit 1;