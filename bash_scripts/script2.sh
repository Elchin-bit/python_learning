#!/bin/bash
# Этот скрипт создает папку с именем, переданным как аргумент,
# и записывает в нее файл info.txt с текущей датой.
FOLDER_NAME=$1
mkdir $FOLDER_NAME
echo "Текущая дата и время записывается в файл..."
date
date > $FOLDER_NAME/info.txt
echo "Дата и время записаны в $FOLDER_NAME/info.txt"