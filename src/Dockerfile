FROM tiangolo/uwsgi-nginx-flask:flask-python3.5
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN python -m spacy download en_core_web_sm
COPY ./app /app
RUN echo "uwsgi_read_timeout 1200s;" > /etc/nginx/conf.d/custom_timeout.conf