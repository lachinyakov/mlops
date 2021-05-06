#!/bin/bash

# Получаем тестовый набор данных
wget https://s3.amazonaws.com/keras-datasets/jena_climate_2009_2016.csv.zip
unzip jena_climate_2009_2016.csv.zip &&
rm jena_climate_2009_2016.csv.zip &&
mv jena_climate_2009_2016.csv data/data.csv
dvc add data/data.csv &&
git add data/.gitignore data/data.csv &&
echo "look a git status" && exit 0 ||
echo "fail tp get test data" && exit 1