#!/bin/bash

# أخذ نسخة احتياطية من قاعدة البيانات
DATE=$(date +%Y-%m-%d_%H-%M)
docker exec ratmir_db sh -c "mysqldump -u root -proot ratmer > /tmp/backup_$DATE.sql"

# نسخ النسخة من الكونتينر إلى مجلد backups على السيرفر
docker cp ratmir_db:/tmp/backup_$DATE.sql ./backups/backup_$DATE.sql

# حذف النسخ القديمة (مثال: الاحتفاظ فقط بآخر 7 أيام)
find ./backups/ -type f -mtime +7 -name "*.sql" -delete
