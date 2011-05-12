#!/bin/bash
/usr/bin/env python manage.py runserver --noreload 127.0.0.1:8088 &
S_ID=$!
/usr/bin/env python manage.py test
kill -9 $S_ID