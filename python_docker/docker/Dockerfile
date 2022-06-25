# syntax=docker/dockerfile:1

FROM  python:3.9-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ADD https://github.com/aikaterhine/american-predictor/raw/main/model.pickle .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5006"]

ENV FLASK_APP rest_api_server