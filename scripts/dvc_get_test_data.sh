#!/bin/bash

# Получаем тестовый набор данных
dvc get https://github.com/iterative/dataset-registry get-started/data.xml -o data/data.xml &&
dvc add data/data.xml &&
git add data/.gitignore data/data.xml &&
echo "look a git status" && exit 0 ||
echo "fail tp get test data" && exit 1