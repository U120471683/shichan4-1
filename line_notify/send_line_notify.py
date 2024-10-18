import requests

def send_line_notify(token, message):
    # 設定 LINE Notify API 的 URL
    url = "https://notify-api.line.me/api/notify"
    
    # 設定請求的標頭，包含授權資訊
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # 設定請求的資料，包含要發送的訊息
    data = {
        "message": message
    }
    
    # 發送 POST 請求到 LINE Notify API
    response = requests.post(url, headers=headers, data=data)
    
    # 回傳狀態碼和回應內容
    return response.status_code, response.text

if __name__ == "__main__":
    # 你的 LINE Notify 存取權杖
    token = "FXVGdF2ffKqt85EWiSPGctGfLAIpzWBzyEseo18L4r3EN"
    
    # 要發送的訊息
    message = "Hello from LINE Notify!"
    
    # 呼叫函式並取得回應
    status_code, response_text = send_line_notify(token, message)
    
    # 印出狀態碼和回應內容
    print(f"Status Code: {status_code}")
    print(f"Response: {response_text}")
