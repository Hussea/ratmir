# اسم الملف: backup.ps1
# الغرض: نسخ احتياطي لقاعدة البيانات من MySQL داخل الكونتينر إلى مجلد backups

# الحصول على التاريخ الحالي لتسمية النسخة
$DATE = Get-Date -Format "yyyy-MM-dd_HH-mm"

# اسم النسخة داخل الكونتينر
$containerBackup = "/tmp/backup_$DATE.sql"

# أخذ نسخة من قاعدة البيانات داخل الكونتينر
docker exec ratmir_db sh -c "mysqldump -u root -proot ratmer > $containerBackup"

# نسخ النسخة من الكونتينر إلى مجلد backups على جهازك
docker cp "ratmir_db:$containerBackup" ".\backups\backup_$DATE.sql"

Write-Host "Backup completed: backups\backup_$DATE.sql"

# حذف النسخ القديمة (مثال: الاحتفاظ فقط بآخر 7 أيام)
Get-ChildItem -Path ".\backups" -Filter "*.sql" |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) } |
    Remove-Item
