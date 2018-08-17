#!/usr/bin/env bash
git pull
kill -9 `ps -aux | grep 'python manage.py' | awk '{print $2}'` 2>/dev/null
nohup python manage.py runserver 0.0.0.0:8000 &