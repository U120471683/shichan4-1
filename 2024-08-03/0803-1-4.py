# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os.path
import os
from datetime import datetime
import random

def created_log_file():
    current_path = os.path.abspath(__name__) #取得目前檔案路徑
    directory_name = os.path.dirname(current_path) #取得目前資料夾路行
    data_path = os.path.join(directory_name,'data') #目前資料夾路徑加上data目錄
    
    if not os.path.isdir(data_path):
        print("沒有data的目錄,手動建立目錄")
        os.mkdir(data_path)
    else:
        print("目錄已經建立")
    

def record_info(log_path):


def main():

    data_path=created_directory()   #呼叫函式

    log_path = os.path.join(data_path,'iot.log') #建立log檔路徑
    if not os.path.isfile(log_path): #如果檔案不存在
        print("沒有iot.log檔,建立新檔")
        with open(log_path,mode='w',encoding='utf-8',newline='') as file: #建立檔案
            file.write('時間,濕度,溫度\n')  #寫入標題
        
    else:
        print("已經有log檔")

    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")     #取得現在時間
    humidity = str(random.randint(330,820) / 10)   #取得濕度
    celsius = str(random.randint(50,400) / 10)    #取得溫度
    with open(log_path,mode='a',encoding='utf-8',newline='') as file:   #寫入檔案
        file.write(now_str + ',' + humidity + ',' + celsius + "\n")     #寫入時間,濕度,溫度          


if __name__ == '__main__':

    main()
    
