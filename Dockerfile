FROM python:3.7

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 5672
EXPOSE 5050

CMD [ "python", "publishers/access_logs.py" ]