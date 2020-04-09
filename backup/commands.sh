#!/bin/bash
source env/bin/activate
python manage.py dbbackup -c -z
python manage.py mediabackup -c -z
python manage.py listbackups
git add backup/
git commit -m "backup"
git push