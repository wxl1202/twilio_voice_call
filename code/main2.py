import os
from twilio.rest import Client

os.environ['TWILIO_ACCOUNT_SID'] = ''
os.environ['TWILIO_AUTH_TOKEN'] = ''

client = Client()

# 目標電話號碼和發送者電話號碼
to_phone = '+886917780800'  # 替換為接收者電話
from_phone = '+18597951791'  # 替換為你的 Twilio 電話號碼

# 播放的文字內容（作為參數）
message_content = "您好，這是來自系統的測試語音。希望您有美好的一天。"

call = client.calls.create(
    to=to_phone,
    from_=from_phone,
    twiml=f'<Response><Say voice="Google.cmn-TW-Standard-A" language="cmn-TW">{message_content}</Say></Response>'
)

print(f"呼叫建立成功，呼叫 SID: {call.sid}")
