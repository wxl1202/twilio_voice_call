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
```


# Cloud Build 打包 image 並上傳 GAR
```bash
# Dev
gcloud builds submit --project gcp-poc-384805 --tag asia.gcr.io/gcp-poc-384805/voice_call:rc0.1 .

# Prod
gcloud builds submit --project pchomeec-devops --tag asia.gcr.io/pchomeec-devops/voice_call:rc0.1 .
```

## 手動部署並設定 Cloud Run 環境變數
```bash
# twilio account SID
TWILIO_ACCOUNT_SID=aaa

# twilio token
TWILIO_AUTH_TOKEN=bbb

# status callback domain (不需要 https://)
DOMAIN=aa.bb.cc

# 使用外撥的電話號碼
PHONE_NUMBER='+17433308044'

# Audit 使用的 webhook 將撥打資訊送到窗裡
GOOGLE_CHAT_ROOM='https://chat.googleapis.com/v1/spaces/AAAAORiB-f4/messages?....'

# cloud run 設定 listen port 5000

# prod domain
https://voice-call-842544503241.asia-east1.run.app
```

## Grafana 設置: Alerting > Contact points > [Google Chat] P0 - emergency

Webhook

URL: https://voice-call-842544503241.asia-east1.run.app/v1/gf/call

HTTP Method: POST

Authorization Header - Credentials: 加入 TOKEN

Message:
```bash
{
"phone": "+886905296673,+886933512675", 
"tts": "網家工程值班自動語音，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理，P0 警告觸發，請立即上線處理"
}
```

## 參考文件
[On-Call voice API 簡報](https://docs.google.com/presentation/d/1zSnaBdJF1zqLWHDSM8kR7ZfaaCp7j5-rfLDCoruGUvs/edit#slide=id.p)