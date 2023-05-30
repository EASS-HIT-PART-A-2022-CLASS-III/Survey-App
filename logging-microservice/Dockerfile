FROM ubuntu

RUN apt-get update && apt-get -y install python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /logging-microservice
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
