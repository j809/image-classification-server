FROM python:3.7-buster

LABEL Image for handling image inferencing requests

COPY ./ app

RUN pip install -r /app/requirements.txt

CMD python /app/app.py
