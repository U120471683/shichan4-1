import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    print("使用者按下放開")
    led.toggle() #`toggle()` 方法會切換 LED 的狀態  #
    now = datetime.now() # 取得現在時間 
    now_str = now.strftime('%Y-%m-%d %H:%M:%S') # 轉換成字串
    print(now_str)
    if led.is_lit:  # 判斷 LED 是否亮著 # `is_lit` 屬性會回傳 LED 的狀態
        print("燈是開的")        
    else:
        print("燈是關的")

if __name__ == '__main__':
    button = Button(pin=18)  # 按鈕接在 GPIO 18 腳位 # 建立 Button 物件
    button.when_released = user_release # 按鈕放開時執行 user_release 函式
    led = LED(pin=25) # LED 接在 GPIO 25 腳位 # 建立 LED 物件
    signal.pause() # 等待訊號，程式不會結束 