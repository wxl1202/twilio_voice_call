# 使用 Python 官方映像檔作為基底
FROM python:3.9-slim

ENV TWILIO_ACCOUNT_SID=aaa
ENV TWILIO_AUTH_TOKEN=bbb
ENV DOMAIN=aa.bb.cc
ENV PHONE_NUMBER='+17433308044'
ENV TZ=Asia/Taipei
ENV GOOGLE_CHAT_ROOM=''

# 關閉 buffered 避免 log 輸出緩衝
# https://stackoverflow.com/questions/60828641/simplest-way-to-perform-logging-from-google-cloud-run
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "code/main3.py"]
