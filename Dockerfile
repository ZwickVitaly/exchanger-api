FROM python:3.12-alpine
LABEL authors="zwickvitaly"
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY server ./

ENTRYPOINT uvicorn --host 0.0.0.0 --port 8080 app:app