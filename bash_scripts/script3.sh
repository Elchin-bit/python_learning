#!/bin/bash
#Скрипт, который проверяет, существует ли файл, имя которого передано как аргумент.
FILE_NAME=$1

if [ -f "$FILE_NAME" ]; then
    echo "Файл X найден"
else
    echo "Файл X не найден"
fi