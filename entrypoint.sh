sed -i -e "s/pyshort_server_name/$PYSHORT_HOST/g" /etc/nginx/http.d/pyshort.conf
nginx -g "daemon on;" && /opt/venv/bin/gunicorn -b 0.0.0.0:8000 pyshort.wsgi
