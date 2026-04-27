FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libgomp1

RUN pip install -r requirements.txt

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
