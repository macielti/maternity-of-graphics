FROM python:3

WORKDIR /app

RUN mkdir outputs

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY ./app /app

EXPOSE 5000

ENV FLASK_APP=main.py

CMD ["uwsgi", "wsgi.ini"]
