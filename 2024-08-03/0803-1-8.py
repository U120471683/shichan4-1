# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os.path
import os
from datetime import datetime
import random

def created_log_file(file:str,folder:str='data')->str:
    current_path = os.path.abspath(__name__) #取得目前檔案路徑
    directory_name = os.path.dirname(current_path) #取得目前資料夾路行
    data_path = os.path.join(directory_name,folder) #目前資料夾路徑加上data目錄
    
    if not os.path.isdir(data_path):
        print(f"沒有{folder}的目錄,手動建立目錄")
        os.mkdir(data_path)
    else:
        print("目錄已經建立")

    log_path = os.path.join(data_path,file) #建立log檔路徑
    if not os.path.isfile(log_path): #如果檔案不存在
        print(f"沒有{file}檔,建立新檔")
        with open(log_path,mode='w',encoding='utf-8',newline='') as file: #建立檔案
            file.write('時間,濕度,溫度\n')  #寫入標題
        
    else:
        print("已經有log檔")   
    return log_path #回傳log_path
    

def record_info(log_path):
     

    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")     #取得現在時間
    humidity = str(random.randint(330,820) / 10)   #取得濕度
    celsius = str(random.randint(50,400) / 10)    #取得溫度
    with open(log_path,mode='a',encoding='utf-8',newline='') as file:   #寫入檔案
        file.write(now_str + ',' + humidity + ',' + celsius + "\n")  
           #寫入時間,濕度,溫度          


def main():

    now=datetime.now()
    current_file_name=now.strftime("%Y-%m-%d.log")
    log_path=created_log_file(current_file_name)  #呼叫函式   
    record_info(log_path)

    
if __name__ == '__main__':


    main()
    
