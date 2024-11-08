import os
import json
import time
import logging
import requests
from flask import Flask, request, jsonify
from twilio.rest import Client

# enable only for dev
# os.environ['TWILIO_ACCOUNT_SID'] = ''
# os.environ['TWILIO_AUTH_TOKEN'] = ''
# os.environ['DOMAIN'] = 'aa.bb.cc'
# os.environ['PHONE_NUMBER'] = '+17433308044'
# os.environ['GOOGLE_CHAT_ROOM'] = 'https://chat.googleapis.com/v1/spaces/AAAAORiB-f4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=znt0IanI-jpY9I0ox5f3bWs9jAF1XdcgVaiLQ81LEQA'

# 發出 audit notification 
def send_message_to_google_chat(webhook_url, message_text):
    """
    發送訊息至 Google Chat
    
    參數：
    - webhook_url: str，Google Chat 房間的 Webhook URL
    - message_text: str，您要發送的訊息文字
    
    回傳：
    - dict: 包含狀態碼和回應訊息的字典
    """
    # 要發送的訊息內容
    message = {
        "text": message_text
    }
    
    # 發送 POST 請求
    response = requests.post(
        url=webhook_url,
        headers={'Content-Type': 'application/json; charset=UTF-8'},
        data=json.dumps(message)
    )
    
    # 檢查回應
    if response.status_code == 200:
        return {"status": "success", "message": "訊息發送成功！"}
    else:
        return {"status": "error", "status_code": response.status_code, "response": response.text}


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

client = Client()

# 取得環境變數
from_phone = os.getenv('PHONE_NUMBER')
domain = os.getenv('DOMAIN')
webhook = os.getenv('GOOGLE_CHAT_ROOM')

# 定義有效的 token 清單
VALID_TOKENS = {"SzbRYzYTVvUbapq6", "DcYmDVbxSzSxMtTs", "uyqq6ncPbTg9wJKv"}

@app.route('/v1/app/call', methods=['POST'])
@app.route('/v1/gf/call', methods=['POST'])
def make_cal_gf():
    # 檢查 Authorization 標頭中的 token
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Unauthorized'}), 401

    token = auth_header.split(' ')[1]
    if token not in VALID_TOKENS:
        return jsonify({'error': 'Unauthorized'}), 401

    # 取得 JSON 資料
    data = request.get_json()
    print(json.dumps(data, indent=4))       # 留下 json data 後續除錯使用
    
    inner_message = json.loads(data.get('message', '{}'))
    phone_numbers = inner_message.get('phone')  # 取得逗號分隔的電話號碼
    message_content = inner_message.get('tts')
    
    if not phone_numbers or not message_content:
        return jsonify({'error': 'Missing phone or message content'}), 400
    
    # 檢查欄位是否此通知是 DatasourceError 或 DatasourceNoData 就不撥出 voice call
    found = any(alert['labels']['alertname'] in ["DatasourceError", "DatasourceNoData"] for alert in data['alerts'])
    
    if found:
        print("Found DatasourceError or DatasourceNoData, bypass call out.")
        return jsonify({'message': 'Found DatasourceError or DatasourceNoData'}), 200
    
    # 檢查是否為 resolve 就不撥出 voice call
    resolved_found = any(alert['status'] == "resolved" for alert in data['alerts'])
    
    if resolved_found:
        print("Found resolved, bypass call out.")
        return jsonify({'message': 'Found resolved'}), 200
    
    
    # 將逗號分隔的號碼轉為清單
    phone_list = [phone.strip() for phone in phone_numbers.split(',')]
    
    call_sids = []  # 用於儲存每次呼叫的 SID

    try:
        # 建立呼叫，並指定 status_callback 追蹤狀態
        for to_phone in phone_list:
            call = client.calls.create(
                to=to_phone,
                from_=from_phone,
                twiml=f'<Response><Say voice="Google.cmn-TW-Standard-A" language="cmn-TW"><prosody rate="80%">{message_content}</prosody></Say></Response>',
                status_callback=f'https://{domain}/call-status',
                status_callback_event=[
                    'initiated', 'ringing', 'answered', 'completed'
                ],
                timeout=60
            )
            # print(call.sid)
            call_sids.append(call.sid)
            timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
            send_message_to_google_chat(webhook, f"[{timestamp}] CallSid: {call.sid}, trigger voice call to {to_phone}, msg: {message_content}")
            
        return jsonify({'message': 'Call initiated', 'call_sids': call_sids}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Call Logs
# https://console.twilio.com/us1/monitor/logs/calls?frameUrl=%2Fconsole%2Fvoice%2Fcalls%2Flogs%3Fx-target-region%3Dus1%26__override_layout__%3Dembed%26bifrost%3Dtrue

# 接收 twilio callback
@app.route('/call-status', methods=['POST'])
def call_status():
    """處理 Twilio 的呼叫狀態更新"""
    # Print all POST data
    print("Received callback data:", request.form.to_dict())
    
    call_sid = request.form.get('CallSid')
    call_status = request.form.get('CallStatus')
    timestamp = request.form.get('Timestamp')

    print(f"[{timestamp}] Call SID: {call_sid}, Status: {call_status}")

    return '', 200

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'production'
    app.run(host='0.0.0.0', port=5000)
