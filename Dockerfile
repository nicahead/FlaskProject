FROM python:3.6.7-alpine3.8

RUN mkdir -p /usr/src/app  && \
    mkdir -p /var/log/gunicorn

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir gunicorn && \
    pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . /usr/src/app

ENV PORT 8000
ENV FLASK_ENV testing
EXPOSE 8000 5000
CMD ["/usr/local/bin/gunicorn", "-c", "App/config/gunicorn.conf.py", "manager:app"]
