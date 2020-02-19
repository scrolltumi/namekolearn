FROM python:2.7.17

RUN apt-get update && apt-get -y install netcat && apt-get clean

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY config.yml ./

COPY start.sh ./

COPY algos.py ./

RUN chmod +x ./start.sh

CMD ["./start.sh"]