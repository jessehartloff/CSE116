FROM python:3.12

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
