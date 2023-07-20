FROM python:3.10

LABEL maintainer "Tobias Verbeke <tobias.verbeke@openanalytics.eu>"

COPY requirements.txt .

RUN pip install gradio fastapi uvicorn

WORKDIR /app

EXPOSE 8000

COPY app.py .

CMD [ "uvicorn" , "app:app", "--reload", "--host",  "0.0.0.0" ]