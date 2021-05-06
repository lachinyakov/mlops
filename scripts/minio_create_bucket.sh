#!/bin/bash
# Скрипт создания бакета в хранилище
# ${PROJECT_BUCKET}      - бакет, имя которого должно быть имя проекта/репозитория, что бы не путаться потом
# ${MINIO_ROOT_USER}     - логин для minio
# ${MINIO_ROOT_PASSWORD} - пароль для minio

# Подключаемся к minio серверу c кредами из переменных окружения
mc alias set minio http://minio:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD} --api S3v4 &&
# создаем bucket ${PROJECT_BUCKET}
mc mb minio/${PROJECT_BUCKET} &&
echo 'bucket was created' && exit 0 ||
echo 'fail to create bucket' && exit 1;
