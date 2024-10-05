nginx -g "daemon on;" && /opt/venv/bin/gunicorn -b 0.0.0.0:8000 pyshort.wsgi
