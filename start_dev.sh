# django-admin compilemessages
## if local config file does not exist, clond one:
# test -f settings/dev.py || echo "=== warning: local.py does not exist, will initialize the file, please update the configs ==="
# test -f settings/dev.py || cp settings/dev.py settings/prod.py
# test -f settings/dev.py && sed -i '' 's/DEBUG = False/DEBUG = True/g' settings/dev.py 2> /dev/null

# synchronous web server for development:
# --settings=settings.dev
# python3 manage.py runserver 0.0.0.0:8000 $server_params

# for async web server:
# export DJANGO_SETTINGS_MODULE=settings.dev
gunicorn -w 3 -b 0.0.0.0:8000 myproject.asgi:application