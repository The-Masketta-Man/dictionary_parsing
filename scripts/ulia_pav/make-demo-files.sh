#!/env bash

# Это скрипт для создания примеров html-файлов в папке $SOURCE_DIR

SOURCE_DIR="./in"

for i in {01..10}; do
    echo "Статья $i" > "$SOURCE_DIR/$i.html" 
done