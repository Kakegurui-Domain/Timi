FROM python:3.10.1-buster

WORKDIR /root/Userbot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","timi.py"]
