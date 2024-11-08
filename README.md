# API example

## /v1/gf/call
```bash
# 本地開發
curl -X POST http://localhost:5000/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"您好，這是一則測試語音。\" }",
  "aaa": ""
}'

# dev
curl -X POST https://voice-call-1014802662897.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'

# dev: 撥打多號碼
#   使用逗號分隔，需使用國際電話格式，eg. +8869xxxxxxxx
curl -X POST https://voice-call-1014802662897.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "message": "{ \"phone\": \"+886905296673,+886933512675\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'

# prod
curl -X POST https://voice-call-842544503241.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'

# prod - 測試 DatasourceError
curl -X POST https://voice-call-842544503241.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "receiver": "\\[Google Chat\\] P0 - emergency",
  "status": "firing",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "alertname": "AAA 測試",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "aaa-log",
        "rulename": "aaa 連線異常 (payflow)",
        "severity": "emergency"
      }
    },
    {
      "status": "firing",
      "labels": {
        "alertname": "DatasourceError",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "bbb-log",
        "rulename": "bbb 連線異常 (payflow)",
        "severity": "emergency"
      }
    }
  ],
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'


# prod - 測試 DatasourceNoData
curl -X POST https://voice-call-842544503241.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "receiver": "\\[Google Chat\\] P0 - emergency",
  "status": "firing",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "alertname": "AAA 測試",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "aaa-log",
        "rulename": "aaa 連線異常 (payflow)",
        "severity": "emergency"
      }
    },
    {
      "status": "firing",
      "labels": {
        "alertname": "DatasourceNoData",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "bbb-log",
        "rulename": "bbb 連線異常 (payflow)",
        "severity": "emergency"
      }
    }
  ],
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'

# prod - 測試 Grafana 格式
curl -X POST https://voice-call-842544503241.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "receiver": "\\[Google Chat\\] P0 - emergency",
  "status": "firing",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "alertname": "AAA 測試",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "aaa-log",
        "rulename": "aaa 連線異常 (payflow)",
        "severity": "emergency"
      }
    },
    {
      "status": "firing",
      "labels": {
        "alertname": "BBB 測試",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "bbb-log",
        "rulename": "bbb 連線異常 (payflow)",
        "severity": "emergency"
      }
    }
  ],
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'


# prod - 測試 resolved 
curl -X POST https://voice-call-842544503241.asia-east1.run.app/v1/gf/call \
-H "Authorization: Bearer SzbRYzYTVvUbapq6" \
-H "Content-Type: application/json" \
-d '{
  "receiver": "\\[Google Chat\\] P0 - emergency",
  "status": "resolved",
  "alerts": [
    {
      "status": "resolved",
      "labels": {
        "alertname": "AAA 測試",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "aaa-log",
        "rulename": "aaa 連線異常 (payflow)",
        "severity": "emergency"
      }
    },
    {
      "status": "firing",
      "labels": {
        "alertname": "BBB 測試",
        "datasource_uid": "9wHKZOY7z",
        "grafana_folder": "PChome 24h",
        "notification-group": "pchome24h-services",
        "ref_id": "bbb-log",
        "rulename": "bbb 連線異常 (payflow)",
        "severity": "emergency"
      }
    }
  ],
  "message": "{ \"phone\": \"+886917780800\", \"tts\": \"網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理\" }",
  "aaa": ""
}'
```


# Cloud Build 打包 image 並上傳 GAR
```bash
# Dev
gcloud builds submit --project gcp-poc-384805 --tag asia.gcr.io/gcp-poc-384805/voice_call:rc0.1 .

# Prod
gcloud builds submit --project pchomeec-devops --tag asia.gcr.io/pchomeec-devops/voice_call:rc0.2 .
```

## 手動部署並設定 Cloud Run 環境變數
```bash
# twilio account SID
TWILIO_ACCOUNT_SID=aaa

# twilio token
TWILIO_AUTH_TOKEN=bbb

# status callback domain，即部署時產生的 Cloud Run Domain (不需要 https://)
DOMAIN=aa.bb.cc

# 使用外撥的電話號碼：月租號碼
PHONE_NUMBER='+17433308044'

# Audit 使用的 webhook 將撥打資訊送到窗裡
GOOGLE_CHAT_ROOM='https://chat.googleapis.com/v1/spaces/AAAAORiB-f4/messages?....'

# cloud run 設定 listen port 5000，對應 Dockerfile 設定。

# prod domain
https://voice-call-842544503241.asia-east1.run.app
```

## Grafana 設置: Alerting > Contact points > [Google Chat] P0 - emergency

Webhook

URL: https://voice-call-842544503241.asia-east1.run.app/v1/gf/call

HTTP Method: POST

Authorization Header - Credentials: 加入 TOKEN （目前為 hard code 在程式中） 

Message:
```bash
{
"phone": "+886905296673,+886933512675", 
"tts": "網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理"
}
```

## 參考文件
[On-Call voice API 簡報](https://docs.google.com/presentation/d/1zSnaBdJF1zqLWHDSM8kR7ZfaaCp7j5-rfLDCoruGUvs/edit#slide=id.p)

[Twilio - Get call status events during a call](https://www.twilio.com/docs/voice/make-calls#get-call-status-events-during-a-call)