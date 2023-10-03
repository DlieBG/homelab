FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app/src
COPY *.py .

ENTRYPOINT [ "python3", "main.py" ]
