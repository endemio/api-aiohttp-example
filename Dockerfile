FROM python:3.8

RUN mkdir -p /app

COPY /app  /app/scripts

WORKDIR /app/scripts

RUN pip install -r requirements.txt

RUN mkdir -p /app/storage

CMD [ "python", "./app.py" ]